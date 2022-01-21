from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def contact(request):
    my_contact = {
        'phone': '12345678',
        'address': 'kampala',
        'my_items': [1,2,3,44,66,67]
    }
    return render(request, 'contact.html', my_contact)

def about(request):
    return render(request, 'about.html')

def login(request):
    pass
    #return render(request, 'login.html')


def register(request):
    pass
    #return render(request, 'register.html')



def logout(request):
    pass
    #return render(request, 'register.html')