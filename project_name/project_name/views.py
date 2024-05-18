from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def arduino(request):
    return render(request,'arduino.html')
def esp32(request):
    return render(request,'esp32.html')
def esp8266(request):
    return render(request,'esp8266.html')
def raspberrypi(request):
    return render(request,'raspberrypi.html')
def drone(request):
    return render(request,'drone.html')
def loraban(request):
    return render(request,'loraban.html')
def blinkled(request):
    return render(request,'blinkled.html')
def temperature(request):
    return render(request,'temperature.html')
def pushbutton(request):
    return render(request,'pushbutton.html')
def buzzer(request):
    return render(request,'buzzer.html')
def ultrasonic(request):
    return render(request,'ultrasonic.html')
def dht(request):
    return render(request,'dht.html')
def pir(request):
    return render(request,'pir.html')
def lcd(request):
    return render(request,'lcd.html')

