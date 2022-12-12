from django.urls import path, include
from . import views
from order import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    path('confilm',views.confilm, name='confilm'),
    path('delete/<int:num>',views.delete, name='delete'),
    path('check_order',views.check_order, name='check_order'),
    path('back',views.back, name='back'),
    path('mail',views.mail, name='mail'),
    path('index',views.index, name='index'),
    path('mail_save',views.mail_save, name='mail_save'),
    path('<int:num>',views.history, name='history'),
    path('confilm_delete',views.confilm_delete, name='confilm_delete'),
]