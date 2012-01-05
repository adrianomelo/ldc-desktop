# -*- coding: utf-8 -*-

class DiagResUsbstorage(object):
    """Classe básica da biblioteca de usb storage que define os resultados da parte de diagnóstico."""
    
    __diag_dict = None
    
    __part_check = None
    __mount_test = None
    __fsck_test = None
    
    def __init__(self, diag_dict):
        """Construtor        
        Parâmetro:
        diag_dict -- dicionário com as informações da etapa de diagnóstico
        """
        self.__diag_dict = diag_dict
        
        self.__part_check = diag_dict['info']['partition_check']['id']
        self.__mount_test = diag_dict['info']['mount_test']['id']
        self.__fsck_test = diag_dict['info']['fsck_test']['id']


    def getPart_check(self):
        """Retorna o 1 ou 0 dependendo do resultado do teste."""
        return self.__part_check

    def getMount_test(self):
        """Retorna o 1 ou 0 dependendo do resultado do teste."""
        return self.__mount_test

    def getFsck_test(self):
        """Retorna o 1 ou 0 dependendo do resultado do teste."""
        return self.__fsck_test
    
    part_check = property(getPart_check, None, None, None)
    mount_test = property(getMount_test, None, None, None)
    fsck_test = property(getFsck_test, None, None, None)
    
    def __str__(self):
        """Retorna uma string formatada contendo todas as informações do diagnóstico de usb storage."""
        return "Partition check: %d\nMount test: %d\nFsck test = %d" % (self.part_check, self.mount_test, self.fsck_test)

    def getReportDiag(self):
        """Método que retorna as informações no formato de tuplas para o pdf"""
        diagList = []
        mountMsg = u"O dispositivo não apresentou problema na montagem." 
        partMsg = u'O particionamento foi identificado corretamente.'
        fsckMsg = u'Não foi encontrado nenhum erro no dispositivo.'
        
        if not self.mount_test:
            mountMsg = u'O dispositivo apresentou problema na montagem.'
        if not self.part_check:
            partMsg = u'O particionamento não foi identificado corretamente.'
        if not self.fsck_test:
            fsckMsg = u'A verificação de erro não foi realizada com sucesso.'
            
        diagList.append(('Teste de montagem', mountMsg))
        diagList.append(('Teste de particionamento', partMsg))
        diagList.append((u'Teste de verificação de erro', fsckMsg))
        return diagList

"""
{
    'status': -1, 
    'info': 
    {
        'partition_check': {'id': 1, 'value': 'NULL', 'description': 'Partition Check'}, 
        'mount_test': {'id': 1, 'value': 'NULL', 'description': 'Mount Test'}, 
        'fsck_test': {'id': 1, 'value': 'NULL', 'description': 'Fsck Test'}
    }, 
    'libName': 'usbstorage'}
"""