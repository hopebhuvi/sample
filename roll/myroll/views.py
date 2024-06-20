from django.shortcuts import render

# Create your views here.

#----------------------register----------------------------------------------------------------------------------
def register(request):
    if request.method='POST'
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        usertype=request.POST['usertype']
        print('---------------------------')

user=User.objects.create_user(first_name=name,email=email,username=username,password=password,usertype=usertype)
        user.save()
        return HttpResponse('registration ok')
    else:
        return render(request,'register.html')

#-----------------------login----------------------------------------------------------------------------------
 

