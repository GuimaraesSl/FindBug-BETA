import gi;gi.require_version('Gtk','3.0');from gi.repository import Gtk as gtk, GdkPixbuf, Gdk

def Inseto0(self):
	Inseto0 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto0.add(scrolled)

	Inseto0.set_border_width(10)
	Inseto0.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto0.jpeg', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[0].set_justify(gtk.Justification.LEFT)
	self.label[0].set_valign(gtk.Align.START)

	self.label[0].set_margin_left(0)
	self.label[0].set_margin_right(5)
	self.label[0].set_margin_top(5)

	grid.attach(self.label[0],1,0,1,1)

	self.Adictional[0].set_justify(gtk.Justification.FILL)
	self.Adictional[0].set_valign(gtk.Align.START)
	self.Adictional[0].set_halign(gtk.Align.START)
	self.Adictional[0].set_margin_left(5)
	self.Adictional[0].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[0],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto0
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()	

def Inseto1(self):
	Inseto1 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto1.add(scrolled)

	Inseto1.set_border_width(10)
	Inseto1.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto1.jpeg', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[1].set_justify(gtk.Justification.LEFT)
	self.label[1].set_valign(gtk.Align.START)

	self.label[1].set_margin_left(0)
	self.label[1].set_margin_right(5)
	self.label[1].set_margin_top(5)

	grid.attach(self.label[1],1,0,1,1)

	self.Adictional[1].set_justify(gtk.Justification.FILL)
	self.Adictional[1].set_valign(gtk.Align.START)
	self.Adictional[1].set_halign(gtk.Align.START)
	self.Adictional[1].set_margin_left(5)
	self.Adictional[1].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[1],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto1
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto2(self):
	Inseto2 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto2.add(scrolled)

	Inseto2.set_border_width(10)
	Inseto2.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto2.jpeg', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[2].set_justify(gtk.Justification.LEFT)
	self.label[2].set_valign(gtk.Align.START)

	self.label[2].set_margin_left(0)
	self.label[2].set_margin_right(5)
	self.label[2].set_margin_top(5)

	grid.attach(self.label[2],1,0,1,1)

	self.Adictional[2].set_justify(gtk.Justification.FILL)
	self.Adictional[2].set_valign(gtk.Align.START)
	self.Adictional[2].set_halign(gtk.Align.START)
	self.Adictional[2].set_margin_left(5)
	self.Adictional[2].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[2],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto2
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()	

def Inseto3(self):
	Inseto3 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto3.add(scrolled)

	Inseto3.set_border_width(10)
	Inseto3.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto3.jpeg', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[3].set_justify(gtk.Justification.LEFT)
	self.label[3].set_valign(gtk.Align.START)

	self.label[3].set_margin_left(0)
	self.label[3].set_margin_right(5)
	self.label[3].set_margin_top(5)

	grid.attach(self.label[3],1,0,1,1)

	self.Adictional[3].set_justify(gtk.Justification.FILL)
	self.Adictional[3].set_valign(gtk.Align.START)
	self.Adictional[3].set_halign(gtk.Align.START)
	self.Adictional[3].set_margin_left(5)
	self.Adictional[3].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[3],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto3
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()	

def Inseto4(self):
	Inseto4 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto4.add(scrolled)

	Inseto4.set_border_width(10)
	Inseto4.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto4.jpeg', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[4].set_justify(gtk.Justification.LEFT)
	self.label[4].set_valign(gtk.Align.START)

	self.label[4].set_margin_left(0)
	self.label[4].set_margin_right(5)
	self.label[4].set_margin_top(5)

	grid.attach(self.label[4],1,0,1,1)

	self.Adictional[4].set_justify(gtk.Justification.FILL)
	self.Adictional[4].set_valign(gtk.Align.START)
	self.Adictional[4].set_halign(gtk.Align.START)
	self.Adictional[4].set_margin_left(5)
	self.Adictional[4].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[4],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_backiground_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto4
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()	

def Inseto5(self):
	Inseto5 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto5.add(scrolled)

	Inseto5.set_border_width(10)
	Inseto5.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto5.jpeg', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[5].set_justify(gtk.Justification.LEFT)
	self.label[5].set_valign(gtk.Align.START)

	self.label[5].set_margin_left(0)
	self.label[5].set_margin_right(5)
	self.label[5].set_margin_top(5)

	grid.attach(self.label[5],1,0,1,1)

	self.Adictional[5].set_justify(gtk.Justification.FILL)
	self.Adictional[5].set_valign(gtk.Align.START)
	self.Adictional[5].set_halign(gtk.Align.START)
	self.Adictional[5].set_margin_left(5)
	self.Adictional[5].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[5],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto5
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto6(self):
	Inseto6 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto6.add(scrolled)

	Inseto6.set_border_width(10)
	Inseto6.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto6.png', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[6].set_justify(gtk.Justification.LEFT)
	self.label[6].set_valign(gtk.Align.START)

	self.label[6].set_margin_left(0)
	self.label[6].set_margin_right(5)
	self.label[6].set_margin_top(5)

	grid.attach(self.label[6],1,0,1,1)

	self.Adictional[6].set_justify(gtk.Justification.FILL)
	self.Adictional[6].set_valign(gtk.Align.START)
	self.Adictional[6].set_halign(gtk.Align.START)
	self.Adictional[6].set_margin_left(5)
	self.Adictional[6].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[6],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto6
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto7(self):
	Inseto7 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto7.add(scrolled)

	Inseto7.set_border_width(10)
	Inseto7.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto7.jpg', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[7].set_justify(gtk.Justification.LEFT)
	self.label[7].set_valign(gtk.Align.START)

	self.label[7].set_margin_left(0)
	self.label[7].set_margin_right(5)
	self.label[7].set_margin_top(5)

	grid.attach(self.label[7],1,0,1,1)

	self.Adictional[7].set_justify(gtk.Justification.FILL)
	self.Adictional[7].set_valign(gtk.Align.START)
	self.Adictional[7].set_halign(gtk.Align.START)
	self.Adictional[7].set_margin_left(5)
	self.Adictional[7].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[7],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto7
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto8(self):
	Inseto8 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto8.add(scrolled)

	Inseto8.set_border_width(10)
	Inseto8.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto8.png', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[8].set_justify(gtk.Justification.LEFT)
	self.label[8].set_valign(gtk.Align.START)

	self.label[8].set_margin_left(0)
	self.label[8].set_margin_right(5)
	self.label[8].set_margin_top(5)

	grid.attach(self.label[8],1,0,1,1)

	self.Adictional[8].set_justify(gtk.Justification.FILL)
	self.Adictional[8].set_valign(gtk.Align.START)
	self.Adictional[8].set_halign(gtk.Align.START)
	self.Adictional[8].set_margin_left(5)
	self.Adictional[8].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[8],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto8
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto9(self):
	Inseto9 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto9.add(scrolled)

	Inseto9.set_border_width(10)
	Inseto9.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto9.jpg', 
	width=500, 
	height=350, 
	preserve_aspect_ratio=True)
	image = gtk.Image()
	image.set_from_pixbuf(pixbuf)
	image.set_halign(gtk.Align.START)
	image.set_margin_left(5)
	image.set_margin_right(5)
	image.set_margin_top(5)
	image.set_margin_bottom(5)
	grid.attach(image,0,0,1,1)
	
	
	self.label[9].set_justify(gtk.Justification.LEFT)
	self.label[9].set_valign(gtk.Align.START)

	self.label[9].set_margin_left(0)
	self.label[9].set_margin_right(5)
	self.label[9].set_margin_top(5)

	grid.attach(self.label[9],1,0,1,1)

	self.Adictional[9].set_justify(gtk.Justification.FILL)
	self.Adictional[9].set_valign(gtk.Align.START)
	self.Adictional[9].set_halign(gtk.Align.START)
	self.Adictional[9].set_margin_left(5)
	self.Adictional[9].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[9],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto9
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()