# -*- coding: utf-8 -*-
import shelve
from base import *
from weather import *
tdb = shelve.open("userdo.db")

def isweather(message):
	if message.find("weather")!=-1:
		return (1)
	else:
		return (0)

def isnews(message):
	if message.find("news")!=-1:
		return(1)
	elif message.find("newspaper")!=-1:
		return(1)
	else:
		return(0)

def isnote(message):
	s=message.split(" ",1)
	if s=="note":
		return(1)
	elif s=="remind":
		return(1)
	elif s=="write:":
		return(1)
	else:
		return(0)

def idontknown(user):
	return("I cant't help you")

def isstart(message):
        if message=="/start":
                return(1)
        else:
                return(0)

def start(user):
	setuserlang(user,'en')
	setusercity(user,'moscow')
        tdb[user+'_do']='scity'
        return("Привет! Введи свой город на английском. Hi! Enter your city in English")

def do(user,message):
	if isweather(message.lower()):
		return weather(readcity(user),readlang(user))
	elif isnews(message.lower()):
		return news(user)
	elif isnote(message.lower()):
		return(note(user,message))
	else:
		return(idontknown(user))

def setlang(user,lang):
        if lang=='en':
                setuserlang(user,'en')
                tdb[user+'_do']='none'
                return("Ok.")
        elif lang=='ru':
                setuserlang(user,'ru')
                tdb[user+'_do']='none'
                return("Ok.")
        else:
                return("Available language ru or en")

def setcity(user,city):
       setusercity(user,city)
       return("Ok.")
                
                
def onmessage(user,message):
	if isstart(message):
		return(start(user))
	elif tdb[user+'_do']=='scity':
                tdb[user+'_do']='slang'
                return(setcity(user,message.lower())+" Теперь выбери язык: ru или en.Now choose your language: ru or en.")
        elif tdb[user+'_do']=='slang':
                return(setlang(user,message.lower()))
        elif tdb[user+'_do']=='lang':
                return(setlang(user,message.lower()))
        elif tdb[user+'_do']=='city':
                return(setcity(user,message.lower()))
        else:
		print (tdb[user+'_do'])
		print (readcity(user))
		print (readlang(user))
                return(do(user,message))
        

tdb.close;
                
