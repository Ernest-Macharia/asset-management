
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from . forms import SignUpForm, AssetForm, AppreciationForm, DepreciationForm
from . models import Asset, Appreciate, Depreciate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')


def register(request):

    form = SignUpForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)

            login(request, user)

            return redirect('login')
    else:

        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'dashboard')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})


def userLogout(request):
    logout(request)
    return render(request, 'login')


def dashboard(request):
    return render(request, 'dashboard.html')

def asset(request):
    return render(request, 'asset.html')


def register_asset(request):
    title = 'Page for adding new assets'
    if request.method == "GET":
        form = AssetForm()
        return render(request, "register_asset.html", {'form': form, 'title':title})
    else:
        form = AssetForm(data=request.POST or None)
        if form.is_valid():
            form.save()

            return redirect("/asset")


def get_assets(request):
    title = 'The list of all the assets added'
    context = {"get_assets": Asset.objects.all(), "title": title}
    return render(request, "assetview.html", context)




def edit_assets(request,id=None):
    item = get_object_or_404(Asset, id=id)
    if request.method == "POST":
        form = AssetForm(request.POST, item=item)
        if form.is_valid():
            form.save()

            return redirect("dashboard")
    else:
        form = AssetForm(item=item)
        return render(request, "edit_assets.html", {'form': form})


    
        


def delete_assets(request, pk):
    Asset.objects.filter(name=pk).delete()
    items = Asset.objects.all()
    context = {
        'items': items
    }
    return render(request, "assetview.html", context)
def calculate(request):
    return render(request, 'calculate.html')

def appreciation(request):
    if request.method == "GET":
        form = AppreciationForm()
        return render(request, "appreciate.html", {'form': form})
    else:
        form = AppreciationForm(data=request.POST or None)
        if form.is_valid():
            form.save()

            return redirect("/asset")

def depreciation(request):
    if request.method == "GET":
        form = DepreciationForm()
        return render(request, "depreciation.html", {'form': form})
    else:
        form = DepreciationForm(data=request.POST or None)
        if form.is_valid():
            form.save()

            return redirect("/asset")