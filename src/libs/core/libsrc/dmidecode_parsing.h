#ifndef DEMIDECODE_PARSING_HEADER
#define DEMIDECODE_PARSING_HEADER

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ldc_core.h"
#include "ldc_tuple_t.h"

#define PROCESS_DMI_LOCAL_VARS 	char * tmp = NULL; \
								char title_ [200]; char * title = title_; title[0] = '\0'; \
								char value_ [200]; char * value = value_; value[0] = '\0'; \
								char description_ [200]; char * description = description_; description[0] = '\0'

/*
 * @brief Move ate a proxima linha no formato "Handle <Handle>, DMI type <Type>, <Bytes> bytes",
 * onde <Type> seja igual ao parametro type. A string retornada e alocada internamente, devendo
 * ser liberada, quando nao mais necessaria.
 *
 * @param f Arquivo de saida do dmidecode.
 * @param type Tipo do dispositivo a ser filtrado da saida do dmidecode.
 *
 * @return Linha no formato indicado, ou NULL, caso nenhuma linha correspondente seja encontrada.
 */
char * dmi_next_type(FILE * f, int type);

/*
 * @brief Le o valor de uma linha do dmidecode no formato "<Label>: <Texto>", onde <Label>
 * seja igual ao parametro label. A string retornada e alocada internamente, devendo
 * ser liberada, quando nao mais necessaria.
 *
 * @param f Arquivo de saida do dmidecode.
 * @param label Label do qual se deseja o valor.
 *
 * @return Linha no formato indicado, ou NULL, caso nenhuma linha correspondente seja encontrada.
 */
char * dmi_read_value(FILE * f, char * label);

/*
 * @brief Libera a memoria alocada pelas funcoes dmidecode da biblioteca core.
 *
 * @param mem Ponteiro para a regiao de memoria a ser liberada.
 */
void dmi_free(void * mem);

/*
 * @brief Executa o dmidecode e armazena a saida da aplicacao em um arquivo.
 *
 * @param tmp_file Arquivo de saida.
 */
void execute_dmidecode (FILE ** tmp_file);

/*
 * @brief Funcao definida por conveniencia, que localiza blocos do output
 * do dmidecode do tipo especificado e os repassa a funcao solicitada,
 * armazenando as tuplas dos resultados na lista passada como parametro.
 *
 * @param type Tipo do dispositivo a ser filtrado da saida do dmidecode.
 * @param tmp_file Arquivo contendo a saida do dmidecode.
 * @param head Cabeca da lista onde a informacao deve ser adicionada.
 * @param log Ponteiro para a estrutura de log onde será inserido a nova tupla.
 * @param dmi_type_processor Funcao que recebera cada um dos blocos encontrados.
 * @param error_msg Mensagem impressa na saida padrao, caso nenhum bloco do tipo especificado seja encontrado.
 */
void process_dmi_type(int type, FILE * tmp_file, tuple_t ** head, tuple_t ** log, void (* dmi_type_processor)(tuple_t **, tuple_t **, FILE *), char * error_msg);

#endif /* DEMIDECODE_PARSING_HEADER */
