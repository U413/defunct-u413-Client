# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"u413", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		user_area = wx.BoxSizer( wx.VERTICAL )
		
		self.display = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.NO_BORDER )
		self.display.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 76, 90, 90, False, "Courier New" ) )
		self.display.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.display.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		user_area.Add( self.display, 1, wx.ALL|wx.EXPAND, 5 )
		
		cmdline_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pointer = wx.StaticText( self.main_panel, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pointer.Wrap( -1 )
		self.pointer.SetFont( wx.Font( 11, 76, 90, 90, False, "Courier New" ) )
		self.pointer.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.pointer.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		cmdline_sizer.Add( self.pointer, 0, wx.ALL, 5 )
		
		self.cmdline = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,15 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_WORDWRAP|wx.NO_BORDER )
		self.cmdline.SetFont( wx.Font( 11, 76, 90, 90, False, "Courier New" ) )
		self.cmdline.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.cmdline.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		cmdline_sizer.Add( self.cmdline, 1, wx.ALL|wx.EXPAND, 5 )
		
		user_area.Add( cmdline_sizer, 0, wx.EXPAND|wx.TOP, 5 )
		
		self.main_panel.SetSizer( user_area )
		self.main_panel.Layout()
		user_area.Fit( self.main_panel )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"derp", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.AppendItem( self.m_menuItem1 )
		
		self.m_menu1.AppendSubMenu( self.m_menu11, u"blabla" )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"darp", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.main_panel.Bind( wx.EVT_RIGHT_DOWN, self.main_panelOnContextMenu ) 
		
		main_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( main_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.exit() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def exit( self, event ):
		event.Skip()
	
	def main_panelOnContextMenu( self, event ):
		self.main_panel.PopupMenu( self.m_menu1, event.GetPosition() )
		
app=wx.App()
win=MyFrame1()
app.MainLoop()
