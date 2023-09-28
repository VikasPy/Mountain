from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth 
from django.contrib.auth import *
from django.core.mail import send_mail
from.models import *
from django.views.decorators.cache import never_cache

import pyotp
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    s_data=Story.objects.all()
    return render(request,'index.html',{'s_data':s_data})

never_cache
@login_required(login_url='login')
def all_story(request):
    s_data=Story.objects.all()
    return render(request,'all_story.html',{'s_data':s_data})

never_cache
@login_required(login_url='login')
def story_form(request):
    return render(request,'story_form.html')


never_cache
@login_required(login_url='login')
def help(request):
    if request.method=='POST':
            user=request.user
            email=request.POST['email']
            mobile=request.POST['phone']
            issue=request.POST['issue']
            when=request.POST['date']
            msg=request.POST['help']
            help_desk.objects.create(user=user,email=email,phone_number=mobile,issue_type=issue,issue_date=when,issue_explain=msg)
            messages.success(request,'Request Sent Succesfully....')
            return redirect("/")
        
    else:
     return render(request,'help.html')
         
         
         
        
         






def ab(request):
    return render(request,'ab.html')

def cd(request):
    return render(request,'cd.html')

def ef(request):
    return render(request,'ef.html')

def gh(request):
    return render(request,'gallery.html')
def ij(request):
    return render(request,'ij.html')


never_cache
@login_required(login_url='login')
def yatra_add(request):
    if request.method == 'POST':
        user=request.POST['fname']
        email=request.POST['email']
        lname=request.POST['lname']
        dob=request.POST['dob']
        m=request.POST['inlineRadioOptions']
        pin=request.POST['pincode']
        adhar=request.POST['adhar']
        mobile=request.POST['mobile']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        request.session['username']=user
        request.session['email']=email
        request.session['password']=password

        if cpassword==password:
                # if User.objects.filter(email=email).exists():
                #     messages.success(request,'email  already exist try another email')
                #     return redirect('login')
                if yatra.objects.filter(email=email).exists():
                    messages.success(request,'user already exist')
                    return redirect('admin_login')
                else:
                  yatra_mail(request)
                return render(request,'home.html')
    
        else:
           messages.error(request,'password does not matched ')
        return render(request,'yatra.html')
    
    else:
        return render(request,'yatra.html')


    



    

def signup(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        request.session['username']=username
        request.session['email']=email
        request.session['password']=password
        if cpassword==password:
                # if User.objects.filter(email=email).exists():
                #     messages.success(request,'email  already exist try another email')
                #     return redirect('login')
                if User.objects.filter(username=username).exists():
                    messages.success(request,'user already exist')
                    return redirect('login')
                else:
                  ottp(request)
                return render(request,'ottp.html')
    
        else:
          messages.error(request,'password does not matched ')
          return render(request,'signup.html')
    else:
        return render(request,'signup.html')

            
        
        

    
            


        
def login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
        #    return render(request,'home.html')
            return redirect("home")
        else:
            messages.error(request,'wrong password try again!')
            return redirect('login')
    else:
        return render(request,'login.html')
        
@never_cache
@login_required(login_url='login')   
def home(request):
    return render(request,'home.html')


@never_cache
@login_required(login_url='login')
def gallary(request):
    data=galary.objects.all()
    return render(request,'gallery.html',{'data':data})

never_cache
@login_required(login_url='login')
def register_guide(request):
    if request.method=='post':
        
         name=request.POST['name']
         surname=request.POST['surname']
         email=request.POST['email']
         phone=request.POST['phone']
         add=request.POST['add']
         dob=request.POST['dob']
         print(dob)
         edu=request.POST['edu']
         texp=request.POST['texp']
         spk=request.POST['spk']
         afil=request.POST['afil']
        
         yatra.objects.create(name=name,surname=surname,afil=afil,dob=dob,edu=edu,spk=spk,texp=texp,email=email,mobile=phone,adres=add)

         return render(request,'home.html')
    else:
        return render(request,'register_guide.html')
               






def logout(request):
    auth.logout(request)
    return redirect('index')
    
   
def ottp(request):
        o=''
        totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
        o+=totp.now()
        request.session['ottp']=o
            

        # if request.method=='POST':
        #     cod=request.POST['otpp']
        #     # if code==ott:
        #  messages.success(request,' signup succesfully')
        send_mail(
                "Travel Diaries Otp",
                f"Your OTP is : {o} Welcome to our community.We are happy to have you on board.Why don’t you follow our CEO on instagram https://www.instagram.com/iarrav/ Thanks Regards :Travel Diaries",
                "myarrav@gmail.com",
                [request.session['email']],
                fail_silently=False,
            )


        return render(request,'ottp.html')

def otp_vrify(request):

    if request.method=='POST':
        od=request.POST.get('ottp')
        s= request.session['username']
        if od==request.session['ottp']:
        #  set_pas=make_password(password=request.session['password'])
         User.objects.create_user(username=request.session['username'],email=request.session['email'],password=request.session['password'])
        #  User.is_active=True
         send_mail(
                "Signup Succesfully Done",
                f"Thank You! {s} You are singnup Succesfully. Welcome to our community.We are happy to have you on board.Why don’t you follow our CEO on instagram https://www.instagram.com/iarrav/ Thanks Regards :Travel Diaries",
                "myarrav@gmail.com",
                [request.session['email']],
                fail_silently=False,
            )
         return redirect('login')
            
        else:
            messages.error(request,'Otp does not match try again!')
            return render(request,'ottp.html')
        
def resend_otp(request):


    o=''
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    o+=totp.now()
    request.session['ottp']=o
    send_mail(
                "Travel Diaries Otp",
                f"Your new Otp is : {o} Welcome to our community.We are happy to have you on board.Why don’t you follow our CEO on instagram https://www.instagram.com/iarrav/ Thanks Regards :Travel Diaries",
                
                "myarrav@gmail.com",
                [request.session['email']],
                fail_silently=False,
            )
    otp_vrify(request)
    
    return render(request,'ottp.html')





def yatra_mail(request):
        # if request.method=='POST':
        #     cod=request.POST['otpp']
        #     # if code==ott:
        #  messages.success(request,' signup succesfully')
        send_mail(
                "Yatra registration form",
                f"Your Yatra registration form is submitted! We will Contact You shortly... Welcome to our community.We are happy to have you on board.Why don’t you follow our CEO on instagram https://www.instagram.com/iarrav/ Thanks Regards :Travel Diaries",
                "myarrav@gmail.com",
                [request.session['email']],
                fail_silently=False,
            )


        return render(request,'home.html')
    





