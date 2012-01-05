#ifndef INFO_USBSTORAGE
#define INFO_USBSTORAGE

#include <ctype.h>

#include <ldc_core.h>

extern char * hd_join(char *del, str_list_t *str);

/**
  @brief Captura as informações dos dispositivos

  @param log Indica se será gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/**
  @brief Captura as informações das partições e insere no tail passado como parâmetro

  @param devFile Indica o local do dispositivo no dev
  @param tail Ponteiro para a estrutura ldc_info_t onde será inserido as informações das partições.

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
void partitions_info (char *devFile, ldc_info_t * tail);

#endif /* INFO_USBSTORAGE */
