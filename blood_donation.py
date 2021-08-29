# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:43:09 2021

@author: Shaunak Maduskar
"""
banks={}
details={}
samples={}
rare=['O-','A-','B-','AB+','AB-']
'''banks={uid:{'name':"Brent hospital",'area':"Highland Park",'blood_grps':['A+','O-','B+'],'demand':False,'notif':0,'data':samples}}'''
'''details={idnum:{'name':"Amy Smith",'area':"Hoboken",'blood_grp':'A+','demand':False,'notif':0}}'''
class Admin(object) :
    def __init__(self,name,idnum,area,blood_grp,demand,notif):
        self.name=name
        self.idnum=idnum
        self.area=area
        self.blood_grp=blood_grp
        self.demand=demand
        self.notif=notif
    def __getInfo(self) :
        a=input("enter deired area")
        for i in details.keys() :
            if details[i]['area'] == a :
                return details[i] 
            else:
                print('No registered donors in area')
    def __addTosystem(self):
        uid=input('enter form number to be stored as id')
        hos_name=input('enter hospital/blood bank/camp name')
        ar=input("enter area")
        bl=input("enter available blood types").split(',')
        banks[uid]={'name':hos_name,'area':ar,'blood_grps':bl,'demand':False,'notif':0,'data':{}}
        return banks
    
    def __bloodRequest(self) :
        for i in details.keys() :
            if details[i]['demand']==True :
                for j in details.keys() :
                    if details[j]['blood_grp']==details[i]['blood_grp'] and i != j :
                        details[j]['notif']+=1
class User(Admin) :
    def __init__(self):
        Admin.__init__(self) 
    def recipient(self) :
        u=input('press 2 to request blood')
        if u==2:
            self.demand=True
        else:
            self.demand=False
        details[self.idnum]['demand']=self.demand
        
    def donor(self) :
        n=input("Press 1 to accept request from notifications")
        if n==1:
            for i in details.keys() :
                if i == self.idnum :
                    details[i]['notif']-=1
                    print('changes made to notifications will be informed to admin')
                    print('visit your nearest blood bank/hospital for donation')


def rareBloodBanks(banks):
    impBanksDict={}
    for i in banks.keys():
        for j in banks[i]['blood_grps'] :
            if banks[i]['blood_grps'][j] in rare :
                impBanksDict[i]={{'name':banks[i]['name'],'area':banks[i]['area'],'blood_grps':banks[i]['blood_grps']}}
    return impBanksDict

def collectSamplesData(banks,hos_name,ar,bl,demand,notif):
    na=input('enter name of donor')
    b=input('enter blood group of donor')
    if b not in bl :
        bl.append(b)
    d=input('enter latest date of donation')
    samples[na]={'bld_grp':b,'latest date':d}
    ui=input('enter unique id of blood bank/hospital')
    banks[ui]={'name':hos_name,'area':ar,'blood_grps':bl,'demand':demand,'notif':notif,'data':samples}
    print(banks[ui]['data'][na])
    return banks

def searchData(banks):
    bld=input('enter desired blood group')
    print('enter 1 to search by branch')
    print('enter 2 to search by date')
    num=input()
    searchResults=[]
    if num == 1 :
        ar=input('enter branch area')
        for i in banks.keys() :
             if banks[i]['area']==ar and bld in banks[i]['blood_grps'] :
                 searchResults.append(banks[i])
        return searchResults
    elif num==2:
        da=input('enter required date')
        for i in banks.keys():
            if da in banks[i]['data'].values() and bld in banks[i]['blood_grps'] :
                searchResults.append(banks[i])
        return searchResults