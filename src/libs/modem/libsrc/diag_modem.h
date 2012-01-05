#ifndef DIAG_MODEM
#define DIAG_MODEM

#include <ldc_core.h>

/*
 * @brief Executa o teste de diagnostico do modem.
 *
 * @param log Indica se ser� gerado o log.
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagn�stico.
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

/*
 * @brief Fun��o auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informa��es do modem.
 * Ent�o, salva na estrutura de retorno todas a infoma��es do dispositivo.
 *
 * @param log Indica se ser� gerado o log.
 * @param hd Ponteiro para a estrutura da libhd que cont�m as informa��es do dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do diagnostico.
 */
ldc_diag_t * diag_libhd_modem (int log, ldc_info_t * info);

/*
 * @brief Funcao auxiliar que processa o output do comando lsmod para identificar os modulos carregados para o modem.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
int process_lsmod(tuple_t ** head, FILE * f);

#endif /* DIAG_MODEM */

