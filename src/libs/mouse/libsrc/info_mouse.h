#ifndef INFO_MOUSE
#define INFO_MOUSE

#include <ldc_core.h>

/*
 * @brief Captura as informa��es do mouse, utilizando as informa��es dispon�veis no hwinfo.
 *
 * @param log Indica se ser� gerado o log.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info (int log);

#endif /* INFO_MOUSE */
