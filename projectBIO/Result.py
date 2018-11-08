import gi;gi.require_version('Gtk','3.0');from gi.repository import Gtk as gtk, GdkPixbuf, Gdk
from MenuBar import *
from Insetos import *

def Sol(self):
	self.Soly = gtk.Window()
	self.grid_result = gtk.Grid(column_spacing=6, row_spacing=6)
	self.Soly.add(self.grid_result)
	self.Button = []
		
	for c in range(len(self.label)):
		self.Button.append(gtk.Button())
#-----------------------------------------------------------------------------------------------------	
	#Image0
	self.image0 = gtk.Image()
	pixbuf0 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto0.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image0.set_from_pixbuf(pixbuf0)
	
	#Image1
	self.image1 = gtk.Image()
	pixbuf1 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto1.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image1.set_from_pixbuf(pixbuf1)

	#image2
	self.image2= gtk.Image()
	pixbuf2 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto2.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image2.set_from_pixbuf(pixbuf2)
	
	#image3
	self.image3= gtk.Image()
	pixbuf3 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto3.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image3.set_from_pixbuf(pixbuf3)

	#image4
	self.image4= gtk.Image()
	pixbuf4 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto4.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image4.set_from_pixbuf(pixbuf4)

	#image5
	self.image5= gtk.Image()
	pixbuf5 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto5.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image5.set_from_pixbuf(pixbuf5)
#----------------------------------------------------------------------------------------------------------------------
	#Button0
	self.Button[0].add(self.image0)
	self.Button[0].set_size_request(100,100)
	self.Button[0].connect('clicked', lambda arg: Inseto0(self))
	#----------------------------------------
	#Button1
	self.Button[1].add(self.image1)
	self.Button[1].set_size_request(100,100)
	self.Button[1].connect('clicked', lambda arg: Inseto1(self))
	#----------------------------------------
	#Button2
	self.Button[2].add(self.image2)
	self.Button[2].set_size_request(100,100)
	self.Button[2].connect('clicked', lambda arg: Inseto2(self))
	#----------------------------------------

	#Button3
	self.Button[3].add(self.image3)
	self.Button[3].set_size_request(100,100)
	self.Button[3].connect('clicked', lambda arg: Inseto3(self))
	#----------------------------------------

	#Button4
	self.Button[4].add(self.image4)
	self.Button[4].set_size_request(100,100)
	self.Button[4].connect('clicked', lambda arg: Inseto4(self))
	#----------------------------------------

	#Button5
	self.Button[5].add(self.image5)
	self.Button[5].set_size_request(100,100)
	self.Button[5].connect('clicked', lambda arg: Inseto5(self))
	#----------------------------------------	
	return 0
		

