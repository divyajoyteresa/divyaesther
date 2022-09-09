from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.contrib import auth, messages
from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate
from .forms import ExtendedUserCreationForm,UserProfileForm
# Create your views here.
from .models import City,District


def register(request):
    if request.method == "POST":
        form1 = ExtendedUserCreationForm(request.POST)
        form2 = UserProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            obj = form1.save()
            obj2 = form2.save(commit=False)
            obj2.user = obj
            obj2.save()
            username=form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            user=authenticate(username=username,password=password)


            return redirect('login')
    else:
        form1 = ExtendedUserCreationForm()
        form2 = UserProfileForm()

    return render(request, "register.html", {'form1':form1,'form2':form2})



def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    return render(request, 'options.html', {'cities': cities})