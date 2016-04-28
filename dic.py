import shelve
import base

db = shelve.open("userdo.db")

def isweather(message):
	if message.find("weather")!=-1:
		return (true)
	else:
		return (false)

def isnews(message):
	if message.find("news")!=-1:
		return(true)
	elif message.find("newspaper")!=-1:
		return(true)
	else:
		return(false)

def isnote(message):
	s=message.split(" ",1)
	if s=="note":
		return(true)
	elif s=="remind":
		return(true)
	elif s=="write:":
		return(true)
	else:
		return(false)

def idontknown(user):
	return("I cant't help you")

def isstart(message):
        if message=="/start":
                return(true)
        else:
                return(false)

def start(user):
        db[user+'_do']='scity'
        return("Привет! Введи свой город на английском. Hi! Enter your city in English")

def do(user,message):
	if isweather(message.lower()):
		return weather(user)
	elif isnews(message.lower()):
		return news(user)
	elif isnote(message.lower()):
		return(note(user,message))
	elif isstart(message):
                return(start(user))
	else:
		return(idontknown(user))

def setlang(user,lang):
        if lang=='en':
                setuserlang(user,'en')
                db[user+'_do']='none'
                return("Ok.")
        elif lang=='ru':
                setuserlang(user,'ru')
                db[user+'_do']='none'
                return("Ok.")
        else:
                return("Available language ru or en")

def setcity(user,city):
       setusercity(user,city)
       return("Ok.")
                
                
def onmessage(user,message):
        if db[user+'_do']=='slang':
                return(setlang(user,message.lower()))
        elif db[user+'_do']=='scity':
                db[user+'_do']='slang'
                return(setcity(user,message.lower())+" Теперь выбери язык: ru или en.Now choose your language: ru or en.")
        elif db[user+'_do']=='lang':
                return(setlang(user,message.lower()))
        elif db[user+'_do']=='city':
                return(setcity(user,message.lower()))
        else:
                return(do(user,message))
        

db.close;
                
