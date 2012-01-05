#ifndef DIAG_USBSTORAGE
#define DIAG_USBSTORAGE

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)

/**
  @brief Executa o teste de diagnóstico

  @param log Indica se será gerado o log
  @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnóstico
*/
ldc_diag_t * diag(int log, ldc_info_t * info);

/**
  @brief Executa o teste de montagem e desmontagem

  @param dev_file Indica o local do dispositivo no dev
  @param part_list Ponteiro para a lista que indica o número da partições que serão testadas

  @return Resultado do teste.

  @retval 1 Sucesso
  @retval 0  Falha
*/
int mount_test(char *dev_file, int* part_list);


/**
  @brief Retorna a lista de partições para o dispositivo

  @param current_info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Lista com o número das partições identificadas para o dispositivo
*/
int* get_part_list(ldc_info_t * current_info);

/**
  @brief Verifica o particinamento

  @param part_list Lista com as partições para serem verificadas

  @return Resultado do teste.

  @retval 1 Sucesso
  @retval 0  Falha
*/
int check_part(int * part_list);

/**
  @brief Executa o fsck

  @param dev_file Indica o local do dispositivo no dev
  @param part_list Ponteiro para a lista que indica o número da partições que serão testadas

  @return Resultado do teste.

  @retval 1 Sucesso
  @retval 0  Falha
*/
int fsck_test(char *dev_file, int* part_list);

#endif /* DIAG_USBSTORAGE */

