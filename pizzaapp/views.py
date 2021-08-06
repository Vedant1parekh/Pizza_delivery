from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PizzaModel,CustomerModel,OrderModel
# Create your views here.
def adminloginview(request):
    return render(request,'C:/Users/Dell/Desktop/pizza/templates/adminlogin.html')
def authenntication(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None and user.username=='admin':
        login(request,user)
        return redirect('adminhomepage')
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid credentials")
        return redirect('adminloginpage')
    

    
def adminhomepage(request):
    context={'pizza':PizzaModel.objects.all()}
    return render(request,'C:/Users/Dell/Desktop/pizza/templates/adminhomepage.html',context)
def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')
def addpizza(request):
    na=request.POST['pizza']
    pr=request.POST['price']
    PizzaModel(name=na,price=pr).save()
    return redirect('adminhomepage')
def deletepizza(request,y):
    PizzaModel.objects.filter(id=y).delete()
    return redirect('adminhomepage')
def homepaegview(request):
    return render(request,"C:/Users/Dell/Desktop/pizza/templates/homepage.html")
def signup(request):
    name=request.POST['username']
    passw=request.POST['password']
    phoneno=request.POST['phoneno']
    
    #username already exists
    if User.objects.filter(username=name).exists():
        messages.add_message(request,messages.ERROR,"USer already exists")
        return redirect('homepage')


    #Username doesnt exist already
    User.objects.create_user(username=name,password=passw).save()
    lastobject=len(User.objects.all())-1
    CustomerModel(userid=User.objects.all()[int(lastobject)].id,phoneno=phoneno).save()
    messages.add_message(request,messages.ERROR,"USer Successfully Created")
    return redirect('homepage')
def userloginview(request):
    return render(request,'C:/Users/Dell/Desktop/pizza/templates/userlogin.html')
def userauthenticate(request):
    username=request.POST['loginname']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('customerpage')
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid credentials")
        return redirect('userloginpage')
def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    name=request.user.username
    context={'name':name,'pizzas':PizzaModel.objects.all()}
    return render(request,'C:/Users/Dell/Desktop/pizza/templates/customerview.html',context)
def userlogout(request):
    return redirect('userloginpage')
def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username=request.user.username
    print(request.user.password)
    phoneno=CustomerModel.objects.filter(userid=request.user.id)[0].phoneno
    add=request.POST['address']
    orderitem=""
    for pizza in PizzaModel.objects.all():
        pizzaid=pizza.id
        name=pizza.name
        price=pizza.price
        qty=request.POST.get(str(pizzaid)," ")
        if str(qty)!="0" and str(qty)!=" ":
            orderitem=orderitem+" "+name+" Total price "+str(int(qty)*int(price))+ "  Quantity : "+qty+"    "
    OrderModel(user=username,phoneno=phoneno,address=add,orderitems=orderitem).save()
    messages.add_message(request,messages.ERROR,"ORDER PLACED SUUCESSFULLY")
    return redirect('customerpage')
def myorders(request):
    orders=OrderModel.objects.filter(user=request.user.username)
    context={'orders':orders}
    return render(request,'C:/Users/Dell/Desktop/pizza/templates/userorders.html',context)
def adminorders(request):
    orders=OrderModel.objects.all()
    context={'orders':orders}
    return render(request,'C:/Users/Dell/Desktop/pizza/templates/adminorders.html',context)
def acceptorder(request,userid):
    orders=OrderModel.objects.filter(id=userid)[0]
    orders.orderstatus="Accepted"
    orders.save()
    return redirect('adminorder')
def declineorder(request,usrid):
    orders=OrderModel.objects.filter(id=usrid)[0]
    orders.orderstatus="Declined"
    orders.save()
    return redirect('adminorder')