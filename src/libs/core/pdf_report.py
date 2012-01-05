# -*- coding: latin-1 -*-

import datetime, os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, ParagraphAndImage
from reportlab.rl_config import defaultPageSize

from libs.core.commands_utils import exec_command

_PDF_FOLDER = '/var/tmp/'

class PdfReport(object):
    """Classe que gera o relat�rio em pdf a partir dos resultados dos testes"""

    def __init__(self, logger):
        """Construtor

        Par�metro:
        logger -- lista de dicion�rios contendo as informa��es dos testes. O formato do dicion�rio �
                  { 'category': 'nome da categoria',
                    'name': 'nome do dispositivo',
                    'icon': 'nome do arquivo da imagem do �cone',
                    'info': [('Modelo', 'x'), ..., ('Vendor', 'y')] -- lista de tuplas contendo o resultado de info(),
                    'compat': (True/False, 'msg') -- resultado do teste de compatibilidade,
                    'diag': [('Dispositivo', 'x'), ..., ('Tamanho', 'y')] -- lista de tuplas contendo o resultado de diag()
                  }
        """
        self._logger = logger

        self._filename = _PDF_FOLDER + self._composeFilename() #nome do arquivo a ser gerado

        self._fontname = 'Helvetica'
        self._fontnameLarge = 'Helvetica-Bold'
        self._fontsize = 10
        self._fontsizeLarge = 16
        self._doc_title = u'Relat�rio do Librix Diagnostic Center'
        self._logoDim = ( 6.09*cm, 1.35*cm )
        self._logo = "gui/resources/logo_azul.jpg"
        self._watermarkDim = (446, 570)
        self._watermark = "gui/resources/pinguimx.jpg"
        self._pageHeight = defaultPageSize[1]
        self._pageWidth = defaultPageSize[0]

        self._styles = self._createStyles() #os estilos que ser�o usados no pdf

        self._categories = [] #lista com as categorias
        self._icons = {} #dicion�rio contendo a refer�ncia para a Imagem dos �cones das cetegorias
        for device in self._logger:
            if not device['category'] in self._categories:
                self._categories.append(device['category'])
                self._icons.__setitem__(device['category'], Image("gui/resources/%s.jpg"%device['icon'].split('.')[0], 25, 25))

        #lista contendo as strings que remover�o um tupla, n�o ser�o mostrados no relat�rio.
        self._removeTuples = ['', 'UNKNOWN', 'OTHER', None, 'NULL', '-1', 'NONE']

        #lista contendo os programas que podem ser usados para abrir o pdf
        self._pdfViewers = ['okular', 'evince', 'kpdf', 'xpdf']


    def dump(self):
        """M�todo que gera o relat�rio e retorna o nome do arquivo criado"""
        doc = SimpleDocTemplate(self._filename, topMargin=1.5*inch)
        self.story = [Spacer(0.5,0.5*inch)]

        for category in self._categories:
            #imprime as informa��es da categoria
            text = Paragraph(category, self._styles['category'])
            iaf = ParagraphAndImage(text, self._icons[category], side='left', xpad=5)
            self.story.append(iaf)

            #imimir as informa��es dos dispositivos da categoria
            for device in self._logger:
                if device['category'] == category:
                    #nome do dispositivo
                    text = Paragraph(device['name'], self._styles['device'])
                    self.story.append(text)

                    #imprimir as informa��es do dispositivo
                    if device.has_key('info') and device['info']:
                        for infoItem in device['info']:
                            self._printInfoItem(infoItem, self._styles['normal'])

                    #imprimir as informa��es do teste de compatibilidade e do diagn�stico
                    if device.has_key('compat'):
                        if device['compat'][0]: # se o compatibilidade for 'True' imprime antes as informa��es de diagn�stico
                            self._printDiag(device, self._styles['normal'])
                            self._printCompat(device['compat'], self._styles['normal'])
                        else: #ordem inversa
                            self._printCompat(device['compat'], self._styles['normal'])
                            self._printDiag(device, self._styles['normal'])
                    self.story.append(Spacer(0.2,0.2*inch))

        doc.build(self.story, onFirstPage=self._firstPage, onLaterPages=self._latterPages)
        return self._filename

    def showReport(self, pdffile):
        """M�todo que abre o kpdf com o arquivo passado como par�metro"""
        pdfViewer = self._getPdfViewer()
        os.system("%s %s 2>> /dev/null &"%(pdfViewer, pdffile))


    def _getPdfViewer(self):
        """M�todo que ir[a retornar o programa de pdf que ser� usado para visualizar o relat�rio"""
        result = ''
        for viewer in self._pdfViewers:
            i, o_str, e_str, retCode = exec_command('which %s'%viewer)
            if o_str and not e_str:
                result = viewer
                break
        return result

    def _printDiag(self, device, style):
        """M�todo auxiliar que chama o metodo '_printInfoItem' para todas as informa��es do diagn�tico."""
        if device.has_key('diag') and device['diag']:
            for infoItem in device['diag']:
                self._printInfoItem(infoItem, style)

    def _printCompat(self, compat, style):
        """M�todo auxiliar para imprimir as informa��es de compatibilidade"""
        text = Paragraph('<b>Compatibilidade</b>: %s'%compat[1], style)
        self.story.append(text)

    def _printInfoItem(self, infoItem, style):
        """M�todo que imprime todas as tuplas de informa��es."""
        if isinstance(infoItem[1], list): #Se � um subitem
            desc = Paragraph('<b>' + infoItem[0] + '</b>', style) #a primeira parte em negrito
            self.story.append(desc)
            for infoSubItem in infoItem[1]:
                self._printInfoItem(infoSubItem, self._styles['subitem'])
        else:
            if (not (infoItem[1].upper() in self._removeTuples)) and  (not ('-1' in infoItem[1])):
                text = '<b>' + self._toUnicode(infoItem[0]) + '</b>: ' + self._toUnicode(infoItem[1])
                info = Paragraph(text, style)
                self.story.append(info)

    def _toUnicode(self, text):
        """M�todo que converte texto para unicode e caso o caracter n�o possa ser reconhecido ser� substitu�do por '-'"""
        result = ''
        try:
            result = unicode(text)
        except UnicodeError, ex:
            listText = list(text)
            listText[ex[2]] = '-' #ex � uma tupla com as informa��es da exce��o e o elemento '2' indica o local do caracter inv�lido
            result = unicode(''.join(listText))
        return result

    def _firstPage(self, canvas, doc):
        """M�todo que imprime as informa��es do layout da primeira p�gina"""
        canvas.saveState()
        canvas.setFont(self._fontnameLarge, self._fontsizeLarge)
        canvas.drawCentredString(self._pageWidth/2.0, self._pageHeight - 130, self._doc_title)
        self._layoutDoc(canvas, doc)
        canvas.restoreState()

    def _latterPages(self, canvas, doc):
        """M�todo que imprime as informa��es do layout de todas as p�ginas menos a primeira"""
        canvas.saveState()
        self._layoutDoc(canvas, doc)
        canvas.restoreState()

    def _layoutDoc(self, canvas, doc):
        """M�todo auxiliar que imprime as informa��es de layout de todas as p�ginas"""
        canvas.drawImage(self._logo, self._pageWidth - self._logoDim[0]- 90, self._pageHeight - 3.2*cm, self._logoDim[0], self._logoDim[1])
        canvas.drawImage(self._watermark, self._pageWidth - self._watermarkDim[0], 0, self._watermarkDim[0], self._watermarkDim[1])
        canvas.setFont(self._fontname, self._fontsize)
        canvas.drawString(inch, 0.75 * inch, u"P�gina %d / %s" % (doc.page, self._filename.split('/')[-1]))

    def _composeFilename(self):
        """M�todo que cria o nome do arquivo pdf baseado na data e hora"""
        today = datetime.datetime.now()
        date = today.strftime('%d%m%Y')
        time = today.strftime('%H%M%S')
        return 'ldc' + '-' + date + '-' + time + '.pdf'

    def _createStyles(self):
        """M�todo que cria um dicion�rio de estilos que ser�o utilizados para imprimir as informa��es"""
        stylesDict = {}
        styles = getSampleStyleSheet()

        style = styles["Normal"]
        style.fontName = 'Helvetica'
        style.leftIndent = 30
        style.spaceAfter = 2
        stylesDict.__setitem__('normal',style)

        styles = getSampleStyleSheet()
        stylesub = styles["Normal"]
        stylesub.fontName = 'Helvetica'
        stylesub.leftIndent = 45
        stylesub.spaceAfter = 2
        stylesDict.__setitem__('subitem',stylesub)

        styleh2 = styles['Heading2']
        styleh2.fontName = 'Helvetica-Bold'
        styleh2.textColor = 'grey'
        styleh2.spaceAfter = 2
        stylesDict.__setitem__('category',styleh2)

        styleh3 = styles['Heading3']
        styleh3.leftIndent = 15
        styleh3.fontName = 'Helvetica-Bold'
        styleh3.spaceAfter = 2
        stylesDict.__setitem__('device',styleh3)

        return stylesDict
