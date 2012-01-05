#ifndef LDC_CORE
#define LDC_CORE

#include <errno.h>

#include <hd.h>

#include "ldc_types.h"
#include "dmidecode_parsing.h"
#include "ldc_log.h"

/*
 * @brief Funcao definida por conveniencia, para evitar a repeticao do codigo de inicializacao
 * das estruturas da libhd.
 *
 * @return Estrutura com as informacoes obtidas da libhd.
 */
hd_data_t * new_hd_data_t ();

/*
 * @brief Funcao definida por conveniencia, para evitar a repeticao do codigo de remocao
 * das estruturas da libhd da memoria.
 *
 * @param hd_data Estrutura a ser removida da memoria.
 * @param hd Estrutura a ser removida da memoria.
 */
void free_hd_structs (hd_data_t * hd_data, hd_t * hd);

/*
 * @brief Funcao definida por conveniencia, para evitar a repeticao de codigo. Esta funcao
 * faz uma chamada a metodos da libhd, passando parametros especificados e repassa os resultados
 * desta chamada a uma outra funcao, tambem especificada.
 *
 * @param log Ponteiro para a estrutura de log onde será inserido a nova tupla.
 * @param type Parametro a ser passado para a funcao hd_list da libhd, definindo o tipo de dispositivo desejado.
 * @param type_process Funcao que recebera cada um dos resultado da chamada a hd_list.
 *
 * @return Estrutura informativa, com os resultados finais.
 */
ldc_info_t * exec_hwinfo_info (ldc_info_t * log, hd_hw_item_t type, ldc_info_t * (* type_process)(ldc_info_t *, hd_t*));

/*
 * @brief Funcao definida por conveniencia, para evitar a repeticao de codigo. Esta funcao
 * faz uma chamada a metodos da libhd, passando parametros especificados e repassa os resultados
 * desta chamada a uma outra funcao, tambem especificada. Esta funcao permite excluir alguns tipos
 * de dispositivos, do resultado final.
 *
 * @param log Indica se sera gerado um log ou nao.
 * @param type Parametro a ser passado para a funcao hd_list da libhd, definindo o tipo de dispositivo desejado.
 * @param undesired_type Parametro a ser passado para a funcao hd_list da libhd, definindo o tipo de dispositivo indesejado.
 * @param type_process Funcao que recebera cada um dos resultado da chamada a hd_list.
 *
 * @return Estrutura informativa, com os resultados finais.
 */
ldc_info_t * exec_hwinfo_info_restricted (int log, hd_hw_item_t type, hd_hw_item_t undesired_type, ldc_info_t * (* type_process)(int, hd_t*));

/*
 * @brief Funcao definida por conveniencia, para evitar a repeticao de codigo. Esta funcao
 * faz uma chamada a metodos da libhd, passando parametros especificados e repassa os resultados
 * desta chamada a uma outra funcao, tambem especificada.
 *
 * @param log Ponteiro para a estrutura de log onde será inserido a nova tupla.
 * @param type Parametro a ser passado para a funcao hd_list da libhd, definindo o tipo de dispositivo desejado.
 * @param type_process Funcao que recebera cada um dos resultado da chamada a hd_list.
 *
 * @return Estrutura de diagnostico, com os resultados finais.
 */
ldc_diag_t * exec_hwinfo_diag (int log, hd_hw_item_t type, ldc_diag_t * (* type_process)(int, hd_t*));

/*
 * @brief Executa uma aplicacao externa e escreve o output em um arquivo.
 *
 * @param cmd Comando a ser executado, incluindo seus parametros.
 * @param output_file Nome/caminho do arquivo onde a saida da aplicacao deve ser escrita.
 */
void execute_command (char * cmd, char * output_file);

/*
 * @brief Executa uma aplicacao externa e escreve o output em um arquivo.
 *
 * @param cmd Comando a ser executado, incluindo seus parametros.
 * @param tmp_file Estrutura onde deve ser alocado o arquivo temporario, de output da aplicacao executada.
 */
void execute_command_create_output (char * cmd, FILE ** tmp_file);

/*
 * @brief Divide uma string nos seus espacos vazios, transformando-a em um array de strings.
 * Os ' ' e '\t' iniciais, da string, sao removidos, assim como o '\n' terminal. O ultimo elemento
 * do array retornado aponta para NULL.
 *
 * @param str String a ser dividida.
 *
 * @return Array de strings.
 */
char ** split_string(char * str);

/*
 * @brief Cria um arquivo temporario, alocado em f, e retorna o nome deste arquivo.
 *
 * @param f Estrutura onde deve ser alocado o arquivo temporario.
 *
 * @return Nome do arquivo temporario criado.
 */
char * create_tmp_file (FILE **f);

/*
 * @brief Interface externa. Esta e a funcao para obter as informacoes do dispositivo.
 * Esta funcao deve ser implementada por todos as bibliotecas.
 *
 * @param log Indica se um log do processo deve ser criado.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info (int log);

/*
 * @brief Interface externa. Esta e a funcao para realizar o diagnostico do dispositivo.
 * Esta funcao deve ser implementada por todos as bibliotecas.
 *
 * @param log Indica se um log do processo deve ser criado.
 * @param info Estrutura informativa, sobre o dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnóstico.
 */
ldc_diag_t * diag (int log, ldc_info_t * info);

#endif /* LDC_CORE */
