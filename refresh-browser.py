import pygtk
pygtk.require('2.0')
import gtk
import wnck
import re
import sys
import time
from subprocess import Popen, PIPE

# http://stackoverflow.com/questions/17776978/python-wnck-set-focus-to-window
screen = wnck.screen_get_default()
while gtk.events_pending():
    gtk.main_iteration()

titlePattern = re.compile('.*Chromium.*')

windows = screen.get_windows()
for w in windows:
  if titlePattern.match(w.get_name()):
    print w.get_name()
    w.activate(0)

# http://danielj.se/2011/06/29/control-keystrokes-and-mouse-from-the-command-line-with-xautomation/
"""Send key to system"""
# control_f4_sequence = '''keydown Control_L
# key F4
# keyup Control_L
# '''

# shift_a_sequence = '''keydown Shift_L
# key A
# keyup Shift_L
# '''

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

# keypress(shift_a_sequence)
# keypress(control_f4_sequence)
key_refresh = '''key F5
'''

keypress(key_refresh)
