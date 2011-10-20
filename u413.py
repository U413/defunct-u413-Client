import urllib
import urllib2
import json

url="http://api.u413.com/"
null=None
true=True
false=False

class u413:
	def __init__(self):
		self.o=urllib2.build_opener(urllib2.HTTPCookieProcessor())
		data=self.get_data()
		self.sessionid=data["SessionId"]
		self.context=data["ContextText"]
		self.title=data["TerminalTitle"]

	def send_command(self,command):
		req=urllib2.Request(url+"(S(%s))/"%self.sessionid,
			headers={
				"Content-Type":"application/json",
				"Accept":"*/*",
				"User-Agent":"PiMaster.u413_UI"},
			data='{"cli":"%s"}'%command)
		data=json.loads(self.o.open(req).read())
		self.title=data["TerminalTitle"]
		self.context=data["ContextText"]
		if data["Exit"]:
			exit()
		return data

	def get_data(self):
		if "sessionid" in dir(self):
			return json.loads(self.o.open(urllib2.Request(url+"(S(%s))/"%self.sessionid)).read())
		return json.loads(self.o.open(urllib2.Request(url)).read())
	
	def print_u413(self,data):
		for p in data["DisplayItems"]:
			if p["Text"]!=None:
				print p["Text"]