import urllib2

url="http://api.u413.com/"
null=None
true=True
false=False

class u413:
	def __init__(self):
		o=urllib2.build_opener(urllib2.HTTPCookieProcessor())

	def send_command(command):
		req=urllib2.Request(url,
			headers={
				"Content-Type":"application/json",
				"Accept":"*/*",
				"User-Agent":"PiMaster.u413_UI"},
			data={
				'{"cli":%s}'%command})
		return eval(o.open(req).read())

	def get_u413():
		return eval(o.open(urllib2.Request(url)).read())