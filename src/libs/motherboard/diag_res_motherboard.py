# -*- coding: latin-1 -*-

class DiagResMotherboard:
    """Classe basica da biblioteca que define os resultados da parte de diagnostico."""
    __msg = None

    def __init__(self, diag_dict):
        """Construtor

        Parametro:
        diag_dict -- dicionario com as informacoes da etapa de diagnostico
        """
        self.__msg = u'Tente atualizar o arquivo de defini��es pciids.'

    def getMsg(self):
        """Retorna mensagem indicando status d o diagnostico."""
        return self.__msg

    msg = property(getMsg, None, None, None)

    def __str__(self):
        """Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
        return "Sugestion: %s" % (self.msg)

    def getReportDiag(self):
        """M�todo que retorna as informa��es no formato de tuplas para o pdf"""
        diagList = []
        diagList.append((u'Sugest�o', self.msg))
        return diagList