from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters= list('')
    Capitals= list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    Lowers=list('abcdefghijklmnopqrstuvwxyz')
    Symbols= list('!@#$%^&*()')
    numbers= list('0123456789')


    if request.GET.get('Uppercase') :
        characters.extend(Capitals)
    if request.GET.get('lowercase') :
        characters.extend(Lowers)
    if request.GET.get('Special characters') :
        characters.extend(Symbols)
    if request.GET.get('Numbers') :
        characters.extend(numbers)
    


    length= int(request.GET.get('length'))

    


    testpassword= ''
    for i in range(length):
        testpassword+= random.choice(characters)
    return render(request,'generator/password.html', { 'password': testpassword })

