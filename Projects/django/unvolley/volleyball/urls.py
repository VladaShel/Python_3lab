from django.urls import path, register_converter
from volleyball import views, converters
from volleyball.views import serve_nstu_icon

urlpatterns = [
    path('', views.index, name='home'),
    path('static/volleyball/images/nstu.ico', serve_nstu_icon, name='serve_nstu_icon'),
]


register_converter(converters.FourDigitYearConverter, "year4")
