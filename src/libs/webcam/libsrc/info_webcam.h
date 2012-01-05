#ifndef INFO_WEBCAM
#define INFO_WEBCAM

#include <hal/libhal.h>
#include <dbus/dbus.h>

#include <ldc_core.h>

/**
  @brief Captura as informacoes da webcam.

  @param log Indica se sera gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

#endif /* INFO_WEBCAM */
