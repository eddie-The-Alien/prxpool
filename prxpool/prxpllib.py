import requests
import random

##gtprxlst gets proy list from github im useing 
##rx443 just use the raw url and if its a simple 
##txt file  itll be good anything else and ya 
##gonna have something to do this is basicly the lib for prxypool so
##  im just gonna put it out as a packge but feel
## free to use any of the functions credit me if 
##you use a good portion
def getprxlst():
	http_url="https://raw.githubusercontent.com/rx443/proxy-list/main/online/http.txt"
	https_url="https://raw.githubusercontent.com/rx443/proxy-list/main/online/https.txt"
	httplst=[]
	httpslst=[]
	http_raw=requests.get(http_url)
	http=http_raw.text
	for h in http.split("\n"):
		httplst.append("http://"+h)
	https_raw=requests.get(https_url)
	https=https_raw.text
	for h in https.split("\n"):
		httpslst.append("https://"+h)
	prxpl={"http":httplst,"https":httpslst}
	print("proxpool setup http and https")
	return  prxpl
##swtchpl starts the rotation removes used prxies
## as it gose
def swtchpl(prxpl):
	nttp=.choice(prxpl["http"])
	nttps=random.choice(prxpl["https"]
	prxpl["http"].remove(nttp)
	prxpl["https"].remove(nttps)
	cp:{"http":nttp,
	"https":nttps
	}
	prxpl.update(cp)
	return prxpl

