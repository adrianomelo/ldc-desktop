#ifndef DIAG_WEBCAM
#define DIAG_WEBCAM

#include <ldc_core.h>

/*
 * @brief Executa o teste de diagnostico da webcam.
 *
 * @param log Indica se sera gerado o log.
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnostico.
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

/*
 * @brief Executa o teste de diagnostico da webcam baseado na libhd.
 *
 * @param log Indica se sera gerado o log.
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnostico.
 */
ldc_diag_t * diag_libhd_webcam(int log, ldc_info_t * info);

/*
 * @brief Funcao auxiliar que trata as informacoes do lsmod.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do lsmod, de onde a informacao deve ser lida.
 */
int process_lsmod(tuple_t ** head, FILE * f);

#endif /* DIAG_WEBCAM */

