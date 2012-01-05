#ifndef DIAG_PROCESSOR
#define DIAG_PROCESSOR

#include "core_processor.h"

/*
 * @brief Executa o teste de diagnostico da processador.
 *
 * @param log Indica se ser� gerado o log.
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagn�stico.
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

/*
 * @brief Fun��o auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informa��es do processador.
 * Ent�o, salva na estrutura de retorno todas a infoma��es do dispositivo.
 *
 * @param log Indica se ser� gerado o log.
 * @param hd Ponteiro para a estrutura da libhd que cont�m as informa��es do dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do diagnostico.
 */
ldc_diag_t * diag_libhd_processor (int log, hd_t * hd);

/*
 * @brief Funcao auxiliar que centraliza o tratamento das informacoes disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void diag_dmidecode_sections(tuple_t ** head, FILE * f);

/*
 * @brief Funcao auxiliar que trata as informacoes sobre os processadores (DMI TYPE 4), disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void diag_process_dmi_type_4(tuple_t ** head, tuple_t ** log, FILE * f);

#endif /* DIAG_PROCESSOR */

