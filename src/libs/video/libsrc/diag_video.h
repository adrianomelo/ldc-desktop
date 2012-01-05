#ifndef DIAG_VIDEO
#define DIAG_VIDEO

#include <ldc_core.h>

/*
 * @brief Executa o teste de diagnostico do video.
 *
 * @param log Indica se será gerado o log.
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnóstico.
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

/*
 * @brief Função auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informações do dispositivo.
 * Então, salva na estrutura de retorno todas a infomações do dispositivo.
 *
 * @param log Indica se será gerado o log.
 * @param hd Ponteiro para a estrutura da libhd que contém as informações do dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_diag_t * monitor_module (int log, hd_t * hd);

#endif /* DIAG_VIDEO */

