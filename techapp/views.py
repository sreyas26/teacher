from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import  Teacher 

# Create your views here.
def home(request):
    return render(request, 'reg.html')

def usercreate(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        address=request.POST['address']
        age=request.POST['age']
        email=request.POST['email']
        c_number=request.POST['numb']
        courses=request.POST['courses']
        image=request.FILES.get('file')

        if password == cpassword: # password matching ......
            if User.objects.filter(username=username).exists(): #check Username Already Exists ..
                messages. info(request, 'This username already exists !!!!!! ')
                #print("Username already Taken .. ")
                return redirect('/')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                
                tec = Teacher(address=address,age=age,c_number=c_number,courses=courses,image=image)
                tec.save()

        else:
            messages. info(request, 'Password doesnt match !!!!!!! ')
            print("Password is not Matching .. ")
            return redirect('/')
        return redirect('/')
    return render(request,'/')