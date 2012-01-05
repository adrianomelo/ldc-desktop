#ifndef INFO_MOTHERBOARD
#define INFO_MOTHERBOARD

#include <ldc_core.h>

/**
  @brief Captura as informações da placa mãe. Utilizando as informações disponíveis no hwinfo (--bios, --bridge).

  @param log Indica se será gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/**
  @brief Método auxiliar que recebe um ponteiro para a estrutura 'tail' e irá inserir uma nova tupla com os valores passados como parâmetros.
  Se o o ponteiro para a estrutura 'log' for diferente de NULL, também será inserido a tupla nela. Também é verificado se o valor de attr_value é
  válido, caso contrário será inserido a string 'Unknown'.

  @param tail Ponteiro para a estrutura onde será inserido a nova tupla.
  @param log Ponteiro para a estrutura de log onde será inserido a nova tupla
  @param attr_name String indicando o nome da tupla.
  @param attr_value String indicando o valor da tupla.
  @param id Inteiro que indica o id da tupla.
  @param attr_desc String que indica a descrição da tupla.
*/
void insert_tuple(ldc_info_t * tail, ldc_info_t * log, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

#endif /* INFO_MOTHERBOARD */
