#ifndef DIAG_USBSTORAGE
#define DIAG_USBSTORAGE

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)

/**
  @brief Executa o teste de diagn�stico

  @param log Indica se ser� gerado o log
  @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagn�stico
*/
ldc_diag_t * diag(int log, ldc_info_t * info);

/**
  @brief Executa o teste de montagem e desmontagem

  @param dev_file Indica o local do dispositivo no dev
  @param part_list Ponteiro para a lista que indica o n�mero da parti��es que ser�o testadas

  @return Resultado do teste.

  @retval 1 Sucesso
  @retval 0  Falha
*/
int mount_test(char *dev_file, int* part_list);


/**
  @brief Retorna a lista de parti��es para o dispositivo

  @param current_info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Lista com o n�mero das parti��es identificadas para o dispositivo
*/
int* get_part_list(ldc_info_t * current_info);

/**
  @brief Verifica o particinamento

  @param part_list Lista com as parti��es para serem verificadas

  @return Resultado do teste.

  @retval 1 Sucesso
  @retval 0  Falha
*/
int check_part(int * part_list);

/**
  @brief Executa o fsck

  @param dev_file Indica o local do dispositivo no dev
  @param part_list Ponteiro para a lista que indica o n�mero da parti��es que ser�o testadas

  @return Resultado do teste.

  @retval 1 Sucesso
  @retval 0  Falha
*/
int fsck_test(char *dev_file, int* part_list);

#endif /* DIAG_USBSTORAGE */

