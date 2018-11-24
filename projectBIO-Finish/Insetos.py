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

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
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

def Inseto10(self):
	Inseto10 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto10.add(scrolled)

	Inseto10.set_border_width(10)
	Inseto10.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto10.jpg', 
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
	
	
	self.label[10].set_justify(gtk.Justification.LEFT)
	self.label[10].set_valign(gtk.Align.START)

	self.label[10].set_margin_left(0)
	self.label[10].set_margin_right(5)
	self.label[10].set_margin_top(5)

	grid.attach(self.label[10],1,0,1,1)

	self.Adictional[10].set_justify(gtk.Justification.FILL)
	self.Adictional[10].set_valign(gtk.Align.START)
	self.Adictional[10].set_halign(gtk.Align.START)
	self.Adictional[10].set_margin_left(5)
	self.Adictional[10].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[10],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto10
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto11(self):
	Inseto11 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto11.add(scrolled)

	Inseto11.set_border_width(10)
	Inseto11.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto11.jpg', 
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
	
	
	self.label[11].set_justify(gtk.Justification.LEFT)
	self.label[11].set_valign(gtk.Align.START)

	self.label[11].set_margin_left(0)
	self.label[11].set_margin_right(5)
	self.label[11].set_margin_top(5)

	grid.attach(self.label[11],1,0,1,1)

	self.Adictional[11].set_justify(gtk.Justification.FILL)
	self.Adictional[11].set_valign(gtk.Align.START)
	self.Adictional[11].set_halign(gtk.Align.START)
	self.Adictional[11].set_margin_left(5)
	self.Adictional[11].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[11],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto11
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto12(self):
	Inseto12 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto12.add(scrolled)

	Inseto12.set_border_width(10)
	Inseto12.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto12.jpg', 
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
	
	
	self.label[12].set_justify(gtk.Justification.LEFT)
	self.label[12].set_valign(gtk.Align.START)

	self.label[12].set_margin_left(0)
	self.label[12].set_margin_right(5)
	self.label[12].set_margin_top(5)

	grid.attach(self.label[12],1,0,1,1)

	self.Adictional[12].set_justify(gtk.Justification.FILL)
	self.Adictional[12].set_valign(gtk.Align.START)
	self.Adictional[12].set_halign(gtk.Align.START)
	self.Adictional[12].set_margin_left(5)
	self.Adictional[12].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[12],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto12
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto13(self):
	Inseto13 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto13.add(scrolled)

	Inseto13.set_border_width(10)
	Inseto13.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto13.jpg', 
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
	
	
	self.label[13].set_justify(gtk.Justification.LEFT)
	self.label[13].set_valign(gtk.Align.START)

	self.label[13].set_margin_left(0)
	self.label[13].set_margin_right(5)
	self.label[13].set_margin_top(5)

	grid.attach(self.label[13],1,0,1,1)

	self.Adictional[13].set_justify(gtk.Justification.FILL)
	self.Adictional[13].set_valign(gtk.Align.START)
	self.Adictional[13].set_halign(gtk.Align.START)
	self.Adictional[13].set_margin_left(5)
	self.Adictional[13].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[13],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto13
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto14(self):
	Inseto14 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto14.add(scrolled)

	Inseto14.set_border_width(10)
	Inseto14.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto14.jpg', 
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
	
	
	self.label[14].set_justify(gtk.Justification.LEFT)
	self.label[14].set_valign(gtk.Align.START)

	self.label[14].set_margin_left(0)
	self.label[14].set_margin_right(5)
	self.label[14].set_margin_top(5)

	grid.attach(self.label[14],1,0,1,1)

	self.Adictional[14].set_justify(gtk.Justification.FILL)
	self.Adictional[14].set_valign(gtk.Align.START)
	self.Adictional[14].set_halign(gtk.Align.START)
	self.Adictional[14].set_margin_left(5)
	self.Adictional[14].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[14],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto14
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto15(self):
	Inseto15 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto15.add(scrolled)

	Inseto15.set_border_width(10)
	Inseto15.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto15.jpg', 
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
	
	
	self.label[15].set_justify(gtk.Justification.LEFT)
	self.label[15].set_valign(gtk.Align.START)

	self.label[15].set_margin_left(0)
	self.label[15].set_margin_right(5)
	self.label[15].set_margin_top(5)

	grid.attach(self.label[15],1,0,1,1)

	self.Adictional[15].set_justify(gtk.Justification.FILL)
	self.Adictional[15].set_valign(gtk.Align.START)
	self.Adictional[15].set_halign(gtk.Align.START)
	self.Adictional[15].set_margin_left(5)
	self.Adictional[15].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[15],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto15
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto16(self):
	Inseto16 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto16.add(scrolled)

	Inseto16.set_border_width(10)
	Inseto16.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto16.jpg', 
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
	
	
	self.label[16].set_justify(gtk.Justification.LEFT)
	self.label[16].set_valign(gtk.Align.START)

	self.label[16].set_margin_left(0)
	self.label[16].set_margin_right(5)
	self.label[16].set_margin_top(5)

	grid.attach(self.label[16],1,0,1,1)

	self.Adictional[16].set_justify(gtk.Justification.FILL)
	self.Adictional[16].set_valign(gtk.Align.START)
	self.Adictional[16].set_halign(gtk.Align.START)
	self.Adictional[16].set_margin_left(5)
	self.Adictional[16].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[16],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto16
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto17(self):
	Inseto17 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto17.add(scrolled)

	Inseto17.set_border_width(10)
	Inseto17.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto17.jpg', 
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
	
	
	self.label[17].set_justify(gtk.Justification.LEFT)
	self.label[17].set_valign(gtk.Align.START)

	self.label[17].set_margin_left(0)
	self.label[17].set_margin_right(5)
	self.label[17].set_margin_top(5)

	grid.attach(self.label[17],1,0,1,1)

	self.Adictional[17].set_justify(gtk.Justification.FILL)
	self.Adictional[17].set_valign(gtk.Align.START)
	self.Adictional[17].set_halign(gtk.Align.START)
	self.Adictional[17].set_margin_left(5)
	self.Adictional[17].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[17],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto17
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto18(self):
	Inseto18 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto18.add(scrolled)

	Inseto18.set_border_width(10)
	Inseto18.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto18.jpg', 
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
	
	
	self.label[18].set_justify(gtk.Justification.LEFT)
	self.label[18].set_valign(gtk.Align.START)

	self.label[18].set_margin_left(0)
	self.label[18].set_margin_right(5)
	self.label[18].set_margin_top(5)

	grid.attach(self.label[18],1,0,1,1)

	self.Adictional[18].set_justify(gtk.Justification.FILL)
	self.Adictional[18].set_valign(gtk.Align.START)
	self.Adictional[18].set_halign(gtk.Align.START)
	self.Adictional[18].set_margin_left(5)
	self.Adictional[18].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[18],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto18
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto19(self):
	Inseto19 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto19.add(scrolled)

	Inseto19.set_border_width(10)
	Inseto19.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto19.jpg', 
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
	
	
	self.label[19].set_justify(gtk.Justification.LEFT)
	self.label[19].set_valign(gtk.Align.START)

	self.label[19].set_margin_left(0)
	self.label[19].set_margin_right(5)
	self.label[19].set_margin_top(5)

	grid.attach(self.label[19],1,0,1,1)

	self.Adictional[19].set_justify(gtk.Justification.FILL)
	self.Adictional[19].set_valign(gtk.Align.START)
	self.Adictional[19].set_halign(gtk.Align.START)
	self.Adictional[19].set_margin_left(5)
	self.Adictional[19].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[19],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto19
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto20(self):
	Inseto20 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto20.add(scrolled)

	Inseto20.set_border_width(10)
	Inseto20.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto20.jpg', 
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
	
	
	self.label[20].set_justify(gtk.Justification.LEFT)
	self.label[20].set_valign(gtk.Align.START)

	self.label[20].set_margin_left(0)
	self.label[20].set_margin_right(5)
	self.label[20].set_margin_top(5)

	grid.attach(self.label[20],1,0,1,1)

	self.Adictional[20].set_justify(gtk.Justification.FILL)
	self.Adictional[20].set_valign(gtk.Align.START)
	self.Adictional[20].set_halign(gtk.Align.START)
	self.Adictional[20].set_margin_left(5)
	self.Adictional[20].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[20],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto20
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto21(self):
	Inseto21 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto21.add(scrolled)

	Inseto21.set_border_width(10)
	Inseto21.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto21.jpg', 
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
	
	
	self.label[21].set_justify(gtk.Justification.LEFT)
	self.label[21].set_valign(gtk.Align.START)

	self.label[21].set_margin_left(0)
	self.label[21].set_margin_right(5)
	self.label[21].set_margin_top(5)

	grid.attach(self.label[21],1,0,1,1)

	self.Adictional[21].set_justify(gtk.Justification.FILL)
	self.Adictional[21].set_valign(gtk.Align.START)
	self.Adictional[21].set_halign(gtk.Align.START)
	self.Adictional[21].set_margin_left(5)
	self.Adictional[21].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[21],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto21
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto22(self):
	Inseto22 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto22.add(scrolled)

	Inseto22.set_border_width(10)
	Inseto22.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto22.jpg', 
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
	
	
	self.label[22].set_justify(gtk.Justification.LEFT)
	self.label[22].set_valign(gtk.Align.START)

	self.label[22].set_margin_left(0)
	self.label[22].set_margin_right(5)
	self.label[22].set_margin_top(5)

	grid.attach(self.label[22],1,0,1,1)

	self.Adictional[22].set_justify(gtk.Justification.FILL)
	self.Adictional[22].set_valign(gtk.Align.START)
	self.Adictional[22].set_halign(gtk.Align.START)
	self.Adictional[22].set_margin_left(5)
	self.Adictional[22].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[22],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto22
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto23(self):
	Inseto23 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto23.add(scrolled)

	Inseto23.set_border_width(10)
	Inseto23.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto23.jpg', 
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
	
	
	self.label[23].set_justify(gtk.Justification.LEFT)
	self.label[23].set_valign(gtk.Align.START)

	self.label[23].set_margin_left(0)
	self.label[23].set_margin_right(5)
	self.label[23].set_margin_top(5)

	grid.attach(self.label[23],1,0,1,1)

	self.Adictional[23].set_justify(gtk.Justification.FILL)
	self.Adictional[23].set_valign(gtk.Align.START)
	self.Adictional[23].set_halign(gtk.Align.START)
	self.Adictional[23].set_margin_left(5)
	self.Adictional[23].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[23],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto23
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()

def Inseto24(self):
	Inseto24 = gtk.Window()

	scrolled = gtk.ScrolledWindow()
	scrolled.set_policy(gtk.PolicyType.NEVER, gtk.PolicyType.AUTOMATIC)
	grid = gtk.Grid()
	scrolled.add(grid)
	Inseto24.add(scrolled)

	Inseto24.set_border_width(10)
	Inseto24.set_default_size(700, 500)

	pixbuf =  GdkPixbuf.Pixbuf.new_from_file_at_scale(
	filename='Pics/inseto24.jpg', 
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
	
	
	self.label[24].set_justify(gtk.Justification.LEFT)
	self.label[24].set_valign(gtk.Align.START)

	self.label[24].set_margin_left(0)
	self.label[24].set_margin_right(5)
	self.label[24].set_margin_top(5)

	grid.attach(self.label[24],1,0,1,1)

	self.Adictional[24].set_justify(gtk.Justification.FILL)
	self.Adictional[24].set_valign(gtk.Align.START)
	self.Adictional[24].set_halign(gtk.Align.START)
	self.Adictional[24].set_margin_left(5)
	self.Adictional[24].set_line_wrap(True)
	
	grid.attach_next_to(self.Adictional[24],image, gtk.PositionType.BOTTOM, 1, 1)

	grid.override_background_color(0, Gdk.RGBA(0,139,0,0.5))
	#                                       (red,green,blue,alpha)

	Ani = Inseto24
	Ani.connect("destroy", gtk.main_quit)
	Ani.show_all()
	gtk.main()