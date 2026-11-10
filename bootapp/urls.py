from django.urls import path

from bootapp import views

urlpatterns = [
  path('',views.home,name='home'),
  path('starter-page/',views.starter_page,name='starter-page'),
  path('pricing/',views.pricing,name='pricing'),
  path('get-a-quote/',views.get_a_quote,name='get-a-quote'),
  path('contact/',views.contact,name='contact'),
  path('about/',views.about,name='about'),
  path('services/',views.services,name='services'),
  path('service-details/',views.service_details,name='service-details'),
]