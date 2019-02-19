from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.files.base import ContentFile
from .models import Image,User,Count,Order
import datetime
import requests as re
# Create your views here.
def formateTime(datatime):
    return '-'.join([x for x in map(lambda x:str(x),
                                        [datatime.year,datatime.month,datatime.day])])

def receiveImage(request):
    image_content = ContentFile(request.FILES['file'].read())
    no = request.POST.get('no')
    img = Image(order=Order.objects.get(no=no),no=no,image=request.FILES['file'])
    img.save()
    print(request.POST,request.FILES)
    return JsonResponse({'status':'success'})

def login(request):
    if request.method == 'POST':
        api = 'https://api.weixin.qq.com/sns/jscode2session'
        payload = {
            'appid':'wxd998f218b30a447f',
            'secret':'bb3e0b02a97c0f522fdd4ad5163af254',
            'js_code':request.POST.get('code'),
            'grant_type':'authorization_code'
            }
        res=re.get(api,params=payload,verify=False,timeout=3).json()
        try:
            user_=User.objects.get(openid=res['openid'])
            address = user_.address.split('\n')
            return JsonResponse({'openid':res['openid'],
                        'user':True,                                #是否注册
                        'name':user_.name,
                        'address':address,
                        'tel':user_.tel,
                        'isRepairGuy':user_.isRepairGuy},safe=False)
        except:
            return JsonResponse({'openid':res['openid'],'user':False},safe=False)
    else :
        return JsonResponse({'status':'failure'})

def enroll(request):
    if request.method == 'POST':
        openid=request.POST.get('openid')
        try:
            User.objects.get(openid=openid)
            return JsonResponse({'status':'已注册'})
        except:
            name = request.POST.get('name')
            tel = request.POST.get('tel')
            address = request.POST.get('address').split('\n')
            User(openid=openid,name=name,tel=tel,address='\n'.join(address)).save()
            return JsonResponse({'status':'success'})

def userAlter(request):
    if request.method == 'POST':
        user = User.objects.get(openid = request.POST.get('openid'))
        user.openid=request.POST.get('openid')
        user.name = request.POST.get('name')
        user.tel = request.POST.get('tel')
        user.address = '\n'.join(request.POST.get('address').split(','))
        user.save()
        return JsonResponse({'status':'success'})

def newOrder(request):
    if request.method == 'POST':
        c= Count.objects.get(name='order')
        c.count += 1
        count = str(c.count)
        no = "0"*(7-len(count))+count
        Order(
            no = no,
            user = User.objects.get(openid = request.POST.get('openid')),
            typ = request.POST.get('typ'),
            cfa = request.POST.get('cfa'),
            faultDes = request.POST.get('faultDes'),
            address = request.POST.get('address')
        ).save()
        c.save()
        return JsonResponse({'status':'success','no':no},safe=False)

    else:
        return JsonResponse({'status':'faulture'})

def orders(request):
    if request.method == 'POST':
        isRepairGuy = request.POST.get('isRepairGuy')
        if isRepairGuy==True:
            orders = Order.objects.filter(isAnnul=1).order_by('-rpTime')
            try:
                if len(orders)-(index*count)>0:
                    orders = orders[index*count:(index+1)*count]
                else:
                    orders = orders[index*count:]
                res = [{'no':order.no,
                'name':user.name,
                'rpTime':formateTime(order.rpTime),
                'faultDes':order.faultDes,
                'isReceive':order.isReceive,
                'isComplete':order.isComplete,
                'isCheck':order.isCheck,
                'image':'media/'+order.image_set.all()[0].image.url,
                'address':order.address,
                'status':order.status} 
                for order in orders]
                return JsonResponse(res,safe=False)
            except:
                return JsonResponse({'status':'success'})
            return JsonResponse({'status':'RepairGuy'})
        else:
            openid=request.POST.get('openid')
            user = User.objects.get(openid=openid)
            count = int(request.POST.get('count'))
            index = int(request.POST.get('index'))
            orders = user.order_set.filter(isAnnul=1).order_by('-rpTime')
            try:
                if len(orders)-(index*count)>0:
                    orders = orders[index*count:(index+1)*count]
                else:
                    orders = orders[index*count:]
                res = [{'no':order.no,
                'name':user.name,
                'rpTime':formateTime(order.rpTime),
                'faultDes':order.faultDes,
                'isReceive':order.isReceive,
                'isComplete':order.isComplete,
                'isCheck':order.isCheck,
                'image':'media/'+order.image_set.all()[0].image.url,
                'address':order.address,
                'status':order.status} 
                for order in orders]
                return JsonResponse(res,safe=False)
            except:
                return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'POST please'})

'''   
def orders2(request):
    if request.method == 'POST':
        no=request.POST.get('no')
        order = Order.objects.get(no=no)
        res = {
            'no':order.no,
            'rpTime':formateTime(order.rpTime),
            'status':'',
            'address':order.address,
            'image':'media/'+order.image_set.all()[0].image.url
        }
        return JsonResponse(res)
    else:
        return JsonResponse({'status':'faulture'})
'''

def order(request,no):
    if request.method == 'POST':
        order = Order.objects.get(no=no)
        user = order.user
        res = {
            'no':no,
            'name':user.name,
            'address':order.address,
            'tel':user.tel,
            'rpTime':formateTime(order.rpTime),
            'faultDes':order.faultDes,
            'images':['media/'+img.image.url for img in order.image_set.all()],
            'typ':order.typ,
            'cfa':order.cfa,
            'faultCon':order.faultCon,
            'costList':order.costList.split('\n'),
            'status':order.status,
            'isReceive':order.isReceive,
            'isComplete':order.isComplete,
            'isCheck':order.isCheck
        }
        if order.isReceive:
            res['receiveTime'] = formateTime(order.receiveTime)
            if(order.isComplete):
                res['completeTime'] = formateTime(order.completeTime)
                if(order.isCheck):
                    res['checkTime'] = formateTime(order.checkTime)
        return JsonResponse(res,safe=False)
    else:
        return JsonResponse({'status':'POST'})

def annul(request):
    if request.method == 'POST':
        order = Order.objects.get(no=request.POST.get('no'))
        order.isAnnul = 0
        if order.isReceive:
            return  JsonResponse({'status':False})
        else:
            order.annulUserOpenid = request.POST.get('openid')
            order.save()
            return JsonResponse({'status':True})
    else:
        return JsonResponse({'status':'POST'})

def repair(request):
    order = Order.objects.get(no=request.POST.get('no'))
    if User.objects.get(openid=request.POST.get('openid')).isRepairGuy:
        if order.isReceive:
            res = {
                'isReceive':order.isReceive,
                'isComplete':order.isComplete,
                'repairGuy':User.objects.get(openid=order.repairGuy).name,
                'faultCon':order.faultCon,
                'status':order.status,
                'costList':order.costList.split('\n')
            }
        else:
            res = {
                'isReceive':order.isReceive,
                'isComplete':order.isComplete,
                'repairGuy':'无',
                'faultCon':order.faultCon,
                'status':order.status,
                'costList':[]
            }
        return JsonResponse(res)
    else:
        return JsonResponse({'status':'noPower'})

def receive(request):
    if request.method == 'POST':
        user = User.objects.get(openid=request.POST.get('openid'))
        if user.isRepairGuy:
            order = Order.objects.get(no=request.POST.get('no'))
            order.repairGuy = user.openid
            order.isReceive = True
            order.receiveTime = datetime.datetime.now()
            order.status = '维修中'
            order.save()
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'isNotRepairGuy'})
    else:
        return JsonResponse({'status':'POST'})

def complete(request):
    if request.method == 'POST':
        user = User.objects.get(openid = request.POST.get('openid'))
        if user.isRepairGuy:
            order = Order.objects.get(no=request.POST.get('no'))
            if(order.isReceive):
                order.isComplete = True
                order.completeTime = datetime.datetime.now()
                order.status = '已完修'
                order.save()
                return JsonResponse({'status':'success'})
            else:
                return JsonResponse({'status':'isNotReceive'})
        else:
            return JsonResponse({'status':'noPower'})
    else:
        return JsonResponse({'status':'POST'})

def repairInfo(request):
    if request.method == 'POST':
        user = User.objects.get(openid=request.POST.get('openid'))
        if user.isRepairGuy:
            order = Order.objects.get(no=request.POST.get('no'))
            if order.isReceive and (not order.isComplete):
                order.faultCon = request.POST.get('faultCon')
                order.costList = '\n'.join(request.POST.get('costList').split(','))
                order.save()
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'noPower'})
    else:
        return JsonResponse({'status':'POST'})

def check(request):
    if request.method == 'POST':
        user = User.objects.get(openid=request.POST.get('openid'))
        order = Order.objects.get(no=request.POST.get('no'))
        if user == order.user:
            if order.isComplete:
                order.isCheck = True
                order.status = '已验收'
                order.save()
                return JsonResponse({'status':'success'})
            else:
                return JsonResponse({'status':'isNotComplete'})
        else:
            return JsonResponse({'status':'noPower'})
    else:
        return JsonResponse({'status':'POST'})