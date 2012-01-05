# -*- coding: utf-8 -*-
import os, sys
from PyQt4 import QtCore, QtGui
from gui.pyui.LDC_Info_pyui import Ui_LDC_Info


# Usar a classe LDC_Info,
# setar titulo com setTitle()
# e editar apenas o campo frame.
class LDC_Info(QtGui.QGroupBox, Ui_LDC_Info):
    """
    Classe responsável por definir o padrão das unidades de interface gráfica dos resultados da execução de cada plugin.
    Define a classe básica de interface que será acoplada na tela de exibição de resultados.
    Todos os módulos de interface de exibição de resultados devem herdas as propriedades desta classe.
    """

    def __init__(self):
        """
        Construtor da classe.
        """
        QtGui.QGroupBox.__init__(self)
        Ui_LDC_Info.__init__(self)
        self.setupUi(self)

    def _check_invalid_values(self, value):
        """
        Verifica se há valores inválidos ou irrelevantes em uma lista.
        """
        ret = ""

        if (value):
            if (value != "Other" and value != "NULL" and value != "Unknown" and value != 'Not' and value != 'Not Applicable' and value != '-1'):
                ret = value

        return ret

    def _check_invalid_list(self, list, charJoin = ', '):
        """
        Verifica se a lista é inválida.
        """
        ret = ""

        if (list):
            ret = []

            for i in list:
                item = self._check_invalid_values(i)

                if (item):
                    ret.append(item)

            if (not ret):
                ret = ""

        return charJoin.join(ret)


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    ldc_info = LDC_Info()

    ldc_info.show()
    sys.exit(app.exec_())
