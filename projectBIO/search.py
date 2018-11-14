import gi;gi.require_version('Gtk','3.0');from gi.repository import Gtk as gtk, GdkPixbuf, Gdk
from MenuBar import *
from Result import *
from Insetos import *

#After Two Hours Are Working Bitchhhhhhhhh 
def ListAll(self):
	Sol(self)
	i = 0
	l = 0
	d = 0
	for c in range(len(self.label)):
		if i == 4:
			i = 1
			l = 0 
			d += 1
			self.grid_result.attach(self.Button[c],l,d,1,1)
			l += 1
		else: 
			self.grid_result.attach(self.Button[c],l,d,1,1)
			l += 1
			i += 1
	
	self.Soly.show_all()
	gtk.main()

def Search(self):
	Sol(self)
	TextEntry = self.Entrada.get_text()
	i = 0
	l = 0
	d = 0
	if TextEntry == '':
		Nomes = []
		Nomes.append(self.Nome_Ordem)
		Nomes.append(self.Nome_Family)
		Nomes.append(self.Nome_SubFamily)
		Nomes.append(self.Nome_Genero)

		for c in range(len(self.label)):
			gin = self.label[c].get_text()
			while '' in Nomes:
				Nomes.remove('')
			while '-' in Nomes:
				Nomes.remove('-')
			try:
				if Nomes[0] in gin and Nomes[1] in gin and  Nomes[2] in gin and  Nomes[3] in gin:
					if i == 4:
						i = 1
						l = 0 
						d += 1
						self.grid_result.attach(self.Button[c],l,d,1,1)
						l += 1
					else: 
						self.grid_result.attach(self.Button[c],l,d,1,1)
						l += 1
						i += 1
			except:
				try:
					if Nomes[0] in gin and Nomes[1] in gin and  Nomes[2] in gin:
						if i == 4:
							i = 1
							l = 0 
							d += 1
							self.grid_result.attach(self.Button[c],l,d,1,1)
							l += 1
						else: 
							self.grid_result.attach(self.Button[c],l,d,1,1)
							l += 1
							i += 1
				except:	
					try:
						if Nomes[0] in gin and Nomes[1] in gin:
							if i == 4:
								i = 1
								l = 0 
								d += 1
								self.grid_result.attach(self.Button[c],l,d,1,1)
								l += 1
							else: 
								self.grid_result.attach(self.Button[c],l,d,1,1)
								l += 1
								i += 1
					except:
						if Nomes[0] in gin:
							if i == 4:
								i = 1
								l = 0 
								d += 1
								self.grid_result.attach(self.Button[c],l,d,1,1)
								l += 1
							else: 
								self.grid_result.attach(self.Button[c],l,d,1,1)
								l += 1
								i += 1

	else:
		for c in range(len(self.label)):
			gin = self.label[c].get_text()
			TextEntry = TextEntry.upper()
			gin2 = self.Adictional[c].get_text()
			if TextEntry in gin or TextEntry in gin2:
				if i == 4:
					i = 1
					l = 0 
					d += 1
					self.grid_result.attach(self.Button[c],l,d,1,1)
					l += 1
				else: 
					self.grid_result.attach(self.Button[c],l,d,1,1)
					l += 1
					i += 1

	
	self.Soly.show_all()
	gtk.main()