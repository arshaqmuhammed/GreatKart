from django.shortcuts import render,redirect
from random import randint
from django.conf import settings
from django.core.mail import send_mail


from customer.models import Customer
from seller.models import Seller
# Create your views here.


def customer_home(request):
    return render(request, 'customer/customer_home.html')


def store(request):
    return render(request, 'customer/store.html')               


def product_detail(request):
    return render(request, 'customer/product_detail.html')


def cart(request):
    return render(request, 'customer/cart.html')


def place_order(request):
    return render(request, 'customer/place_order.html')


def order_complete(request):
    return render(request, 'customer/order_complete.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def seller_register(request):
    msg = ''
    status = False

    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        company = request.POST['cmpname']
        bankname = request.POST['bankname']
        bankbranch = request.POST['bankbranch']
        accnumber = request.POST['accnumber']
        ifsc = request.POST['ifsc']
        picture = request.FILES['seller_image']
       
        seller_exist = Seller.objects.filter(email = email).exists()
        if not seller_exist:

            seller = Seller(
                firstname = firstname,
                lastname = lastname,
                email = email,
                gender = gender,
                city = city,
                country = country,
                picture = picture,
                accnumber = accnumber,
                company_name = company,
                bank_name =  bankname,
                bank_branch = bankbranch,
                ifsc = ifsc
            )
            
            seller.save()
            msg = 'Account created sccesfully..!!'
            status = True
        else:
            msg = 'Account already exists'
    return render(request, 'customer/seller_register.html', {'message' : msg})


def seller_login(request):
    msg = ''
    if request.method == "POST":
        s_email = request.POST['email']
        s_password = request.POST['password']
        
        seller = Seller.objects.filter(email = s_email , paswword = s_password)

        if seller.exists():
            # print('session')
            request.session['seller'] = seller[0].id
            request.session['seller_name'] = seller[0].firstname + ' ' + seller[0].lastname

            print("***********",request.session['seller'])
            return redirect('Seller:seller_home')
        else:
            msg = 'incorrect username or password' 
    

    return render(request, 'customer/seller_login.html',{'message': msg})


def customer_signup(request):
    msg = ''
    status = False
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        password = request.POST['password']

        customer_exist = Customer.objects.filter(email = email).exists()
        
        if not customer_exist:
            customer = Customer(
                firstname = firstname,
                lastname = lastname,
                email = email,
                gender = gender,
                city = city,
                country = country,
                paswword = password)
            customer.save()
            msg = 'Registration succesfull..!!'
            status = True
        else: 
            msg = 'Already registered'
        
    return render(request, 'customer/customer_signup.html',{'message': msg,'status':status})


def customer_login(request):
    msg = ''
    if request.method == "POST":
        c_email = request.POST['email']
        c_password = request.POST['password']
        
        customer = Customer.objects.filter(email = c_email , paswword = c_password)

        if customer.exists():
            print('session')
            request.session['customer'] = customer[0].id
            return redirect('customer:customer_home')
        else:
            msg = 'incorrect username or password'   

    return render(request, 'customer/customer_login.html',{'message':msg})


def forgot_password_customer(request):
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')
