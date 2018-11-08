import gi;gi.require_version('Gtk','3.0');from gi.repository import Gtk as gtk, GdkPixbuf, Gdk
from search import *
from Result import *
from Insetos import *

class MenuB(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self,title='FindBug-BETA')
		self.set_border_width(5)
		self.set_default_size(0, 200)
		self.set_position(gtk.WindowPosition.CENTER)
		
		self.Grid_Menu = gtk.Grid(column_spacing=6, row_spacing=6)
		self.add(self.Grid_Menu)

		self.hb = gtk.HeaderBar()
		self.hb.set_show_close_button(True)
		self.hb.props.title = "FindBug-BETA"
		self.set_titlebar(self.hb)

		#Label.....
		self.label = []
		for g in range(100):
			self.label.append(gtk.Label())	

		#Label.....
		self.Adictional = []
		for g in range(100):
			self.Adictional.append(gtk.Label())	

		self.label[0].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> NYSIUS SP\n<b>NOMES COMUNS:</b> NÃO DEFINIDO\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> LYGAEIDAE\n<b>SUBFAMÍLIA:</b> ORSILLINAE\n<b>GÊNERO:</b> NYSIUS</span>")
		self.Adictional[0].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS:</b> APRESENTA COR CINZA ESCURA E PORTE PEQUENO, MEDINDO 4MM DE COMPRIMENTO E 1MM DE LARGURA. AS NINFAS SÃO BEM MÓVEIS NO SOLO E COM A INCIDÊNCIA SOLAR ALTA, SE ESCONDEM NA PALHADA DE ÁREAS COM PLANTIO.</span>")
		
		self.label[1].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> NEZARA VIRIDULA\n<b>NOMES COMUNS:</b>\n FEDE-FEDE-DA-SOJA\n PECEVEJO-VERDE\n PECEVEJO-VERDE-DA-SOJA\n PECEVEJO-DA-SOJA\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> PENTATOMIDAE\n<b>SUBFAMÍLIA:</b> PENTATOMINAE\n<b>GÊNERO:</b> sdsjsfgjasdfa</span>")
		self.Adictional[1].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: </b>OS PERCEVEJOS INJETAM TOXINAS NOS GRÃOS, PERFURAM A PLANTA, ONDE FORMAM MANCHAS MARRONS OU ENEGRECIDAS. RETARDO DO CRESCIMENTO DOS FRUTOS IMATUROS. QUEDA PREMATURA DOS FRUTOS E FLORES. FRUTOS DEFORMADOS. POSSIBILITA A INSTALAÇÃO DE BACTÉRIAS E FUNGOS QUE INFECTAM CAROÇOS, NOZES E SEMENTE AFETANDO O SABOR DO PRODUTO. MANCHAS EM GRÃOS. SEMENTES ATROFIADAS, ENRUGADAS, DEFORMADAS E PRESENÇA DE MANCHA PRETA EM UMA DEPRESSÃO. FUMAGINA SOBRE FOLHAS. REDUÇÃO DA PRODUTIVIDADE DA PLANTA. OVOS: SÃO DE COR CREME A AMARELA, LIGEIRAMENTE ALONGADOS, DEPOIS AMARELOS A ALARANJADOS, EM SEGUIDA, ROSADOS E, FINALMENTE, BRILHANTES. NINFAS: ANTENAS ,NÃO POSSUEM ASAS, MAS POSSUEM ALMOFADAS LATERAIS,QUE SÃO DE COR PRETA QUANDO ECLODEM DO OVO E DE ACORDO COM O DESENVOLVIMENTO TORNAM-SE VERDES. ADULTOS: MEDEM, APROXIMADAMENTE 15 X 8 MM DE TAMANHO, POSSUEM COLORAÇÃO VERDE, TRÊS PEQUENOS PONTOS BRANCOS SÃO, GERALMENTE, EVIDENTES NA BORDA FRONTAL.</span>")
		
		self.label[2].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> APIOMERUS SP.\n<b>NOMES COMUNS:</b> PERCEVEJO PREDADOR\n ASSASSINOS DE ABELHAS \n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> REDUVIIDAE\n<b>SUBFAMÍLIA:</b> HARPACTORINAE\n<b>GÊNERO:</b> NÃO DEFINIDO</span>")
		self.Adictional[2].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS:</b> </span>")
		
		self.label[3].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> ONCOMETOPIA FACIALIS\n<b>NOMES COMUNS:</b> CIGARRINHAS DA CVC\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> CICADELLIDAE\n<b>SUBFAMÍLIA:</b> CICADELLINAE\n<b>GÊNERO:</b> NÃO DEFINIDO</span>")
		self.Adictional[3].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS:</b>OS OVOS SÃO COLOCADOS PELAS FÊMEAS UM AO LADO DO OUTRO, EM UMA ÚNICA CAMADA E COBERTOS POR UMA FINA CAMADA DE CERA. ESTA ESPÉCIE TEM PREFERÊNCIA PELOS RAMOS MAIS DESENVOLVIDOS, E ENCONTRADA PRINCIPALMENTE NOS RAMOS ERETOS. AS NINFAS SÃO ESCURAS AO NASCEREM E TEM PERÍODO DE CRESCIMENTO DE 76 DIAS. MEDE CERCA DE 1,1 CM, TEM ASAS MARRONS, MESCLANDO ÁREAS TRANSPARENTES E DOURADAS, COM UMA MANCHA ESCURA NA PARTE POSTERIOR DA CABEÇA. APARÊNCIA (COR): COROA DE COLORAÇÃO VIOLETA COM MANCHA PRETA SUBTRIANGULAR DANOS: CRESCIMENTO VEGETATIVO DA PLANTA E ATACANDO OS ÓRGÃOS SUBTERRÂNEOS. </span>")
		
		self.label[4].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>ZICCA NIGROPUNCTATA\n<b>NOMES COMUNS:</b> NÃO DEFINIDO\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> COREIDAE\n<b>SUBFAMÍLIA:</b> COREINAE\n<b>GÊNERO:</b> NÃO DEFINIDO</span>")
		self.Adictional[4].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS:</b></span>")

		self.label[5].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>ORIUS INSIDIOSUS\n<b>NOMES COMUNS:</b> NÃO DEFINIDO\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> CANTHOCORIDAE\n<b>SUBFAMÍLIA:</b> NAO ENCONTRADA\n<b>GÊNERO:</b> NÃO DEFINIDO </span>")
		self.Adictional[5].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS:</b> </span>")

		#Entry
		#focusGained and Lost
		#hint
		self.Entrada = gtk.Entry()
		self.Entrada.set_margin_bottom(10)
		self.Entrada.set_margin_top(10)
		self.Entrada.set_margin_left(10)
		self.Entrada.set_margin_right(10)
		self.Grid_Menu.attach(self.Entrada,0,0,4,1)
		self.Entrada.connect("activate", lambda arg: Search(self))


		#Label de Ordem
		self.Ordem_Label = gtk.Label()

		self.Ordem_Label.set_margin_bottom(0)
		self.Ordem_Label.set_margin_top(10)
		self.Ordem_Label.set_margin_left(10)
		self.Ordem_Label.set_margin_right(10)
		
		self.Grid_Menu.attach(self.Ordem_Label, 0, 1,1,1)
		self.Ordem_Label.set_markup("<span foreground='#171212' size='11000' face='Arial'><b>Ordem</b></span>")

		#Label de Familly
		self.Familly_Label = gtk.Label()
		self.Familly_Label.set_margin_bottom(0)
		self.Familly_Label.set_margin_top(10)
		self.Familly_Label.set_margin_left(10)
		self.Familly_Label.set_margin_right(10)
		self.Grid_Menu.attach(self.Familly_Label, 1, 1,1,1)
		self.Familly_Label.set_markup("<span foreground='#171212' size='11000' face='Arial'><b>Família</b></span>")

		#Label de SubFamilly
		self.SubFamilly_Label = gtk.Label()
		self.SubFamilly_Label.set_margin_bottom(0)
		self.SubFamilly_Label.set_margin_top(10)
		self.SubFamilly_Label.set_margin_left(10)
		self.SubFamilly_Label.set_margin_right(10)
		self.Grid_Menu.attach(self.SubFamilly_Label, 2, 1,1,1)
		self.SubFamilly_Label.set_markup("<span foreground='#171212' size='11000' face='Arial'><b>Subfamília</b></span>")

		#Label de Genero
		self.Genero_Label = gtk.Label()

		self.Genero_Label.set_margin_bottom(0)
		self.Genero_Label.set_margin_top(10)
		self.Genero_Label.set_margin_left(10)
		self.Genero_Label.set_margin_right(10)

		self.Grid_Menu.attach(self.Genero_Label, 3, 1,1,1)
		self.Genero_Label.set_markup("<span foreground='#171212' size='11000' face='Arial'><b>Gênero</b></span>")

		#Store das Ordens
		self.Ordem_store = gtk.ListStore(int, str)
		#
		#Ordem_Combo
		self.Ordem_combo = gtk.ComboBox.new_with_model_and_entry(self.Ordem_store)
		self.Ordem_combo.set_margin_bottom(0)
		self.Ordem_combo.set_margin_top(1)
		self.Ordem_combo.set_margin_left(10)
		self.Ordem_combo.set_margin_right(10)
		self.Grid_Menu.attach(self.Ordem_combo, 0, 2,1,1)
		
		#Store das Family's
		self.Family_store = gtk.ListStore(float,str)

		#Family_Combo
		self.Family_combo = gtk.ComboBox.new_with_model_and_entry(self.Family_store)
		self.Family_combo.set_margin_bottom(0)
		self.Family_combo.set_margin_top(1)
		self.Family_combo.set_margin_left(10)
		self.Family_combo.set_margin_right(10)
		self.Grid_Menu.attach(self.Family_combo, 1, 2,1,1)

		#Store das SubFamily's
		self.SubFamily_store = gtk.ListStore(float,str)

		#SubFamily_Combo
		self.SubFamily_combo = gtk.ComboBox.new_with_model_and_entry(self.SubFamily_store)
		self.SubFamily_combo.set_margin_bottom(0)
		self.SubFamily_combo.set_margin_top(1)
		self.SubFamily_combo.set_margin_left(10)
		self.SubFamily_combo.set_margin_right(10)
		self.Grid_Menu.attach(self.SubFamily_combo, 2, 2,1,1)

		#StoreGenero
		self.Genero_store = gtk.ListStore(float,str)

		#Genero_Combo
		self.Genero_combo = gtk.ComboBox.new_with_model_and_entry(self.Genero_store)
		self.Genero_combo.set_margin_bottom(0)
		self.Genero_combo.set_margin_top(1)
		self.Genero_combo.set_margin_left(10)
		self.Genero_combo.set_margin_right(10)
		self.Grid_Menu.attach(self.Genero_combo, 3, 2,1,1)

		#SearchButton
		self.search = gtk.Button(label="Search")

		self.search.set_margin_bottom(10)
		self.search.set_margin_top(10)
		self.search.set_margin_left(10)
		self.search.set_margin_right(10)
		
		self.search.connect("clicked",lambda arg: Search(self))
		self.Grid_Menu.attach(self.search,4,0,1,1)

		#BackGround Color
		self.Grid_Menu.override_background_color(0, Gdk.RGBA(0,0.4,0.2,3))
		

		self.Nome_Ordem = str()
		self.Nome_Family = str()
		self.Nome_SubFamily = str()
		self.Nome_Genero = str()

				
		self.All()

	def All(self):
		#OrdemStore
		self.Ordem_store.append([1.01, "-"])
		self.Ordem_store.append([1, "HEMIPTERA"])
	
		self.Ordem_combo.set_entry_text_column(1)
		self.Ordem_combo.connect("changed", self.on_Ordem_combo)

		#FamilyStore
		self.Family_store.append([2.01, "-"])
		self.Family_store.append([2.1, "LYGAEIDAE"])
		self.Family_store.append([2.2, "PENTATOMIDAE"])
		self.Family_store.append([2.3, "REDUVIIDAE"])
		self.Family_store.append([2.4, "CICADELLIDAE"])
		self.Family_store.append([2.5, "COREIDAE"])
		self.Family_store.append([2.6, "CANTHOCORIDAE"])
		
	
	
		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)

		#SubFamilyStore
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.1, "ORSILLINAE"])
		self.SubFamily_store.append([3.2, "PENTATOMINAE"])
		self.SubFamily_store.append([3.3, "HARPACTORINAE"])
		self.SubFamily_store.append([3.4, "CICADELLINAE"])
		self.SubFamily_store.append([3.5, "COREINAE"])

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

		#Gênero
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.1, "NYSIUS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)


	def on_Ordem_combo(self,Ordem_combo):
		self.tree_iter = Ordem_combo.get_active_iter()
		if self.tree_iter != None:
			self.model = Ordem_combo.get_model()
			self.ID, self.Nome_Ordem = self.model[self.tree_iter][:2]
			self.ID = int(self.ID) 
		
			if self.ID == 1:
				self.Family1()
			if self.ID == 2:
				self.Family2()

	def on_Family_combo(self,Family_combo):
		self.tree_iter_Family = Family_combo.get_active_iter()
		if self.tree_iter_Family != None:
			self.model_family = Family_combo.get_model()
			self.ID_F, self.Nome_Family = self.model_family[self.tree_iter_Family][:2]
			self.ID_Family = float(self.ID_F) 
		
			if self.ID_Family == 2.1:
				self.SubFamily1()

			if self.ID_Family == 2.2:
				self.SubFamily2()

			if self.ID_Family == 2.3:
				self.SubFamily3()

			if self.ID_Family == 2.4:
				self.SubFamily4()

			if self.ID_Family == 2.5:
				self.SubFamily5()
	
	
	def on_SubFamily_combo(self,SubFamily_combo):
		self.tree_iter_SubFamily = SubFamily_combo.get_active_iter()
		if self.tree_iter_SubFamily != None:
			self.model_Subfamily = SubFamily_combo.get_model()
			self.ID_SF, self.Nome_SubFamily = self.model_Subfamily[self.tree_iter_SubFamily][:2]
			self.ID_SubFamily = float(self.ID_SF) 

			if self.ID_SubFamily == 3.1:
				self.Genero1()

	def on_Genero_combo(self,Genero_combo):
		self.tree_iter_Genero = Genero_combo.get_active_iter()
		if self.tree_iter_Genero != None:
			self.model_Genero = Genero_combo.get_model()
			self.ID_G, self.Nome_Genero = self.model_Genero[self.tree_iter_Genero][:2]
			self.ID_Genero = float(self.ID_G) 

 #------------------------------------------DEF'S ORGANIZAÇÃO--------------------------------------
	def Family1(self):
		self.Family_store.clear()
		self.Family_store.append([2.02, "-"])
		self.Family_store.append([2.1, "LYGAEIDAE"])
		self.Family_store.append([2.2, "PENTATOMIDAE"])
		self.Family_store.append([2.3, "REDUVIIDAE"])
		self.Family_store.append([2.4, "CICADELLIDAE"])
		self.Family_store.append([2.5, "COREIDAE"])
		self.Family_store.append([2.6, "CANTHOCORIDAE"])


		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)

	def SubFamily1(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.1, "ORSILLINAE"])

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

	def SubFamily2(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

	def SubFamily3(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.3, "HARPACTORINAE"])
		

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

	def SubFamily4(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.3, "CICADELLINAE"])
		

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

	def SubFamily5(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.5, "COREINAE"])
		

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	
	def Genero1(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.1, "NYSIUS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
		