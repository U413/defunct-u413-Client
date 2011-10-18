import urllib2

url="http://api.u413.com/"
null=None
true=True
false=False

class u413:
	def __init__(self):
		self.o=urllib2.build_opener(urllib2.HTTPCookieProcessor())
		self.sessionid=self.get_data()["SessionId"]

	def send_command(self,command):
		req=urllib2.Request(url+"(S(%s))/"%self.sessionid,
			headers={
				"Content-Type":"application/json",
				"Accept":"*/*",
				"User-Agent":"PiMaster.u413_UI"},
			data=
				'{"cli":%s}'%command)
		return eval(self.o.open(req).read())

	def get_data(self):
		if "sessionid" in dir(self):
			return eval(self.o.open(urllib2.Request(url+"(S(%s))/"%self.sessionid)).read())
		return eval(self.o.open(urllib2.Request(url)).read())
	
	#shortcuts
	
	def get_title(self):
		return self.get_data()["TerminalTitle"]