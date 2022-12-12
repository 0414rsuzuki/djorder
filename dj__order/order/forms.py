from django import forms
from . import models
from .models import Order_data , Mail_data 

class OrderForm(forms.Form):
    order_item = forms.CharField(label='商品名',widget=forms.TextInput(attrs={'class':'form-control'}))
    order_count = forms.IntegerField(label='点数',widget=forms.NumberInput(attrs={'class':'form-control'}))

class NumberForm(forms.Form):
    order_number = forms.IntegerField(label='発注番号',widget=forms.NumberInput(attrs={'class':'form-control'}))

class AddressForm(forms.Form):
    company = forms.CharField(label='発注先名',widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.EmailField(label='メールアドレス',widget=forms.TextInput(attrs={'class':'form-control'}))

class SendForm(forms.Form):
    address = forms.EmailField(label='送信先',widget=forms.TextInput(attrs={'class':'form-control'}))
    