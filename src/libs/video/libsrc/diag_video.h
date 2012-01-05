#ifndef DIAG_VIDEO
#define DIAG_VIDEO

#include <ldc_core.h>

/*
 * @brief Executa o teste de diagnostico do video.
 *
 * @param log Indica se ser� gerado o log.
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagn�stico.
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

/*
 * @brief Fun��o auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informa��es do dispositivo.
 * Ent�o, salva na estrutura de retorno todas a infoma��es do dispositivo.
 *
 * @param log Indica se ser� gerado o log.
 * @param hd Ponteiro para a estrutura da libhd que cont�m as informa��es do dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_diag_t * monitor_module (int log, hd_t * hd);

#endif /* DIAG_VIDEO */

