# -*- coding: utf-8 -*-

"""
    RQF10.B : Compatibilidade – Montar o dispositivo, escrever um arquivo no dispositivo, ler o mesmo arquivo e compara–lo com o arquivo original. Finalmente, remover o arquivo do dispositivo.
"""
import os, hashlib, random
from libs.core.compat_dev import CompatDev
from libs.core.commands_utils import exec_command

class CompatUsbstorage(CompatDev):
    """Estende a classe 'CompatDev'.
    Classe que implementa o teste de compatibilidade do armazenamneto usb.
    """

    _mount_path = '/mnt/tmp' #Local padrão para montagem
    _hd_path = '/tmp' #Local padrão para salvar o arquivo no HD
    _file_name = 'test_file.tmp' #Nome do arquivo usado no teste.

    def __init__(self, parent):
        """Construtor que chama a classe base 'CompatDev'."""
        CompatDev.__init__(self, parent)

    def compat(self, info_list):
        """Executa o teste de compatibilidade como definido na RFQ10.B.'

        Parâmetro:
        info_list -- Lista contendo as informações detectadas para o dispositivo (lista de 'InfoResUsbstorage')

        Retorna uma lista contendo o resultado do teste e uma string de mensagem para cada dispositivo.
        """
        self._compat_res = None
        self._compat_res = []

        if (info_list):
            for info in info_list:
                if (info.device_file):
                    result_list = []
                    if info.partition_list:
                        for part in info.partition_list:
                            self._umount(info.device_file, part.id)
                            if (self._mount(info.device_file, part.id)):
                                if (self._cp_test()):
                                    if(self._umount(info.device_file, part.id)):
                                       result_list.append((True, ''))
                                    else:
                                        result_list.append((False, 'Erro na desmontagem.'))
                                else:
                                    result_list.append((False, u'Erro no teste de cópia.'))
                            else:
                                result_list.append((False, 'Erro na montagem.'))
                            self._update_final_result(result_list, part.id)
                    else:
                        self._compat_res.append((False, u'Não foi reconhecida a partição do dispositivo.'))

                else:
                    self._compat_res.append((False, 'Dispositivo incorreto.'))
        else:
            self._compat_res.append((False, u'Não foi detectado nenhum dispositivo de armazenamento usb.'))

    def _update_final_result(self, result_list, part):
        """Atualiza todos os resultados das partições em uma única resposta e adiciona a variável '_compat_res'.

        Parâmetro:
        result_list -- Lista de tuplas no formato (True, '') que contém o resultado do teste para cada partição
        part -- Lista das partições testadas
        """
        result_final = True
        msg = u"Dispositivo de armazenamento compatível com o Librix."
        for result in result_list:
            if not result[0]:
                result_final = False
                if result[1]:
                    msg = msg + u" Partição %s: %s\n"%(part, result[1])
        self._compat_res.append((result_final, msg))

    def _umount(self, device_file, part):
        """Desmonta o dispositivo passado como parâmetro.
        Retorna se o comando foi executado com sucesso

        Parâmetro:
        device_file -- string que determina o device file do dispositivo
        part -- string que indica o número da partiçã a ser desmontada
        """
        result = True
        i, o_str, e_str, ret_code = exec_command('umount %s%s'%(device_file, part))
        if e_str:
           result =  False
        return result

    def _mount(self, device_file, part):
        """Monta o dispositivo passado como parâmetro.
        Retorna se o comando foi executado com sucesso

        Parâmetro:
        device_file -- string que determina o device file do dispositivo
        part -- string que indica o número da partiçã a ser desmontada
        """
        result = True
        i, o_str, e_str, ret_code = exec_command('mkdir %s'%self._mount_path)
        i, o_str, e_str, ret_code = exec_command('mount %s%s %s'%(device_file, part, self._mount_path))
        if e_str:
           result =  False
        return result

    def _cp_test(self):
        """Copia o arquivo de teste para o dispositivo e depois dele para o HD e compara o checksum dos dois.
        Retorna se o teste de cópia foi executado com sucesso.
        """
        hd_path_file = self._hd_path+'/'+self._file_name
        mount_path_file = self._mount_path + '/' + self._file_name
        result = False
        check_sum = self._gen_test_file()
        i, o_str, e_str, ret_code = exec_command('cp %s %s'%(hd_path_file, mount_path_file))
        if not e_str:
            os.remove(hd_path_file)
            i, o_str, e_str, ret_code = exec_command('mv %s %s'%(mount_path_file, hd_path_file))
            if not e_str:
                new_check_sum = self._get_checksum()
        if check_sum == new_check_sum:
            result = True
        return result

    def _gen_test_file(self, range_num=1000000):
        """Gerá um arquivo de teste aleatório com o nome '_file_name' e salva ele em '_hd_path'.
        Retorna o checksum do arquivo criado.

        Parâmetro:
        range_num -- o range dos números aleatórios inseridos no arquivo (o valor padrão é 1000000).
        """
        file_path_name = self._hd_path + '/' + self._file_name
        try:
            os.remove(file_path_name)
        except OSError: #Não existia o arquivo
            pass
        #Gerando um arquivo.
        test_file = open(file_path_name, 'w')
        rand = int(random.random()*range_num)
        test_file.write(str(range(rand, rand + range_num)))
        test_file.close()
        return self._get_checksum()

    def _get_checksum(self):
        """calcula o checksum do arquivo com o nome '_file_name' salvo em '_hd_path'.
        Retorna o checksum do arquivo.
        """
        file_path = self._hd_path + '/' + self._file_name
        file = open( file_path, 'r' )
        content_of_file = file.read()
        file.close()
        md5obj = hashlib.md5( content_of_file )
        return md5obj.digest()


# Testing...

def main(argv):
    """Cria um objeto da classe e chama o 'runTest()' definido em 'CompatDev'"""
    test = CompatUsbstorage()
    test.runTest(libs.usbstorage.diag_usbstorege.DiagUsbstorage)

import sys
if __name__ == "__main__":
    main(sys.argv)
