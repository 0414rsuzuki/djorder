from pdb import post_mortem
from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Order_data , Mail_data 
from .forms import OrderForm , AddressForm , NumberForm ,SendForm
from django.db.models import QuerySet , Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.core.paginator import Paginator

import os
import datetime
#from wkhtmltopdf.views import PDFTemplateView
#from xhtml2pdf import pisa

def index(request):#フォーム内容を表示。

    params = {
        'title': 'Order System',
        'form': OrderForm(),
        }
    return render(request,'order/index.html',params)

def mail_save(request):
    if request.method == 'POST':
        company = request.POST['company']
        address = request.POST['address']
        company = Order_data(company=company)
        mail_data = Mail_data(address=address)
        mail_data.save()
        company.save()
        return HttpResponseRedirect(reverse('check_order'))

def confilm(request):#フォーム内容をDBに保存。
    #value ='order_item' , 'order_count' 
    
    if request.method == 'POST':

        order_item = request.POST['order_item']
        order_count =request.POST['order_count']
        order_date = datetime.datetime.now()

        order_data = Order_data(order_item=order_item,\
        order_count=order_count,order_date = order_date)
        order_data.save()
    
    print_data = Order_data.objects.all()
    params = {
    'title': 'Order System',
    'form': OrderForm(),
    'message' : '発注商品を確認してください。',
    'print_data' : print_data,
            }

    return render(request,'order/confilm.html',params)

def delete(request,num):
    delete_data = Order_data.objects.get(id=num)
    delete_data.delete()
    return HttpResponseRedirect(reverse('confilm'))

def check_order(request):
    request.method == 'POST'
    print_data = Order_data.objects.all()
    params = {
        'print_data' : print_data,
        'message' : '発注書をメールで送信します。発注内容を確認してください。',
        'title' : 'Order Confirmation',
        'address': SendForm(),
        'order_number' : NumberForm(),
        #'company_data': company_data,
            }
    return render(request,'order/check.html',params)

def company_address(request):
    request.method == 'POST'
    company = request.POST['company']
    address = request.POST['address']
    Mail_data(company = company , address = address)
    Mail_data.save()
    return redirect('order/confilm',request)

def back(request):

    return redirect ('/order/confilm',request)


def mail(request):
    request.method == 'POST'
    title = '発注書の件'
    confilm_orderdata = Order_data.objects.all()
    order_number = request.POST['order_number']
    params = { 
        'title' : '発注書の件',
        'order_data' : confilm_orderdata,
        'date' : datetime.datetime.now(),
        'order_number' : order_number
            }
    address = request.POST['address']
    html_content = render_to_string('order/mail.html', params, request)
    message = strip_tags(html_content)
    from_email = 'ryu.s.outsider@gmail.com' # 送信者
    recipient_list = [address] # 宛先リスト
    send_mail(title, message, from_email, recipient_list)
    return render(request,'order/confilm_mail.html')

def history(request, num=1):
    data = Order_data.objects.all()
    page = Paginator(data,5)  
    params = {
        'title':'発注履歴',
        'message':'',
        'data': page.get_page(num),
            }
    return render(request,'order/history.html',params)

def confilm_delete(request):
    delete_data = Order_data.objects.all()
    delete_data.delete()
    return HttpResponseRedirect(reverse('index'))