#ifndef DIAG_MOTHERBOARD
#define DIAG_MOTHERBOARD

#include <ldc_core.h>
/*
 * @brief Stub do diagnostico de placa-mae.
 *
 * @param log Indica se sera gerado o log
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagn�stico
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

#endif /* DIAG_MOTHERBOARD */

