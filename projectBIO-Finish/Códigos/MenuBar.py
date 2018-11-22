import gi;gi.require_version('Gtk','3.0');from gi.repository import Gtk as gtk, GdkPixbuf, Gdk
from search import *
from Result import *
from Insetos import *

class MenuB(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self,title='FindBug-BETA')
		self.set_border_width(5)
		self.set_default_size(0, 150)
		self.set_position(gtk.WindowPosition.CENTER)
		
		self.Grid_Menu = gtk.Grid()
		self.add(self.Grid_Menu)

		self.hb = gtk.HeaderBar()
		self.hb.set_show_close_button(True)
		self.hb.props.title = "FindBug-BETA"
		self.set_titlebar(self.hb)

		#Label.....
		self.label = []
		for g in range(25):
			self.label.append(gtk.Label())	

		#Label.....
		self.Adictional = []
		for g in range(25):
			self.Adictional.append(gtk.Label())	

		self.label[0].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> NYSIUS SP\n<b>NOMES COMUNS:</b> NÃO DEFINIDO\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> LYGAEIDAE\n<b>SUBFAMÍLIA:</b> ORSILLINAE\n<b>GÊNERO:</b> NYSIUS</span>")
		self.Adictional[0].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS:</b> APRESENTA COR CINZA ESCURA E PORTE PEQUENO, MEDINDO 4MM DE COMPRIMENTO E 1MM DE LARGURA. AS NINFAS SÃO BEM MÓVEIS NO SOLO E COM A INCIDÊNCIA SOLAR ALTA, SE ESCONDEM NA PALHADA DE ÁREAS COM PLANTIO.</span>")
		
		self.label[1].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> NEZARA VIRIDULA\n<b>NOMES COMUNS:</b>\n FEDE-FEDE-DA-SOJA\n PECEVEJO-VERDE\n PECEVEJO-VERDE-DA-SOJA\n PECEVEJO-DA-SOJA\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> PENTATOMIDAE\n<b>SUBFAMÍLIA:</b> PENTATOMINAE\n<b>GÊNERO:</b> DICHELOPS</span>")
		self.Adictional[1].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: </b>OS PERCEVEJOS INJETAM TOXINAS NOS GRÃOS, PERFURAM A PLANTA, ONDE FORMAM MANCHAS MARRONS OU ENEGRECIDAS. RETARDO DO CRESCIMENTO DOS FRUTOS IMATUROS. QUEDA PREMATURA DOS FRUTOS E FLORES. FRUTOS DEFORMADOS. POSSIBILITA A INSTALAÇÃO DE BACTÉRIAS E FUNGOS QUE INFECTAM CAROÇOS, NOZES E SEMENTE AFETANDO O SABOR DO PRODUTO. MANCHAS EM GRÃOS. SEMENTES ATROFIADAS, ENRUGADAS, DEFORMADAS E PRESENÇA DE MANCHA PRETA EM UMA DEPRESSÃO. FUMAGINA SOBRE FOLHAS. REDUÇÃO DA PRODUTIVIDADE DA PLANTA. OVOS: SÃO DE COR CREME A AMARELA, LIGEIRAMENTE ALONGADOS, DEPOIS AMARELOS A ALARANJADOS, EM SEGUIDA, ROSADOS E, FINALMENTE, BRILHANTES. NINFAS: ANTENAS ,NÃO POSSUEM ASAS, MAS POSSUEM ALMOFADAS LATERAIS,QUE SÃO DE COR PRETA QUANDO ECLODEM DO OVO E DE ACORDO COM O DESENVOLVIMENTO TORNAM-SE VERDES. ADULTOS: MEDEM, APROXIMADAMENTE 15 X 8 MM DE TAMANHO, POSSUEM COLORAÇÃO VERDE, TRÊS PEQUENOS PONTOS BRANCOS SÃO, GERALMENTE, EVIDENTES NA BORDA FRONTAL.</span>")
		
		self.label[2].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> APIOMERUS SP.\n<b>NOMES COMUNS:</b> PERCEVEJO PREDADOR\n ASSASSINOS DE ABELHAS \n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> REDUVIIDAE\n<b>SUBFAMÍLIA:</b> HARPACTORINAE\n<b>GÊNERO:</b> NÃO DEFINIDO</span>")
		self.Adictional[2].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: ESPÉCIES PODEM SER ENCONTRADAS NOS ESTADOS UNIDOS, INDO PARA A AMÉRICA TROPICAL. O NOME COMUM DOS ASSASSINOS DE ABELHAS DERIVA DE SEU HÁBITO FREQUENTE DE SENTAR E ESPERAR FLORES E ABELHAS COMO PRESAS. POSSUI UMA CAMADA DE RESINA ADESIVA LOCALIZADA EM SEU ABDÔMEN DORSAL. ACREDITA-SE QUE A RESINA SEJA DERIVADA DE MATERIAL VEGETAL E PODE DESEMPENHAR UM PAPEL NA DEFESA DOS OVOS DA PREDAÇÃO, ESPECIALMENTE PELAS FORMIGAS.</b> </span>")
		
		self.label[3].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> ONCOMETOPIA FACIALIS\n<b>NOMES COMUNS:</b> CIGARRINHAS DA CVC\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> CICADELLIDAE\n<b>SUBFAMÍLIA:</b> CICADELLINAE\n<b>GÊNERO:</b> NÃO ONCOMETOPIA</span>")
		self.Adictional[3].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS:</b>OS OVOS SÃO COLOCADOS PELAS FÊMEAS UM AO LADO DO OUTRO, EM UMA ÚNICA CAMADA E COBERTOS POR UMA FINA CAMADA DE CERA. ESTA ESPÉCIE TEM PREFERÊNCIA PELOS RAMOS MAIS DESENVOLVIDOS, E ENCONTRADA PRINCIPALMENTE NOS RAMOS ERETOS. AS NINFAS SÃO ESCURAS AO NASCEREM E TEM PERÍODO DE CRESCIMENTO DE 76 DIAS. MEDE CERCA DE 1,1 CM, TEM ASAS MARRONS, MESCLANDO ÁREAS TRANSPARENTES E DOURADAS, COM UMA MANCHA ESCURA NA PARTE POSTERIOR DA CABEÇA. APARÊNCIA (COR): COROA DE COLORAÇÃO VIOLETA COM MANCHA PRETA SUBTRIANGULAR DANOS: CRESCIMENTO VEGETATIVO DA PLANTA E ATACANDO OS ÓRGÃOS SUBTERRÂNEOS. </span>")
		
		self.label[4].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>ZICCA NIGROPUNCTATA\n<b>NOMES COMUNS:</b> NÃO DEFINIDO\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> COREIDAE\n<b>SUBFAMÍLIA:</b> COREINAE\n<b>GÊNERO:</b> NÃO DEFINIDO</span>")
		self.Adictional[4].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS:</b></span>")

		self.label[5].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>ORIUS INSIDIOSUS\n<b>NOMES COMUNS:</b> INSETO DE FLOR\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> CANTHOCORIDAE\n<b>SUBFAMÍLIA:</b> ANTHOCORINAE\n<b>GÊNERO:</b> ANTHOCORINAE</span>")
		self.Adictional[5].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: O ORIUS INSIDIOSUS É UM IMPORTANTE PREDADOR DE MUITAS PRAGAS</b> </span>")

		self.label[6].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>BLATELLA GERMANICA\n<b>NOMES COMUNS:</b> BARATINHA OU BARATA-GERMÂNICA\n<b>ORDEM:</b> BLATTODEA\n<b>FAMÍLIA:</b> BLATTELLIDAE\n<b>SUBFAMÍLIA:</b> BLATTELLINAE\n<b>GÊNERO:</b> BLATELLA </span>")
		self.Adictional[6].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: POR HABITAREM LOCAIS SUJOS, COMO BUEIROS, CONTAMINAM ALIMENTOS CONSUMIDOS PELO HOMEM, CAUSANDO DOENÇAS COMO DIARREIA, LEPRA, DISENTERIA, GASTROENTERITES, TIFO, MENINGITE, PNEUMONIA, DIFTERIA, DENTRE OUTRAS. TAMBÉM PODEM CAUSAR DANOS CONSIDERÁVEIS EM ROUPAS, LIVROS, ETC, ALÉM DE IMPREGNAR OS LOCAIS COM CHEIRO DESAGRADÁVEL E CARACTERÍSTICO.</b> </span>")

		self.label[7].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>COELOSIS BICORNIS.\n<b>NOMES COMUNS:</b> BESOURO RINOCERONTE\n<b>ORDEM:</b> COLEOPTERA\n<b>FAMÍLIA:</b> SCARABAEIDAE\n<b>SUBFAMÍLIA:</b> DYNASTINAE\n<b>GÊNERO:</b> DYNASTES </span>")
		self.Adictional[7].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: VIVE EM FLORESTAS TROPICAIS DA AMÉRICA DO SUL. APRESENTAM GRANDES CHIFRES (APÊNDICES CEFÁLICOS E TORÁCICOS) SÓ ENCONTRADOS EM MACHOS E ESSES SÃO UTILIZADOS EM DISPUTAS ENTRE MACHOS, PELA FÊMEA, NA ÉPOCA DO ACASALAMENTO. É CAPAZ DE SUPORTAR 850 VEZES SEU PRÓPRIO PESO. MEDE ENTRE 30 A 57 MM DE COMPRIMENTO E ENTRE 14 A 21 MM DE LARGURA, NORMALMENTE É PRETO COM MESCLAS DE ENCARNADO MUITO ESCURO. ELE SE ALIMENTA DE MATÉRIA ORGÂNICA EM DECOMPOSIÇÃO. NÃO MORDE, NÃO PICA E NÃO É VENENOSO.</b> </span>")

		self.label[8].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>SPHENOPHORUS LEVIS.\n<b>NOMES COMUNS:</b>  BICUDO DA CANA – DE – AÇÚCAR\n<b>ORDEM:</b> COLEOPTERA\n<b>FAMÍLIA:</b> CURCULIONIDAE\n<b>SUBFAMÍLIA:</b> DRYOPHTHORINAE\n<b>GÊNERO:</b> SPHENOPHORUS </span>")
		self.Adictional[8].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: OS DANOS SÃO CAUSADOS PELAS LARVAS QUE ABRIGAM - SE NO INTERIOR DO RIZOMA E DANIFICAM OS TECIDOS. EM CONSEQUÊNCIA PODE OCORRER A MORTE DA PLANTA E FALHAS NAS BROTAÇÕES DAS SOQUEIRAS, COM PERDAS DE 20 A 30 TONELADAS DE CANA POR ANO. </b> </span>")

		self.label[9].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>ANTHONOMUS GRANDIS\n<b>NOMES COMUNS:</b>  BICUDO-DO-ALGODOEIRO\n<b>ORDEM:</b> COLEOPTERA\n<b>FAMÍLIA:</b> CURCULIONIDAE\n<b>SUBFAMÍLIA:</b> CURCULIONINAE\n<b>GÊNERO:</b> ANTHONOMUS </span>")
		self.Adictional[9].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: OS PRIMEIROS ADULTOS MIGRAM PARA A CULTURA POR OCASIÃO DO FLORESCIMENTO, ATRAÍDOS PELO CHEIRO, E ATACAM INICIALMENTE OS BOTÕES FLORAIS QUE, APÓS O ATAQUE, APRESENTAM AS BRÁCTEAS ABERTAS E, POSTERIORMENTE, CAEM.  AS FLORES ATACADAS FICAM COM O ASPECTO DE BALÃO (“FLOR EM BALÃO”), DEVIDO À ABERTURA ANORMAL DAS PÉTALAS. AS MAÇÃS DO ALGODÃO APRESENTAM PERFURAÇÕES EXTERNAS, SENDO QUE, INTERNAMENTE, AS FIBRAS E SEMENTES SÃO DESTRUÍDAS POR LARVAS DECORRENTES DE OVIPOSIÇÃO DO INSETO, E IMPEDEM SUA ABERTURA NORMAL (“CARIMÃ”), DEIXANDO-AS ENEGRECIDAS. </b> </span>")

		self.label[10].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>TERATOPACTUS NODICOLLIS\n<b>NOMES COMUNS:</b>  GORGULHO DO SOLO\n<b>ORDEM:</b> COLEOPTERA\n<b>FAMÍLIA:</b> CURCULIONIDAE\n<b>SUBFAMÍLIA:</b> POLYDROSINAE\n<b>GÊNERO:</b> TERATOPACTUS HELLER </span>")
		self.Adictional[10].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: AS LARVAS ALIMENTAM-SE DOS NÓDULOS EM LEGUMINOSAS, DA RADÍCULA E HIPOCÓTILO DAS PLANTAS E, NESTE CASO, AS PLANTAS MORREM ANTES DA EMERGÊNCIA, HAVENDO FALHAS NA LINHA DE PLANTIO. ELAS (AS LARVAS) PODEM CONSUMIR VÁRIAS PLANTAS, CAUSANDO MAIOR DANO NA FASE DE GERMINAÇÃO E NO INÍCIO DE DESENVOLVIMENTO VEGETATIVO. RESUMINDO, AS LARVAS DANIFICAM AS RAÍZES DA PLANTA. OS ADULTOS ATACAM FOLHAS E FLORES. </b> </span>")

		self.label[11].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>TRIGONA SPINIPES\n<b>NOMES COMUNS:</b> ABELHA IRAPUÃ\n<b>ORDEM:</b> HYMENOPTERA\n<b>FAMÍLIA:</b> APIDAE\n<b>SUBFAMÍLIA:</b> MELIPONÍNEOS\n<b>GÊNERO:</b> TRIGONA </span>")
		self.Adictional[11].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DDANOS: CAUSA DANOS Á FOLHAS, FLORES, FRUTOS, CASCA (TRONCO) /CORTIÇA. OS DANOS SÃO FEITOS POR MEIO DO CORTE DOS TECIDOS QUANDO ESTÃO À PROCURA DE UMA SUBSTÂNCIA PARA A CONSTRUÇÃO DO NINHO. DESTRUIÇÃO DE BOTÕES FLORAIS APRESENTANDO ORIFÍCIOS DE ALGUMAS PLANTAS, FERIMENTOS E DANIFICAÇÃO DOS FRUTOS, DESTRUIÇÃO DE CACHOS DE UVA, DANIFICAM BROTOS DE CITRUS (TODAS AS ESPÉCIES) E PODE OCASIONAR QUEDA DE FLORES. </b> </span>")

		self.label[12].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b>ARACANTHUS MOUREI\n<b>NOMES COMUNS:</b> TORRÃOZINHO\n<b>ORDEM:</b> COLEOPTERA\n<b>FAMÍLIA:</b> CURCULIONIDAE\n<b>SUBFAMÍLIA:</b> ENTIMINAE\n<b>GÊNERO:</b> ARACANTHUS </span>")
		self.Adictional[12].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: GERALMENTE O ADULTO INICIA SEU ATAQUE NAS BORDAS DA LAVOURA, JUNTO A ESTRADAS OU A TALHÕES DE MILHO QUE ESTÃO PRÓXIMOS DA SOJA. O DANO MAIS GRAVE E QUANDO O SEU ATAQUE OCORRE NA FASE INICIAL DO DESENVOLVIMENTO DA CULTURA E CARACTERIZAM-SE POR PEQUENOS ORIFÍCIO E CORTES NAS MARGENS DA FOLHA E DOS COTILÉDONES, CONFERINDO UM ASPECTO DE SERRILHADO E EM ÁREAS COM GRANDE INFESTAÇÃO, O INSETO PODE ATACAR TAMBÉM A GEMA APICAL DO VEGETAL. </b> </span>")

		self.label[13].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> PSYCHODA \n<b>NOMES COMUNS:</b> MOSCA DE ESGOTO, MOSCA-DE-BANHEIRO, MOSCA-DOS-FILTROS\n<b>ORDEM:</b> DIPTERA\n<b>FAMÍLIA:</b> PSYCHODIDAE\n<b>SUBFAMÍLIA:</b> PSYCHODINAE\n<b>GÊNERO:</b> CLOGMIA </span>")
		self.Adictional[13].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DESCRIÇÃO: ASPECTO DE UMA PEQUENA TRAÇA, COM O CORPO E AS ASAS RECOBERTOS POR UMA FINA CAMADA DE PEQUENOS PELOS DE COLORAÇÃO CINZENTO-ACASTANHADA </b> </span>")

		self.label[14].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> SUPELLA LOMGIPALPA \n<b>NOMES COMUNS:</b> BARATA DE FAIXA MARROM\n<b>ORDEM:</b> BLATTODEA\n<b>FAMÍLIA:</b> ECTOBIIDAE\n<b>SUBFAMÍLIA:</b> SUPELLA LONGIPALPA\n<b>GÊNERO:</b> SUPELLA </span>")
		self.Adictional[14].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: ESSE ANIMAL É ORIGINÁRIO DO CONTINENTE AFRICANO MAS É CONSIDERADO UMA PESTE QUASE COSMOPOLITA. ESSA BARATA É COMUMENTE ENCONTRADA DENTRO DE RESIDÊNCIAS OU PRÓXIMO A ELAS </b> </span>")

		self.label[15].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> PERIPLANETA FULIGINOSA \n<b>NOMES COMUNS:</b> BARATA MARROM FULIGEM OU BANDA MARROM, BANDA CAFÉ\n<b>ORDEM:</b> BLATTODEA\n<b>FAMÍLIA:</b> BLATTIDAE\n<b>SUBFAMÍLIA:</b> BLATTINAE\n<b>GÊNERO:</b> PERIPLANETA </span>")
		self.Adictional[15].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: EMBORA SEJA PARENTE DA BARATA-AMERICANA, A BARATA MARROM FULIGEM É FACILMENTE DESTINGUÍVEL PO SUA COLORAÇÃO MARROM ESCURA. ALÉM DO QUE, AO CONTRÁRIO DA PARATA-AMERICANA, QUE GERALMENTE POSSUI UM TÓRAX DE COR CLARA, A FULIGINOSA APRESENTA UM TOM AMARRONZADO E BRILHANTE NA MESMA REGIAO. </b> </span>")

		self.label[16].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> HETERODERES RUFANGULUS \n<b>NOMES COMUNS:</b> LARVA – ARAME\n<b>ORDEM:</b> COLEOPTERA\n<b>FAMÍLIA:</b> ELATERIDAE\n<b>SUBFAMÍLIA:</b> AGRYPNINAE\n<b>GÊNERO:</b> AGRIOTES </span>")
		self.Adictional[16].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: AS LARVAS POSSUEM HÁBITOS SUBTERRÂNEOS, ATACANDO AS RAÍZES E TUBÉRCULOS DAS PLANTAS.  AS PLANTAS ATACADAS FICAM AMARELADAS, PODENDO MORRER DEVIDO À DESTRUIÇÃO QUE ESTES INSETOS CAUSAM ÀS RAÍZES. AS TOUCEIRAS ATACADAS SÃO FACILMENTE OBSERVADAS NO CAMPO. </b> </span>")

		self.label[17].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> DEOIS FLAVOPICTA \n<b>NOMES COMUNS:</b> CIGARRAS DAS PASTAGENS\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> CERCOPIDAE\n<b>SUBFAMÍLIA:</b> TOMASPIDINAE\n<b>GÊNERO:</b> DEOIS </span>")
		self.Adictional[17].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: CAUSAM IMPORTANTES PREJUÍZOS AS PASTAGENS E LAVOURAS DE MILHO. FOLHAS PICADAS MOSTRAM ÁREAS CLORÓTICAS E COM SINAIS DE NECROSE, O QUE PODE LEVAR A MORTE DA PLANTA. PLANTAS NOVAS SÃO EXTREMAMENTE SENSÍVEIS AO ATAQUE DA PRAGA. </b> </span>")

		self.label[18].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> EUBORELLIA SP \n<b>NOMES COMUNS:</b> TESOURINHA\n<b>ORDEM:</b> DERMAPTERA\n<b>FAMÍLIA:</b> ANISOLABIDIDAE\n<b>SUBFAMÍLIA:</b> ANISOLABIDINAE\n<b>GÊNERO:</b> EUBORELLIA </span>")
		self.Adictional[18].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: DE MODO GERAL, DERMÁPTEROS NÃO SÃO APONTADOS COMO PRAGAS. </b> </span>")

		self.label[19].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> EUSCHISTUS HEROS SP \n<b>NOMES COMUNS:</b> PERCEVEJO DA SOJA OU PERCEVEJO-MARROM-DA-SOJA.\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> PENTATOMIDAE\n<b>SUBFAMÍLIA:</b> PENTATOMINAE\n<b>GÊNERO:</b> EUSCHISTUS </span>")
		self.Adictional[19].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: ESSES INSETOS AFETAM AS CULTURAS DE ALGODÃO, GIRASSOL E SOJA. É CONHECIDO POR SER UMA DAS MAIS AGRESSIVAS PRAGAS DA CULTURA DA SOJA. </b> </span>")

		self.label[20].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> LABIDURA RIPARIA \n<b>NOMES COMUNS:</b> BICHA-CADELA OU TESOURINHA\n<b>ORDEM:</b> DERMAPTERA\n<b>FAMÍLIA:</b> LABIDURIDAE\n<b>SUBFAMÍLIA:</b> LABIDURINAE\n<b>GÊNERO:</b> LABIDURA </span>")
		self.Adictional[20].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: É CONSIDERADA UMA PREDADORA GENERALISTA SE ALIMENTANDO DE UMA VARIEDADE DE INSETOS INCLUSIVE DE OUTROS INSETOS E PRAGAS COMO A BROCA DE CANA. </b> </span>")

		self.label[21].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> LEPTOGLOSSUS STIGMA \n<b>NOMES COMUNS:</b> PERCEVEJO-GAÚCHO OU PERCEVEJO – DAS – FRUTAS.\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> COREIDAE\n<b>SUBFAMÍLIA:</b> COREINAE\n<b>GÊNERO:</b> LEPTOGLOSSUS </span>")
		self.Adictional[21].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: AS CULTURAS AFETADAS SÃO ABÓBORA, CAJU, MILHO, SORGO, ROMÃ, CARAMBOLA, CITROS, GOIABA, MANGA, MARACUJÁ, MELANCIA E PEPINO, PRINCIPALMENTE PELO FATO DE CAUSAR DANOS DIRETOS NO PRODUTO COMERCIAL, QUE SÃO OS FRUTOS. </b> </span>")

		self.label[22].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> MAHANARVA FIMBRIOLATA \n<b>NOMES COMUNS:</b> CIGARRINHA-DA-CANA-DE-AÇÚCAR, BARATINHA, CIGARRINHA-DOS-CANAVIAIS E CIGARRINHA-VERMELHA.\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> CERCOPIDAE\n<b>SUBFAMÍLIA:</b> TOMASPEDINAE\n<b>GÊNERO:</b> MAHANARVA </span>")
		self.Adictional[22].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: ATACA PRINCIPALMENTE AS FOLHAS E AS RAÍZES DA CANA DE AÇÚCAR. CANA-DE-AÇÚCAR, PASTAGENS, TODAS AS CULTURAS COM OCORRÊNCIA DO ALVO BIOLÓGICO. </b> </span>")

		self.label[23].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> NEOMEGALOTOMUS PARVUS \n<b>NOMES COMUNS:</b> PERCEVEJO-FORMIGÃO.\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> ALYDIDAE\n<b>SUBFAMÍLIA:</b> PENTATOMINAE\n<b>GÊNERO:</b> NEOMEGALOTOMUS </span>")
		self.Adictional[23].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: SEMENTE OU GRÃO, CAULE/RAMOS EM LAVOURAS EM GERAL. </b> </span>")

		self.label[24].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>NOME CIENTÍFICO:</b> PIEZODORUS GUILDINII \n<b>NOMES COMUNS:</b> PERCEVEJO-VERDE-PEQUENO-DA-SOJA, PERCEVEJO-VERDE-PEQUENO\n<b>ORDEM:</b> HEMIPTERA\n<b>FAMÍLIA:</b> PENTATOMIDAE\n<b>SUBFAMÍLIA:</b> PENTATOMINAE\n<b>GÊNERO:</b> PIEZODORUS </span>")
		self.Adictional[24].set_markup("<span foreground='#001000' size='x-large' face='Arial'><b>INFORMAÇÕES ADICIONAIS: DANOS: SEMENTE OU GRÃO, CAULE/RAMOS EM LAVOURAS EM GERAL. </b> </span>")

		#ShowAll
		self.Tudo = gtk.Button(label="Todos")

		self.Tudo.set_margin_left(10)
		self.Tudo.set_margin_right(10)
		self.Tudo.set_margin_bottom(10)
		
		self.Tudo.connect("clicked",lambda arg: ListAll(self))
		self.Grid_Menu.attach(self.Tudo,4,4,1,1)

		# 008000    228B22

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
		self.Ordem_combo.set_margin_top(1)
		self.Ordem_combo.set_margin_left(10)
		self.Ordem_combo.set_margin_right(10)
		self.Grid_Menu.attach(self.Ordem_combo, 0, 2,1,1)
		
		#Store das Family's
		self.Family_store = gtk.ListStore(float,str)

		#Family_Combo
		self.Family_combo = gtk.ComboBox.new_with_model_and_entry(self.Family_store)
		self.Family_combo.set_margin_top(1)
		self.Family_combo.set_margin_left(10)
		self.Family_combo.set_margin_right(10)
		self.Grid_Menu.attach(self.Family_combo, 1, 2,1,1)

		#Store das SubFamily's
		self.SubFamily_store = gtk.ListStore(float,str)

		#SubFamily_Combo
		self.SubFamily_combo = gtk.ComboBox.new_with_model_and_entry(self.SubFamily_store)
		self.SubFamily_combo.set_margin_top(1)
		self.SubFamily_combo.set_margin_left(10)
		self.SubFamily_combo.set_margin_right(10)
		self.Grid_Menu.attach(self.SubFamily_combo, 2, 2,1,1)

		#StoreGenero
		self.Genero_store = gtk.ListStore(float,str)

		#Genero_Combo
		self.Genero_combo = gtk.ComboBox.new_with_model_and_entry(self.Genero_store)
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
		self.Grid_Menu.override_background_color(gtk.StateType.NORMAL, Gdk.RGBA(0,139,0,0.5))
		

		self.Nome_Ordem = str()
		self.Nome_Family = str()
		self.Nome_SubFamily = str()
		self.Nome_Genero = str()

					
		self.All()

	def All(self):
		#OrdemStore
		self.Ordem_store.append([1.01, "-"])
		self.Ordem_store.append([1, "HEMIPTERA"])
		self.Ordem_store.append([2, "BLATTODEA"])
		self.Ordem_store.append([3, "COLEOPTERA"])
		self.Ordem_store.append([4, "HYMENOPTERA"])
		self.Ordem_store.append([5, "DIPTERA"])
		self.Ordem_store.append([6, "DERMAPTERA"])

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
		self.Family_store.append([2.7, "BLATTELLIDAE"])
		self.Family_store.append([2.8, "SCARABAEIDAE"])
		self.Family_store.append([2.9, "CURCULIONIDAE"])
		self.Family_store.append([3.0, "APIDAE"])
		self.Family_store.append([3.1, "PSYCHODIDAE"])
		self.Family_store.append([3.2, "ECTOBIIDAE"])
		self.Family_store.append([3.3, "BLATTIDAE"])
		self.Family_store.append([3.4, "ELATERIDAE"])
		self.Family_store.append([3.5, "CERCOPIDAE"])
		self.Family_store.append([3.6, "ANISOLABIDIDAE"])
		self.Family_store.append([3.7, "LABIDURIDAE"])
		self.Family_store.append([3.8, "ALYDIDAE"])
				
		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)

		#SubFamilyStore
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.1, "ORSILLINAE"])
		self.SubFamily_store.append([3.2, "PENTATOMINAE"])
		self.SubFamily_store.append([3.3, "HARPACTORINAE"])
		self.SubFamily_store.append([3.4, "CICADELLINAE"])
		self.SubFamily_store.append([3.5, "COREINAE"])
		self.SubFamily_store.append([3.6, "BLATTELLINAE"])
		self.SubFamily_store.append([3.7, "DYNASTINAE"])
		self.SubFamily_store.append([3.8, "DRYOPHTHORINAE"])
		self.SubFamily_store.append([3.9, "CURCULIONINAE"])
		self.SubFamily_store.append([4.0, "POLYDROSINAE"])
		self.SubFamily_store.append([4.1, "MELIPONÍNEOS"])
		self.SubFamily_store.append([4.2, "ENTIMINAE"])
		self.SubFamily_store.append([4.3, "PSYCHODINAE"])
		self.SubFamily_store.append([4.4, "SUPELLA LONGIPALPA"])
		self.SubFamily_store.append([4.5, "BLATTINAE"])
		self.SubFamily_store.append([4.6, "AGRYPNINAE"])
		self.SubFamily_store.append([4.7, "TOMASPIDINAE"])
		self.SubFamily_store.append([4.8, "ANISOLABIDINAE"])
		self.SubFamily_store.append([4.9, "LABIDURINAE"])
		self.SubFamily_store.append([5.0, "TOMASPEDINAE"])
		self.SubFamily_store.append([5.1, "ANTHOCORINAE"])
		self.SubFamily_store.append([5.2, "PIEZODORUS"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

		#Gênero
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.1, "NYSIUS"])
		self.Genero_store.append([4.2, "BLATELLA"])
		self.Genero_store.append([4.3, "DYNASTES"])
		self.Genero_store.append([4.4, "SPHENOPHORUS"])
		self.Genero_store.append([4.5, "ANTHONOMUS"])
		self.Genero_store.append([4.6, "TERATOPACTUS HELLER"])
		self.Genero_store.append([4.7, "TRIGONA"])
		self.Genero_store.append([4.8, "ARACANTHUS"])
		self.Genero_store.append([4.9, "CLOGMIA"])
		self.Genero_store.append([5.0, "SUPELLA"])
		self.Genero_store.append([5.1, "PERIPLANETA"])
		self.Genero_store.append([5.2, "AGRIOTES"])
		self.Genero_store.append([5.3, "DEOIS"])
		self.Genero_store.append([5.4, "DICHELOPS"])
		self.Genero_store.append([5.5, "EUBORELLIA"])
		self.Genero_store.append([5.6, "EUSCHISTUS"])
		self.Genero_store.append([5.7, "LABIDURA"])
		self.Genero_store.append([5.8, "LEPTOGLOSSUS"])
		self.Genero_store.append([5.9, "MAHANARVA"])
		self.Genero_store.append([6.0, "NEOMEGALOTOMUS"])
		self.Genero_store.append([6.1, "ONCOMETOPIA"])
		self.Genero_store.append([6.2, "ANTHOCORINAE"])

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

			if self.ID == 3:
				self.Family3()

			if self.ID == 4:
				self.Family4()

			if self.ID == 5:
				self.Family5()

			if self.ID == 6:
				self.Family6()

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

			if self.ID_Family == 2.6:
				self.SubFamily20()

			if self.ID_Family == 2.7:
				self.SubFamily6()

			if self.ID_Family == 2.8:
				self.SubFamily7()

			if self.ID_Family == 2.9:
				self.SubFamily8()
			
			if self.ID_Family == 3.0:
				self.SubFamily11()

			if self.ID_Family == 3.1:
				self.SubFamily13()

			if self.ID_Family == 3.2:
				self.SubFamily14()

			if self.ID_Family == 3.3:
				self.SubFamily15()

			if self.ID_Family == 3.4:
				self.SubFamily16()

			if self.ID_Family == 3.5:
				self.SubFamily17()

			if self.ID_Family == 3.6:
				self.SubFamily18()

			if self.ID_Family == 3.7:
				self.SubFamily19()

			if self.ID_Family == 3.8:
				self.SubFamily2()
		
	
	def on_SubFamily_combo(self,SubFamily_combo):
		self.tree_iter_SubFamily = SubFamily_combo.get_active_iter()
		if self.tree_iter_SubFamily != None:
			self.model_Subfamily = SubFamily_combo.get_model()
			self.ID_SF, self.Nome_SubFamily = self.model_Subfamily[self.tree_iter_SubFamily][:2]
			self.ID_SubFamily = float(self.ID_SF) 

			
			if self.ID_SubFamily == 3.1:
				self.Genero1()

			if self.ID_SubFamily == 3.2:
				self.Genero14()

			if self.ID_SubFamily == 3.4:
				self.Genero19()

			if self.ID_SubFamily == 3.5:
				self.Genero17()

			if self.ID_SubFamily == 3.6:
				self.Genero2()

			if self.ID_SubFamily == 3.7:
				self.Genero3()

			if self.ID_SubFamily == 3.8:
				self.Genero4()

			if self.ID_SubFamily == 3.9:
				self.Genero5()
		
			if self.ID_SubFamily == 4.0:
				self.Genero6()

			if self.ID_SubFamily == 4.1:
				self.Genero7()
		
			if self.ID_SubFamily == 4.2:
				self.Genero8()

			if self.ID_SubFamily == 4.3:
				self.Genero9()

			if self.ID_SubFamily == 4.4:
				self.Genero10()

			if self.ID_SubFamily == 4.5:
				self.Genero11()

			if self.ID_SubFamily == 4.6:
				self.Genero12()

			if self.ID_SubFamily == 4.7:
				self.Genero13()

			if self.ID_SubFamily == 4.8:
				self.Genero15()

			if self.ID_SubFamily == 4.9:
				self.Genero16()

			if self.ID_SubFamily == 5.0:
				self.Genero18()
		
			if self.ID_SubFamily == 5.1:
				self.Genero20()


	def on_Genero_combo(self,Genero_combo):
		self.tree_iter_Genero = Genero_combo.get_active_iter()
		if self.tree_iter_Genero != None:
			self.model_Genero = Genero_combo.get_model()
			self.ID_G, self.Nome_Genero = self.model_Genero[self.tree_iter_Genero][:2]
			self.ID_Genero = float(self.ID_G) 

 #------------------------------------------DEF'S ORGANIZAÇÃO--------------------------------------
	#Ordem: HEMIPTERA	
	def Family1(self):
		self.Family_store.clear()
		self.Family_store.append([2.02, "-"])
		self.Family_store.append([2.1, "LYGAEIDAE"])
		self.Family_store.append([2.2, "PENTATOMIDAE"])
		self.Family_store.append([2.3, "REDUVIIDAE"])
		self.Family_store.append([2.4, "CICADELLIDAE"])
		self.Family_store.append([2.5, "COREIDAE"])
		self.Family_store.append([2.6, "CANTHOCORIDAE"])
		self.Family_store.append([3.5, "CERCOPIDAE"])
		self.Family_store.append([3.8, "ALYDIDAE"])

		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)

	#Ordem: BLATTODEA
	def Family2(self):
		self.Family_store.clear()
		self.Family_store.append([2.02, "-"])
		self.Family_store.append([2.7, "BLATTELLIDAE"])
		self.Family_store.append([3.2, "ECTOBIIDAE"])
		self.Family_store.append([3.3, "BLATTIDAE"])

		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)

	#Ordem: CLEOPTERA
	def Family3(self):
		self.Family_store.clear()
		self.Family_store.append([2.02, "-"])
		self.Family_store.append([2.8, "SCARABAEIDAE"])
		self.Family_store.append([2.9, "CURCULIONIDAE"])
		self.Family_store.append([3.4, "ELATERIDAE"])
		

		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)

	#Ordem: HYMENOPTERA
	def Family4(self):
		self.Family_store.clear()
		self.Family_store.append([2.02, "-"])
		self.Family_store.append([3.0, "APIDAE"])

		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)
	
	#Ordem: DIPTERA
	def Family5(self):
		self.Family_store.clear()
		self.Family_store.append([2.02, "-"])
		self.Family_store.append([3.1, "PSYCHODIDAE"])

		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)

	#Ordem: DERMAPTERA
	def Family6(self):
		self.Family_store.clear()
		self.Family_store.append([2.02, "-"])
		self.Family_store.append([3.6, "ANISOLABIDIDAE"])
		self.Family_store.append([3.7, "LABIDURIDAE"])

		self.Family_combo.set_entry_text_column(1)
		self.Family_combo.connect("changed", self.on_Family_combo)
	

		#SUBFAMILYS
		#1 a 5 Ordem: HEMIPTERA

	#Familia: LYGAEIDAE
	def SubFamily1(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.1, "ORSILLINAE"])

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	#Familia: PENTATOMIDAE
	def SubFamily2(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.2, "PENTATOMINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	#Familia: REDUVIIDAE
	def SubFamily3(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.3, "HARPACTORINAE"])
		

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	#Familia: CICADELLIDAE
	def SubFamily4(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.4, "CICADELLINAE"])
		

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	#Familia: COREIDAE
	def SubFamily5(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.5, "COREINAE"])	

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

#-------------------------------------------------------------------------------------------


	#Ordem: BLATTODEA Familia: BLATTELLIDAE
	def SubFamily6(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.6, "BLATTELLINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	
	#Ordem: COLEOPTERA Familia: SCARABAEIDAE
	def SubFamily7(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.7, "DYNASTINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	
	#Ordem: COLEOPTERA Familia: CURCULIONIDAE
	def SubFamily8(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([3.8, "DRYOPHTHORINAE"])
		self.SubFamily_store.append([3.9, "CURCULIONINAE"])
		self.SubFamily_store.append([4.0, "POLYDROSINAE"])
		self.SubFamily_store.append([4.2, "ENTIMINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
		
	#Ordem: HYMENOPTERA Familia: APIDAE
	def SubFamily11(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([4.1, "MELIPONÍNEOS"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	
	#Ordem: DIPTERA Familia: PSYCHODIDAE
	def SubFamily13(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([4.3, "PSYCHODINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	
	#Ordem: BLATTODEA Familia: ECTOBIIDAE
	def SubFamily14(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([4.4, "SUPELLA LONGIPALPA"])

		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	
	#Ordem: BLATTODEA Familia: BLATTIDAE
	def SubFamily15(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([4.5, "BLATTINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	
	#Ordem: COLEOPTERA Familia: ELATERIDAE
	def SubFamily16(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([4.6, "AGRYPNINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

	#Ordem: HEMIPTERA Familia: CERCOPIDAE
	def SubFamily17(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([4.7, "TOMASPIDINAE"])
		self.SubFamily_store.append([5.0, "TOMASPEDINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

	#Ordem: DERMAPTERA Familia: ANISOLABIDIDAE
	def SubFamily18(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([4.8, "ANISOLABIDINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

	#Ordem: DERMAPTERA Familia: LABIDURIDAE
	def SubFamily19(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([4.9, "LABIDURINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)

	#Ordem: HEMIPTERA Familia: CANTHOCORIDAE
	def SubFamily20(self):
		self.SubFamily_store.clear()
		self.SubFamily_store.append([3.01, "-"])
		self.SubFamily_store.append([5.1, "ANTHOCORINAE"])
		
		self.SubFamily_combo.set_entry_text_column(1)
		self.SubFamily_combo.connect("changed", self.on_SubFamily_combo)
	

		#GENEROS


	#ORDEM      FAMILIA    SUBFAMILIA
	#HEMIPTERA  LYGAEIDAE  ORSILLINAE
	def Genero1(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.1, "NYSIUS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#BLATTODEA  BLATTELLIDAE  BLATTELLINAE  
	def Genero2(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.2, "BLATELLA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#COLEOPTERA  SCARABAEIDAE  DYNASTINAE
	def Genero3(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.3, "DYNASTES"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#COLEOPTERA  CURCULIONIDAE  DRYOPHTHORINAE
	def Genero4(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.4, "SPHENOPHORUS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#COLEOPTERA  CURCULIONIDAE  CURCULIONINAE
	def Genero5(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.5, "ANTHONOMUS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#COLEOPTERA  CURCULIONIDAE  POLYDROSINAE
	def Genero6(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.6, "	TERATOPACTUS HELLER"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#HYMENOPTERA  APIDAE  MELIPONÍNEOS
	def Genero7(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.7, "TRIGONA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#COLEOPTERA  CURCULIONIDAE  ENTIMINAE
	def Genero8(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.8, "ARACANTHUS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#DIPTERA  PSYCHODIDAE  PSYCHODINAE
	def Genero9(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([4.9, "CLOGMIA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#BLATTODEA  ECTOBIIDAE SUPELLA LONGIPALPA 
	def Genero10(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.0, "SUPELLA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#BLATTODEA  BLATTIDAE  BLATTINAE
	def Genero11(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.1, "PERIPLANETA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
	
	#COLEOPTERA  ELATERIDAE  AGRYPNINAE
	def Genero12(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.2, "AGRIOTES"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)

	#HEMIPTERA  CERCOPIDAE  TOMASPIDINAE
	def Genero13(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.3, "DEOIS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)

	#HEMIPTERA  PENTATOMIDAE  PENTATOMINAE
	def Genero14(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.4, "DICHELOPS"])
		self.Genero_store.append([5.6, "EUSCHISTUS"])
		self.Genero_store.append([6.0, "NEOMEGALOTOMUS"])
		self.Genero_store.append([6.2, "PIEZODORUS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)

	#DERMAPTERA  ANISOLABIDIDAE  ANISOLABIDINAE
	def Genero15(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.5, "EUBORELLIA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)

	#DERMAPTERA LABIDURIDAE LABIDURINAE
	def Genero16(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.7, "LABIDURA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)

	#HEMIPTERA COREIDAE COREINAE
	def Genero17(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.8, "LEPTOGLOSSUS"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)

	#HEMIPTERA COREIDAE TOMASPEDINAE
	def Genero18(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([5.9, "MAHANARVA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)

	#HEMIPTERA CICADELLIDAE CICADELLINAE
	def Genero19(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([6.1, "ONCOMETOPIA"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)


	def Genero20(self):
		self.Genero_store.clear()
		self.Genero_store.append([4.01, "-"])
		self.Genero_store.append([6.2, "ANTHOCORINAE"])

		self.Genero_combo.set_entry_text_column(1)
		self.Genero_combo.connect("changed", self.on_Genero_combo)
