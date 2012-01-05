# -*- coding: utf-8 -*-

import ldc_resources_rc

from PyQt4 import QtCore, QtGui
from gui.pyui.LDC_Result_Frame_pyui import Ui_LDC_Result_Frame
from gui.pyui.LDC_ResultList_Widget_pyui import Ui_LDC_ResultList_Widget
from gui.pyui.LDC_Button_pyui import Ui_LDC_Button

class LDC_Result_Frame(QtGui.QFrame, Ui_LDC_Result_Frame):
    """
    Classe que define a estrutura e funções básicas da tela de exibição de resultados.
    """

    def __init__(self):
        """
        Construtor da classe.
        """
        QtGui.QFrame.__init__(self)
        Ui_LDC_Result_Frame.__init__(self)
        self.setupUi(self)
        self.listed_categories = []
        self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())
        #self.pushButton.hide()

    def addResult(self, test_name="test", test_category="", test_result_frame=None, icon=""):
        """
        Adiciona a unidade de interface gráfica(test_result_frame) que contém o resultado sob a categoria(test_category) na tela de exibição de resultados.
        Se a categoria não existe, cria uma nova categoria com o nome test_category e o ícone definido em icon.
        """
        category_exists = False
        for category in self.listed_categories:
            if category[1] == test_category:
                category_exists = True
                resultlist = self.stackedWidget.widget(category[0])
                resultlist.addResult(test_result_frame)

        if not category_exists:
            self.__addCategory(test_category, icon)
            self.addResult(test_name, test_category, test_result_frame)

    def __addCategory(self, test_category="", icon=""):
        """
        Cria uma nova categoria na tela de resultados.
        """
        index = self.stackedWidget.currentIndex()
        position = self.verticalLayout.count() - 1

        button = LDC_PushButton(position, test_category)
        button.setLDCIcon(icon)
        page = LDC_ResultList_Widget()
        page.setAttribute(QtCore.Qt.WA_NoSystemBackground)

        self.listed_categories.append((position, test_category))
        self.verticalLayout.insertWidget(position, button)
        self.stackedWidget.insertWidget(position, page)

        QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), button.LDC_clicked)
        QtCore.QObject.connect(button, QtCore.SIGNAL("LDC_Clicked(PyQt_PyObject)"), self.__changeResultFrame)

    def __changeResultFrame(self, name):
        """
        Quando um botão de categoria é clicado, um sinal é emitido e esta função é chamada
        para tornar visíveis os resultados dos testes referentes à categoria clicada.
        """
        self.stackedWidget.setCurrentIndex(name[0])


class LDC_PushButton(QtGui.QPushButton):
    """
    Reimplementação de QPushButton para definir funções de uso específico do LDC como setLDCIcon() e LDC_clicked().
    """
    position = -1

    def __init__(self, position, *args):
        """
        Construtor da classe.
        """
        apply(QtGui.QPushButton.__init__, (self,) + args)
        self.position = position
        self.setFixedSize(183, 44)
        self.setStyleSheet("background-image: url(:/ldc_button_bckg/ldc_button.png);")

    def setLDCIcon(self, icon):
        """
        Função que define o ícone a ser exibido no botão.
        """
        try:
            icon = QtGui.QIcon("gui/resources/" + icon)
            self.setIconSize(QtCore.QSize(30,30))
            self.setIcon(icon)
            self.setFlat(True)
        except:
            icon = QtGui.QIcon("gui/resources/ldc_mainwindow_icon.png")
            self.setIconSize(QtCore.QSize(30,30))
            self.setIcon(icon)
            self.setFlat(True)

    def LDC_clicked(self):
        """
        Emite um sinal indicando que o botão foi clicado e
        passando as informações de posição e nome do botão.
        """
        self.emit(QtCore.SIGNAL("LDC_Clicked(PyQt_PyObject)"), [self.position, self.text()])

class LDC_ResultList_Widget(QtGui.QFrame, Ui_LDC_ResultList_Widget):
    """
    Classe usada para agrupar itens de interface gráfica oriundos dos resultados dos testes.
    Cada categoria tem um objeto deste tipo para armazenar os resultados de seus testes.
    """

    def __init__(self):
        """
        Construtor da classe.
        """
        QtGui.QFrame.__init__(self)
        Ui_LDC_ResultList_Widget.__init__(self)
        self.setupUi(self)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalWidget = QtGui.QWidget()
        self.verticalWidget.setLayout(self.verticalLayout)
        self.verticalLayout.insertStretch(-1)
        self.scrollArea.setWidget(self.verticalWidget)

    def addResult(self, grouped_data):
        """
        Insere a unidade de interface gráfica na lista.
        """
        self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, grouped_data)

class DeviceNotFound(QtGui.QGroupBox):
    """
    Classe usada para indicar a inexistência de um dispositivo.
    Quando o usuário seleciona um dispositivo para ser testado, mas este não existe,
    esta classe é usada no lugar do que seria o resultados dos testes sobre esse dispositivo.
    """

    def __init__(self, name):
        QtGui.QGroupBox.__init__(self)
        self.setTitle(name)
        self.setStyleSheet("color: rgb(15, 82, 2);")
        lineEdit = QtGui.QLineEdit(self)
        lineEdit.setFrame(False)
        lineEdit.setText("Nenhum dispositivo deste tipo foi encontrado.")
        lineEdit.setStyleSheet("""background-image: url(:/ldc_white_bckg/ldc_white_bckg.png);\n color: rgb(0, 0, 0);""")
        verticalLayout = QtGui.QVBoxLayout()
        verticalLayout.addWidget(lineEdit)
        self.setLayout(verticalLayout)

