from django.shortcuts import render,redirect
from .models import *
from  datetime import datetime
# Create your views here.
def home (request):
    return render(request,'App1/home.html',{})
def login (request):
    us=False
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=User.objects.get(email=email,password=password)
            print(user)
            return render(request,'App1/userhome.html',{'user':user})
        except:
            print('user not found')
            return render(request,'App1/login.html',{})

        
        
    else:
        return render(request,'App1/login.html',{})
def user (request):
    print(request.body)
    return render(request,'App1/userhome.html',{})
def topics(request):
    if request.method=='POST':
        try:
            user=User.objects.get(id=int(request.POST['user']))
            topics=Topic.objects.all()
        except:
            user=User.objects.get(id=int(request.POST['info']))
            topics=user.topic_set.all()
        

    return render(request,'App1/topics.html',{'user':user,'topic':topics})

def chats(request,id=int):
    if request.method=='POST':
        try:
    
            user=User.objects.get(id=int(request.POST['user']))
            topics=Topic.objects.get(id=id)
            allmass=topics.massage_set.all()
            userm=topics.massage_set.filter(sender=user)

        except:
            user=User.objects.get(id=int(request.POST['info']))
            massage=request.POST['massage']
            topics=Topic.objects.get(id=id)
            massage=topics.massage_set.create(sender=user,content=massage,date=datetime.now())
            userm=Massage.objects.filter(sender=user,topic=topics)
            print(userm)
            allmass=Massage.objects.filter(topic=topics).order_by('-id')


        

        return render(request,'App1/chats.html',{'user':user,'topic':topics,'allmass':allmass,'userm':userm,'x':1})
    else:
        return render(request,'App1/chats.html',{'error':'error'})

def add(request):
    if request.method=='POST':
        try:
            user=User.objects.get(id=int(request.POST['user']))
        except:
            user=User.objects.get(id=int(request.POST['info']))
            name=request.POST['name']
            topic=Topic.objects.create(name=name,creator=user)
            topic.save
        return render(request,'App1/add.html',{'user':user})

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        tg=request.POST['tg']
        phone=request.POST['phone']
        nick_name=request.POST['name']
        if request.POST['password']==request.POST['password2']:
            password=request.POST['password']
        
            try:
                user=userOn.objects.get(email=email)
                
                user.delete()
                user=User.objects.create( nick_name=nick_name,password=password,email=email,tgUserName=tg,phoneNumber=phone)
                user.save()
                return render(request,'App1/userhome.html',{'user':user})
            except:
                try:
                    User.objects.get(email=email)

                    return render(request,'App1/signin.html',{'usere':True})
                except:
                    return render(request,'App1/signin.html',{'userd':True})
        else:
            return render(request,'App1/signin.html',{'notm':True})

        
        
    else:
        return render(request,'App1/signin.html',{})


def update(request):
    increment=int(request.GET['append_increment'])
    user=User.objects.GET(id=int(request.POST['user']))
    increment_to=increment+10
    allmass=Massage.objects.filter(topic=topics).order_by('-id')[increment:increment_to]
    return render(request,'App1/update.html',{'allmass':allmass,'user':user})


