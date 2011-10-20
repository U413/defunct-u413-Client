# -*- coding: utf-8 -*-

import wx
import u413

class window(wx.Frame):
	def __init__(self):
		self.u413=u413.u413()
		wx.Frame.__init__(self,None,-1,title=self.u413.data["TerminalTitle"])
		self.SetSizeHintsSz(wx.DefaultSize,wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour(0,0,0))
		main_sizer=wx.BoxSizer(wx.VERTICAL)
		self.main_panel=wx.Panel(self,wx.ID_ANY,wx.DefaultPosition,wx.DefaultSize,wx.TAB_TRAVERSAL)
		self.main_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		user_area=wx.BoxSizer(wx.VERTICAL)
		self.display=wx.TextCtrl(self.main_panel,wx.ID_ANY,wx.EmptyString,wx.DefaultPosition,wx.DefaultSize,wx.TE_MULTILINE|wx.TE_READONLY|wx.NO_BORDER)
		self.display.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(),76,90,90,False,"Courier New"))
		self.display.SetForegroundColour(wx.Colour(0,255,0))
		self.display.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		user_area.Add(self.display,1,wx.ALL|wx.EXPAND,5)
		cmdline_sizer=wx.BoxSizer(wx.HORIZONTAL)
		self.context=wx.StaticText(self.main_panel,wx.ID_ANY,u">",wx.DefaultPosition,wx.DefaultSize,0)
		self.context.Wrap(-1)
		self.context.SetFont(wx.Font(11,76,90,90,False,"Courier New"))
		self.context.SetForegroundColour(wx.Colour(0,255,0))
		self.context.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		cmdline_sizer.Add(self.context,0,wx.ALL,5)
		self.cmdline=wx.TextCtrl(self.main_panel,wx.ID_ANY,wx.EmptyString,wx.DefaultPosition,wx.Size(-1,15),wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_WORDWRAP|wx.NO_BORDER|wx.TE_PROCESS_ENTER)
		self.cmdline.SetFont(wx.Font(11,76,90,90,False,"Courier New"))
		self.cmdline.SetForegroundColour(wx.Colour(0,255,0))
		self.cmdline.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self.cmdline.Bind(wx.EVT_KEY_UP,self.OnKeyPress)
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
	
	def OnKeyPress(self,event):
		if event.GetKeyCode()==wx.WXK_RETURN:
			self.u413.send_command(self.cmdline.GetValue())
			self.cmdline.SetValue("")
			text=""
			if self.u413.data["ClearScreen"]:
				self.display.SetLabel("")
			else:
				#without this the sections aren't separated properly
				text='\n'
			for p in self.u413.data["DisplayItems"]:
				text+=p["Text"]+'\r\n'
			self.display.SetLabel(self.display.GetLabel()+text)
			self.SetTitle(self.u413.title)
			self.context.SetLabel(self.u413.data["ContextText"]+'> ')
		
if __name__=="__main__":
	app=wx.App(False)
	frame=window()
	frame.Show()
	app.MainLoop()
