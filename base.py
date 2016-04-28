import shelve
db = shelve.open("base.db")

def readlang(user):
    if db[user+'_lang']=='ru':
        return('ru')
    else:
        return('en')

def readcity(user):
    return (db[user+'_city'])

def setuserlang(user,lang):
    db[user+'_lang']=lang

def setusercity(user,city):
    db[user+'_city']=city

db.close
