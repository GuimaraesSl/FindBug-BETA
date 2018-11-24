import gi;gi.require_version('Gtk','3.0');from gi.repository import Gtk as gtk, GdkPixbuf, Gdk
from MenuBar import *
from Insetos import *

def Sol(self):
	self.Soly = gtk.Window()
	self.grid_result = gtk.Grid(column_spacing=6, row_spacing=6)
	self.Button = []

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	scrolled.add(self.grid_result)
	self.Soly.add(scrolled)
	self.Soly.set_default_size(1000, 1000)
		
	for c in range(len(self.label)):
		self.Button.append(gtk.Button())
	
	#Image0
	self.image0 = gtk.Image()
	pixbuf0 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto0.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image0.set_from_pixbuf(pixbuf0)
	
	#Image1
	self.image1 = gtk.Image()
	pixbuf1 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto1.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image1.set_from_pixbuf(pixbuf1)

	#image2
	self.image2= gtk.Image()
	pixbuf2 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto2.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image2.set_from_pixbuf(pixbuf2)
	
	#image3
	self.image3= gtk.Image()
	pixbuf3 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto3.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image3.set_from_pixbuf(pixbuf3)

	#image4
	self.image4= gtk.Image()
	pixbuf4 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto4.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image4.set_from_pixbuf(pixbuf4)

	#image5
	self.image5= gtk.Image()
	pixbuf5 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto5.jpeg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image5.set_from_pixbuf(pixbuf5)

	#image6
	self.image6= gtk.Image()
	pixbuf6 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto6.png', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image6.set_from_pixbuf(pixbuf6)

	#image7
	self.image7= gtk.Image()
	pixbuf7 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto7.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image7.set_from_pixbuf(pixbuf7)

	#image8
	self.image8= gtk.Image()
	pixbuf8 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto8.png', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image8.set_from_pixbuf(pixbuf8)

	#image9
	self.image9= gtk.Image()
	pixbuf9 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto9.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image9.set_from_pixbuf(pixbuf9)

	#image10
	self.image10= gtk.Image()
	pixbuf10 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto10.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image10.set_from_pixbuf(pixbuf10)

	#image11
	self.image11= gtk.Image()
	pixbuf11 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto11.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image11.set_from_pixbuf(pixbuf11)

	#image12
	self.image12= gtk.Image()
	pixbuf12 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto12.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image12.set_from_pixbuf(pixbuf12)

	#image13
	self.image13= gtk.Image()
	pixbuf13 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto13.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image13.set_from_pixbuf(pixbuf13)

	#image14
	self.image14= gtk.Image()
	pixbuf14 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto14.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image14.set_from_pixbuf(pixbuf14)

	#image15
	self.image15= gtk.Image()
	pixbuf15 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto15.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image15.set_from_pixbuf(pixbuf15)

	#image16
	self.image16= gtk.Image()
	pixbuf16 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto16.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image16.set_from_pixbuf(pixbuf16)

	#image17
	self.image17= gtk.Image()
	pixbuf17 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto17.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image17.set_from_pixbuf(pixbuf17)

	#image18
	self.image18= gtk.Image()
	pixbuf18 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto18.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image18.set_from_pixbuf(pixbuf18)

	#image19
	self.image19= gtk.Image()
	pixbuf19 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto19.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image19.set_from_pixbuf(pixbuf19)

	#image20
	self.image20= gtk.Image()
	pixbuf20 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto20.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image20.set_from_pixbuf(pixbuf20)

	#image21
	self.image21= gtk.Image()
	pixbuf21 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto21.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image21.set_from_pixbuf(pixbuf21)

	#image22
	self.image22= gtk.Image()
	pixbuf22 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto22.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image22.set_from_pixbuf(pixbuf22)

	#image23
	self.image23= gtk.Image()
	pixbuf23 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto23.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image23.set_from_pixbuf(pixbuf23)

	#image24
	self.image24= gtk.Image()
	pixbuf24 =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto24.jpg', 
	width=250, 
	height=250, 
	preserve_aspect_ratio=True)
	self.image24.set_from_pixbuf(pixbuf24)
	
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

	#Button6
	self.Button[6].add(self.image6)
	self.Button[6].set_size_request(100,100)
	self.Button[6].connect('clicked', lambda arg: Inseto6(self))
	#----------------------------------------

	#Button7
	self.Button[7].add(self.image7)
	self.Button[7].set_size_request(100,100)
	self.Button[7].connect('clicked', lambda arg: Inseto7(self))
	#----------------------------------------	

	#Button8
	self.Button[8].add(self.image8)
	self.Button[8].set_size_request(100,100)
	self.Button[8].connect('clicked', lambda arg: Inseto8(self))
	#----------------------------------------

	#Button9
	self.Button[9].add(self.image9)
	self.Button[9].set_size_request(100,100)
	self.Button[9].connect('clicked', lambda arg: Inseto9(self))
	#----------------------------------------

	#Button10
	self.Button[10].add(self.image10)
	self.Button[10].set_size_request(100,100)
	self.Button[10].connect('clicked', lambda arg: Inseto10(self))
	#----------------------------------------		

	#Button11
	self.Button[11].add(self.image11)
	self.Button[11].set_size_request(100,100)
	self.Button[11].connect('clicked', lambda arg: Inseto11(self))
	#----------------------------------------		

	#Button12
	self.Button[12].add(self.image12)
	self.Button[12].set_size_request(100,100)
	self.Button[12].connect('clicked', lambda arg: Inseto12(self))
	#----------------------------------------	

	#Button13
	self.Button[13].add(self.image13)
	self.Button[13].set_size_request(100,100)
	self.Button[13].connect('clicked', lambda arg: Inseto13(self))
	#----------------------------------------	

	#Button14
	self.Button[14].add(self.image14)
	self.Button[14].set_size_request(100,100)
	self.Button[14].connect('clicked', lambda arg: Inseto14(self))
	#----------------------------------------

	#Button15
	self.Button[15].add(self.image15)
	self.Button[15].set_size_request(100,100)
	self.Button[15].connect('clicked', lambda arg: Inseto15(self))
	#----------------------------------------		

	#Button16
	self.Button[16].add(self.image16)
	self.Button[16].set_size_request(100,100)
	self.Button[16].connect('clicked', lambda arg: Inseto16(self))
	#----------------------------------------	

	#Button17
	self.Button[17].add(self.image17)
	self.Button[17].set_size_request(100,100)
	self.Button[17].connect('clicked', lambda arg: Inseto17(self))
	#----------------------------------------	

	#Button18
	self.Button[18].add(self.image18)
	self.Button[18].set_size_request(100,100)
	self.Button[18].connect('clicked', lambda arg: Inseto18(self))
	#----------------------------------------

	#Button19
	self.Button[19].add(self.image19)
	self.Button[19].set_size_request(100,100)
	self.Button[19].connect('clicked', lambda arg: Inseto19(self))
	#----------------------------------------	

	#Button20
	self.Button[20].add(self.image20)
	self.Button[20].set_size_request(100,100)
	self.Button[20].connect('clicked', lambda arg: Inseto20(self))
	#----------------------------------------

	#Button21
	self.Button[21].add(self.image21)
	self.Button[21].set_size_request(100,100)
	self.Button[21].connect('clicked', lambda arg: Inseto21(self))
	#----------------------------------------

	#Button22
	self.Button[22].add(self.image22)
	self.Button[22].set_size_request(100,100)
	self.Button[22].connect('clicked', lambda arg: Inseto22(self))
	#----------------------------------------	

	#Button23
	self.Button[23].add(self.image23)
	self.Button[23].set_size_request(100,100)
	self.Button[23].connect('clicked', lambda arg: Inseto23(self))
	#----------------------------------------	

	#Button24
	self.Button[24].add(self.image24)
	self.Button[24].set_size_request(100,100)
	self.Button[24].connect('clicked', lambda arg: Inseto24(self))
	#----------------------------------------	
	return 0