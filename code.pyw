# -*- coding: utf-8 -*-

import wx
import urllib2

o=urllib2.build_opener(urllib2.HTTPCookieProcessor())
url="http://api.u413.com/"
null=None
true=True
false=False

metadata=eval(o.open(urllib2.Request(url+"metadata")).read())["DisplayItems"][0]

def send_command(command):
	req=urllib2.Request(url,
		headers={
			"Content-Type":"application/json",
			"Accept":"*/*",
			"User-Agent":"PiMaster.u413_UI"},
		data={
			'{"cli":%s}'%command})
	return o.open(req).read()

def get_u413():
	return eval(o.open(urllib2.Request(url)).read())

class window(wx.Frame):
	def __init__(self):
		data=get_u413()
		wx.Frame.__init__(self,None,-1,title=data["TerminalTitle"])
		self.SetSizeHintsSz(wx.DefaultSize,wx.DefaultSize)
		main_sizer=wx.BoxSizer(wx.VERTICAL)
		self.SetBackgroundColour(wx.Colour(0,0,0))
		self.main_panel=wx.Panel(self,wx.ID_ANY,wx.DefaultPosition,wx.DefaultSize,wx.TAB_TRAVERSAL)
		self.main_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		user_area=wx.BoxSizer(wx.VERTICAL)
		self.display=wx.TextCtrl(self.main_panel,wx.ID_ANY,wx.EmptyString,wx.DefaultPosition,wx.DefaultSize,wx.TE_MULTILINE|wx.TE_READONLY|wx.NO_BORDER)
		self.display.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(),76,90,90,False,"Courier New"))
		self.display.SetForegroundColour(wx.Colour(0,255,0))
		self.display.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		user_area.Add(self.display,1,wx.ALL|wx.EXPAND,5)
		cmdline_sizer=wx.BoxSizer(wx.HORIZONTAL)
		self.pointer=wx.StaticText(self.main_panel,wx.ID_ANY,u">",wx.DefaultPosition,wx.DefaultSize,0)
		self.pointer.Wrap(-1)
		self.pointer.SetFont(wx.Font(11,76,90,90,False,"Courier New"))
		self.pointer.SetForegroundColour(wx.Colour(0,255,0))
		self.pointer.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		cmdline_sizer.Add(self.pointer,0,wx.ALL,5)
		self.cmdline=wx.TextCtrl(self.main_panel,wx.ID_ANY,wx.EmptyString,wx.DefaultPosition,wx.Size(-1,15),wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_WORDWRAP|wx.NO_BORDER)
		self.cmdline.SetFont(wx.Font(11,76,90,90,False,"Courier New"))
		self.cmdline.SetForegroundColour(wx.Colour(0,255,0))
		self.cmdline.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		cmdline_sizer.Add(self.cmdline,1,wx.ALL|wx.EXPAND,5)
		user_area.Add(cmdline_sizer,0,wx.EXPAND|wx.TOP,5)
		self.main_panel.SetSizer(user_area)
		self.main_panel.Layout()
		user_area.Fit(self.main_panel)
		main_sizer.Add(self.main_panel,1,wx.EXPAND|wx.ALL,5)
		self.SetSizer(main_sizer)
		self.Layout()
		self.Centre(wx.BOTH)
	
	def __del__(self):
		pass
		
if __name__=="__main__":
	app=wx.App(False)
	frame=window()
	frame.Show()
	app.MainLoop()
