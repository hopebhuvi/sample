from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from bhuvi1.forms import Empform
from bhuvi1.models import Tech
from bhuvi1.models import Emp
from bhuvi1.forms import Stateform
from bhuvi1.forms import Districtform

# Create your views here.
def index(request):
    return HttpResponse('hiiiii')
def index1(request):
    n={'name':'ammu'}
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render(n))
def index2(request):
    return render(request,'index.html',{'name':'anu'})
def index3(request):
    n={}
    value=input("enter value")
    n['name']=value
    print(n)
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render(n))

def emp_reg(request):
    if request.method=="GET":
        emp=Empform()
        return render(request,'empreg.html',{'form':emp})
    else:
        #return HttpResponse('success')
        frm=Empform(request.POST)
        if frm.is_valid():
            frm.save()
            print(frm)
        return HttpResponse("Successfully submitted")
#-----------------------------------------------------------------------------------------------------------------
def tech_add(request):
    if request.method=="POST":
        fn=request.POST.get("fname")
        pho=request.FILES['ph']
        print(pho)
        print(fn)
        t=Tech.objects.create(first_name=fn,photo=pho)
        t.save()
        return HttpResponse("<script>window.alert('successfully added!.....')</script>")
    else:
        return render(request,'tech_ph.html')
#--------------------------------session&cookies---------------------------------------------------------------
def setsession(request):
    request.session["name"]="ammu"
    request.session["email"]="ammu@gmail.com"
    return HttpResponse("session set.......!")

def getsession(request):
    n=request.session["name"]
    e=request.session["email"]
    return HttpResponse(n +" and "+ e)

def delsession(request):
    del request.session["name"]
    return HttpResponse("successfully deleted.....!")

def setcook(request):
    res=HttpResponse("cookie set")
    res.set_cookie('name','ammu')
    return res

def getcook(request):
    b=request.COOKIES['name']
    return HttpResponse(b)
    

def empView(request):
    ep=Emp.objects.all()
    return render(request,'empView.html',{'data':ep})


def stud_del(request,o):
    print(o)
    st=Emp.objects.get(id=o)
    st.delete()
    return HttpResponse("<script>window.alert('successfully deleted!.......');window.location.href='/empView/'</script>")

def stud_edit(request,m):
    st=Emp.objects.get(id=m)
    return render(request,'edit.html',{'data':st})

def stud_update(request,b):
    st=Emp.objects.get(id=b)
    frm=Empform(request.POST,instance=st)
    frm.save()
    return HttpResponse("<script>window.alert('successfully updated!.....');window.location.href='/empView/'</script>")

# --------------------------task-------------------------------------------------------------------------------------------

def index1(request):
     return render(request,'home.html')

def form(request):
    if request.method=="POST":
        n=request.POST.get('name')
        p=request.POST.get('pass')
        # t=Form.objects.create(name=n,pas=p)
        # t.save()
        request.session['form_name']=n
        request.session['form_pas']=p
        return  HttpResponse("<script>window.alert('Uploaded successfully!.....and the session is set!......');window.location.href='/welcome/'</script>")
    else:
        return render(request,'login.html')


def edit(request):
    form_name=request.session.get('form_name')
    return render(request,'welcome.html',{'form_name':form_name})


def logout(request):
    if 'form_name' in request.session:
        del request.session['form_name']
        return HttpResponse("<script>window.alert('successfully Logout!.....');window.location.href='/'</script>")
    else:
        return HttpResponse("<script>window.alert('You are not logged out!.....');window.location.href='/'</script>")

def n_edit(request):
    return HttpResponse("<script>window.alert('You are not logged out!.....');window.location.href='/'</script>")

#-----------------------------------statedistrict-------------------------------------------------------------------

def stat(request):
    # if request.method=="GET":
    #     state=Stateform()
    #     return render(request,'state.html',{'form':state})
    # else:
    #     #return HttpResponse('success')
    #     frm=Stateform(request.POST)
    #     if frm.is_valid():
    #         frm.save()
    #         print(frm)
    #     return HttpResponse(("<script>window.alert('Successfully submitted!.....');window.location.href='/state.html/'</script>"))
    states=State.objects.all()
    return render(request,'state.html',{'states':states})

def dis(request):
    # if request.method=="GET":
    #     district=Districtform()
    #     return render(request,'district.html',{'form':district})
    # else:
    #     #return HttpResponse('success')
    #     frm=Districtform(request.POST)
    #     if frm.is_valid():
    #         frm.save()
    #         print(frm)
    #     return HttpResponse(("<script>window.alert('Successfully submitted!.....');window.location.href='/district.html/'</script>"))
    districts=District.objects.all()
    return render(request,'district.html',{'districts':districts})