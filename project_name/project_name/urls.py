from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('arduino/', views.arduino, name='arduino'),
    path('esp32/', views.esp32, name='esp32'),
    path('esp8266/', views.esp8266, name='esp8266'),
    path('raspberry_pi/', views.raspberrypi, name='raspberry_pi'),
    path('drone/', views.drone, name='drone'),
    path('lorawan/', views.loraban, name='lorawan'),
    path('arduino/blinkled.html', views.blinkled, name='blinkled'),
    path('arduino/temperature.html', views.temperature, name='temperature'),
    path('arduino/pushbutton.html', views.pushbutton, name='pushbutton'),
    path('arduino/buzzer.html', views.buzzer, name='buzzer'),
    path('arduino/ultrasonic.html',views.ultrasonic, name='ultrasonic'),
    path('arduino/dht.html',views.dht, name='dht'),
    path('arduino/pir.html', views.pir, name='pir'),
    path('arduino/lcd.html', views.lcd, name='lcd'),
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('', include('tutorial.urls')),
]
