from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length=50)
    name = models.CharField(max_length=6)                   #用户姓名
    address = models.TextField()                            #用户地址
    tel = models.CharField(max_length=15)                   #用户电话
    isRepairGuy = models.BooleanField(default=False)        #维修员权限标记


class Order(models.Model):
    no = models.CharField(max_length=7)                     #订单编号
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    typ = models.CharField(max_length=40)                   #机器型号
    cfa = models.CharField(max_length=20,blank=True)        #资产编号
    address = models.CharField(max_length=50)
    rpTime = models.DateTimeField(auto_now_add=True)        #报修时间
    faultDes = models.TextField()                           #故障描述
    faultCon = models.TextField(blank=True)                 #故障内容
    costList = models.TextField(blank=True)                 #费用明细   
    repairGuy = models.CharField(max_length=50,blank=True)   #维修技术员,标记为维修员openid
    isComplete = models.BooleanField(default=False)
    completeTime = models.DateTimeField('完修时间',default = timezone.now)         #完修时间
    isCheck = models.BooleanField(default=False)            #是否验收
    checkTime = models.DateTimeField('验收时间',default = timezone.now)           #验收时间
    isReceive = models.BooleanField(default=False)          #是否接单
    receiveTime = models.DateTimeField('接单时间',default = timezone.now)
    isAnnul = models.IntegerField(default=1)           #是否撤销
    annulUserOpenid = models.CharField(max_length=50,default='')    #撤销操作员
    status = models.CharField(max_length=4,default='处理中')
'''
                    status 的定义：
                        ChildField 
                        0:处理中
                        1:维修中
                        2:已完修
                        3:已验收
'''

def get_photo_path(isinstance,filename):
    productionName = isinstance.no
    print(productionName,"",filename)
    return 'images/%s/%s'%(productionName,filename)

class Image(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    no = models.CharField(max_length=7,default='')
    image = models.ImageField(upload_to=get_photo_path)

class Count(models.Model):
    name = models.CharField(max_length=10)
    count = models.IntegerField(default=0)