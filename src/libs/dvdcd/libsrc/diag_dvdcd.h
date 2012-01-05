#ifndef DIAG_DVDCD
#define DIAG_DVDCD

#include <ldc_core.h>

/*
 * @brief Stub do diagnostico de CD/DVD. Essa funcionalidade e completamente implementada em Python.
 *
 * @param log Indica se será gerado o log
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnóstico
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

#endif /* DIAG_DVDCD */

