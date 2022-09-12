from django.urls import path
from .import views

urlpatterns = [
    path('',views.register_function,name="register_function"),

    path('login',views.login_function,name="login"),
    path('home',views.home_function,name="home"),
    path('home_login',views.home_login_function,name="home_login"),
    path('home_page',views.home_page_function,name="home_page"),

    path('signout/',views.signout, name='signout'),

    path('payments',views.payments, name='payments'),
    path('payrecords',views.payrecords_function, name='payrecords'),

    path('payment_text',views.payment_text,name='payment_text'),
    path('payment_csv',views.payment_csv,name='payment_csv'),
    path('payment_pdf',views.payment_pdf,name='payment_pdf'),
    

    path('calendar',views.calendar,name="calendar"),
    
    
]