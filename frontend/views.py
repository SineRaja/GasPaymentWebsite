from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from datetime import date
from django.contrib import messages
# Create your views here.

def index(request):
    error = ""
    if request.method == 'POST':
        sd = request.POST['customernumber']
        pwd = request.POST['password']
        connection = Customer.objects.filter(usercnum=sd).first()
        if connection is not None and connection.useradd == pwd:  
            viewbill = Bill.objects.filter(connection=connection, status='Not Paid')
            return render(request, 'viewmybill.html', locals())
        else:
            messages.info(request, 'There is no user found!')
            return redirect('index')
    return render(request, 'index.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['userfullname']
        p = request.POST['userpassword']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def viewmybill(request, pid):
    error = ""
    bill = Bill.objects.get(id=pid)
    if request.method == "POST":
        bill.status = "paid"
        try:
            bill.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'viewmybill.html', locals())


def admin_home(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    cus = Customer.objects.all().count()
    b = Bill.objects.all().count()
    d = {'cus': cus, 'b': b}
    return render(request, 'admin_home.html', d)


def add_Customer(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        c = request.POST['usercontactnumber']
        e = request.POST['email']
        a = request.POST['address']
        city = request.POST['city']
        s = request.POST['state']
        try:
            user = User.objects.create_user(
                first_name=fn, last_name=ln, username=e)
            Customer.objects.create(
                user=user, usercnum=c, useradd=a, userplace=city, userst=s)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_Customer.html', locals())


def view_Customer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    customer = Customer.objects.all()
    return render(request, 'view_Customer.html', locals())


def edit_Customer(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=request.user.id)
    customer = Customer.objects.get(id=pid)
    error = False
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        c = request.POST['contact']
        a = request.POST['address']
        city = request.POST['city']
        s = request.POST['state']

        user.first_name = fn
        user.last_name = ln
        customer.usercnum = c
        customer.useradd = a
        customer.userplace = city
        customer.userst = s
        user.save()
        customer.save()
        error = True

    d = {'customer': customer, 'user': user, 'error': error}
    return render(request, 'edit_Customer.html', locals())


def delete_Customer(request, pid):
    customer = Customer.objects.get(id=pid)
    customer.delete()
    return redirect('view_Customer')


def add_Bill(request):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    error = ""
    connection1 = Customer.objects.all()
    if request.method == "POST":
        usercnum = request.POST['connectionid']
        b = request.POST['newbilldate']
        cdreading = request.POST['currentdayreading']
        cpdreading = request.POST['previousdayreading']
        cnreading = request.POST['currentnightreading']
        cnpreading = request.POST['previousnightreading']
        cgreading = request.POST['currentgasreading']
        cgpreading = request.POST['previousgasreading']
        # t = request.POST['totalunit']
        cpud = request.POST['chargeperunitforday']
        cpun = request.POST['chargeperunitfornight']
        cpug = request.POST['chargeperunitforgas']
        cpuv = request.POST['stadingchargeper']
        fa = request.POST['finalamount']
        dd = request.POST['duedate']

        connection = Customer.objects.get(id=usercnum)
        try:
            Bill.objects.create(connection=connection, billformonth=b, 
                                crdayele=cdreading, prdayele=cpdreading,
                                dayelechargeperunit=cpud, crnightele=cnreading, 
                                prnightele=cnpreading, nightelechargeperunit=cpun,
                                crgas=cgreading, prgas=cgpreading, 
                                gaschargeperunit=cpug, standingcharge=cpuv,  
                                finalamount=fa, duedate=dd, status='Not Paid')
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_Bill.html', locals())


def add_billUser(request):
    error = ""
    connection1 = Customer.objects.all()
    if request.method == "POST":
        usercnum = request.POST['connectionid']
        b = request.POST['newbilldate']
        cdreading = request.POST['currentdayreading']
        cpdreading = request.POST['previousdayreading']
        cnreading = request.POST['currentnightreading']
        cnpreading = request.POST['previousnightreading']
        cgreading = request.POST['currentgasreading']
        cgpreading = request.POST['previousgasreading']
        # t = request.POST['totalunit']
        cpud = request.POST['chargeperunitforday']
        cpun = request.POST['chargeperunitfornight']
        cpug = request.POST['chargeperunitforgas']
        cpuv = request.POST['stadingchargeper']
        fa = request.POST['finalamount']
        dd = request.POST['duedate']

        connection = Customer.objects.get(id=usercnum)
        try:
            Bill.objects.create(connection=connection, billformonth=b, 
                                crdayele=cdreading, prdayele=cpdreading,
                                dayelechargeperunit=cpud, crnightele=cnreading, 
                                prnightele=cnpreading, nightelechargeperunit=cpun,
                                crgas=cgreading, prgas=cgpreading, 
                                gaschargeperunit=cpug, standingcharge=cpuv,  
                                finalamount=fa, duedate=dd, status='Not Paid')
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_billUser.html', locals())

def view_Bill(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    bill = Bill.objects.all()
    return render(request, 'view_bill.html', locals())


def delete_Bill(request, pid):
    bill = Bill.objects.get(id=pid)
    bill.delete()
    return redirect('view_Bill')


def Logout(request):
    logout(request)
    return redirect('index')


def payment(request, pid):
    error = ""
    bill = Bill.objects.get(id=pid)
    if request.method == "POST":
        bill.status = "paid"
        try:
            bill.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'payment.html', locals())


def billpayment(request, pid):
    error= ""
    bill = Bill.objects.get(id = pid)
    if request.method == "POST":
        bill.status = "paid"
        try:
            bill.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "billpayment.html", locals())
    