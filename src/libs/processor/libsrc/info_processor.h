#ifndef INFO_PROCESSOR
#define INFO_PROCESSOR

#include "core_processor.h"

/**
  @brief Converte uma lista de strings em uma string unica. Esta funcao e importada da biblioteca libhd.

  @param del String delimitadora.
  @param str Lista de strings. O tipo str_list_t esta definido na biblioteca libhd.

  @return Ponteiro o buffer com a string final armazenada.
*/
extern char * hd_join (char * del, str_list_t * str); /* from libhd */

/*
 * @brief Captura as informa��es do CD/DVD, utilizando as informa��es dispon�veis no dmidecode.
 *
 * @param log Indica se ser� gerado o log.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info(int log);

/*
 * @brief Fun��o auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informa��es do dispositivo.
 * Ent�o, salva na estrutura de retorno todas a infoma��es do dispositivo.
 *
 * @param log
 * @param hd Ponteiro para a estrutura da libhd que cont�m as informa��es do dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info_libhd_processor(ldc_info_t * log, hd_t * hd);

/*
 * @brief Funcao auxiliar que centraliza o tratamento das informacoes disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void info_dmidecode_sections(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Funcao auxiliar que trata as informacoes sobre os processadores, disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void info_process_dmi_type_4(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Funcao auxiliar que trata as informacoes sobre as memorias cache, disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void info_process_dmi_type_7(tuple_t ** head, tuple_t ** log, FILE * f);

#endif /* INFO_PROCESSOR */
