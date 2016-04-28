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

def do(user,message):
	if isweather(message.lower()):
		return weather(user)
	elif isnews(message.lower()):
		return news(user)
	elif isnote(message.lower()):
		return(note(user,message))
	else:
		return(idontknown(user))

