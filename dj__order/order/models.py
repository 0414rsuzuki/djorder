from django.db import models
from django.contrib.auth.models import User

class Order_data(models.Model):
    company = models.CharField(max_length=30,null=True)
    order_item = models.CharField(max_length=30,null=True)
    order_count = models.IntegerField(null=True)
    order_number= models.IntegerField(null=True)
    order_manager = models.ForeignKey(User, on_delete=models.CASCADE,related_name='order_manager',null=True)
    order_date = models.DateTimeField(null=True)
    def __str__(self):
        return '<Order_data:id= \
            ' + self.company + ' \
            ' + str(self.id) + ', \
            ' + self.order_item + ' \
            ' + str(self.order_number) + '\
            ' + self.order_manager + '\
            ' + str(self.order_date) + '>'

class Mail_data(models.Model):
    company = models.ForeignKey(Order_data,null=True, on_delete=models.CASCADE,related_name='Mail_company')
    address = models.EmailField(null=True)
    def __str__(self):
        return '<Mail_data:id= \
            ' + str(self.id) + ', \
            ' + self.company + ' \
            ' + self.address +' >'
