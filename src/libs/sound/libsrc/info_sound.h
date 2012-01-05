#ifndef INFO_SOUND
#define INFO_SOUND

#include <ldc_core.h>

/**
  @brief Captura as informações da placa de som. Utilizando as informações do hwinfo (--sound).
  @param log Indica se será gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/**
  @brief Procura no /proc/asound/modules o ID da placa que está configurada com o módulo de driver passado como parâmetro.

  @param tail Ponteiro para a estrutura ldc_info_t onde será inserido o ID da placa.
  @param mod Indica o módulo do driver configurado para a placa.
*/
void device_id(ldc_info_t * tail, char *mod);

#endif /* INFO_SOUND */
