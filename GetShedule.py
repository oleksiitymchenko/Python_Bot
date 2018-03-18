import datetime

import requests


def GetWeekNumber():
    url = "http://api.rozklad.org.ua/v2/weeks"
    responce = requests.get(url)
    return responce.json()['data']

def GetDayShedule(group,week=GetWeekNumber(),day = datetime.date.isoweekday(datetime.date.today())):
    if day == 7 : raise Exception("Day cannot be sunday")
    if week>2 or week<1 :raise Exception("week must be 1 or 2")

    url="https://api.rozklad.org.ua/v2/groups/{}/lessons".format(group)
    response = requests.get(url).json()

    if not response['message']=="Ok": raise Exception("group is not existing")
    response = response['data']
    list =[]
    for x in response:
        if not day==0:
            if x['day_number']==str(day) and x['lesson_week']==str(week):
             list.append(x)
        elif x['lesson_week']==str(week):
            list.append(x)
    return list

def GetWeekShedule(group,week=GetWeekNumber()):
    return GetDayShedule(group,week,0)

def dayShedule(day):
    sheduleList = GetDayShedule("іт-61",day=day)
    mes=""
    for x in sheduleList:
        mes+=x['lesson_number']+'. '+x['lesson_name']+' '+x['lesson_room'] +'\n'
    mes = sheduleList[0]['day_name'] +'\n'+mes
    return mes