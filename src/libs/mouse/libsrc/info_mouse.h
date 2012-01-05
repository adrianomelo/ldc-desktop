#ifndef INFO_MOUSE
#define INFO_MOUSE

#include <ldc_core.h>

/*
 * @brief Captura as informações do mouse, utilizando as informações disponíveis no hwinfo.
 *
 * @param log Indica se será gerado o log.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info (int log);

#endif /* INFO_MOUSE */
