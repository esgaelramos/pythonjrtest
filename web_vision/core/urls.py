from django.urls import path

from core import views

app_name='core'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),

    # TEST 1 - HUMPTY DUMPTY
    path('humpty', views.humpty, name='humpty'),
    path('youhumpty', views.youhumpty, name='youhumpty'),

    # TEST 2 - SUMA
    path('suma', views.suma, name='suma'),
    path('yousuma', views.yousuma, name='yousuma'),

    # TEST 3 - DAY TO PROGRAMMER
    path('pday', views.pday, name='pday'),
    path('youpday', views.youpday, name='youpday'),
]
