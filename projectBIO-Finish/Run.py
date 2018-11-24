import gi;gi.require_version('Gtk','3.0');from gi.repository import Gtk as gtk, GdkPixbuf, Gdk
from MenuBar import*


win = MenuB()
win.connect("destroy", gtk.main_quit)
win.show_all()
gtk.main()