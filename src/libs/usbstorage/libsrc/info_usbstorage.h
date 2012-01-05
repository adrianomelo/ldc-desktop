#ifndef INFO_USBSTORAGE
#define INFO_USBSTORAGE

#include <ctype.h>

#include <ldc_core.h>

extern char * hd_join(char *del, str_list_t *str);

/**
  @brief Captura as informa��es dos dispositivos

  @param log Indica se ser� gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/**
  @brief Captura as informa��es das parti��es e insere no tail passado como par�metro

  @param devFile Indica o local do dispositivo no dev
  @param tail Ponteiro para a estrutura ldc_info_t onde ser� inserido as informa��es das parti��es.

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
void partitions_info (char *devFile, ldc_info_t * tail);

#endif /* INFO_USBSTORAGE */
