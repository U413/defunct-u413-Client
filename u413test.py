import u413
import sys

u=u413.u413()
s=""
while s.upper()!="EXIT":
	print u.print_u413(u.send_command(raw_input(u.context+"> ")))