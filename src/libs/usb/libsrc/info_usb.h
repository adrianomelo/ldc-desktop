#ifndef INFO_USB
#define INFO_USB

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)

extern char * hd_join (char * del, str_list_t * str); /* from libhd */

/**
  @brief Captura as informacoes da USB.

  @param log Indica se sera gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info(int log);

/**
  @brief Processa informacoes quantitativas de hubs USB através do comando lsusb.

  @param cmd Comando lsusb a ser quantificado.

  @return Inteiro descrevendo a quantidade correspondente aos critérios de cmd.
*/
int process_lsusb_numeric_info(char * cmd);

#endif /* INFO_USB */
