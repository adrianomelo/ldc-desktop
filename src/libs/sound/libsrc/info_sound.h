#ifndef INFO_SOUND
#define INFO_SOUND

#include <ldc_core.h>

/**
  @brief Captura as informa��es da placa de som. Utilizando as informa��es do hwinfo (--sound).
  @param log Indica se ser� gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/**
  @brief Procura no /proc/asound/modules o ID da placa que est� configurada com o m�dulo de driver passado como par�metro.

  @param tail Ponteiro para a estrutura ldc_info_t onde ser� inserido o ID da placa.
  @param mod Indica o m�dulo do driver configurado para a placa.
*/
void device_id(ldc_info_t * tail, char *mod);

#endif /* INFO_SOUND */
