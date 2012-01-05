#ifndef INFO_VIDEO
#define INFO_VIDEO

#include <ldc_core.h>

extern unsigned hd_display_adapter(hd_data_t *hd_data);

/**
  @brief Captura as informações dos dispositivos

  @param log Indica se será gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/*
 * @brief Função auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informações do dispositivo.
 * Então, salva na estrutura de retorno todas a infomações do dispositivo.
 *
 * @param log
 * @param hd Ponteiro para a estrutura da libhd que contém as informações do dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * videocard_module ();

/**
  @brief Método auxiliar que recebe um ponteiro para a estrutura 'tail' e irá inserir uma nova tupla com os valores passados como parâmetros.
  Também é verificado se o valor de attr_value é válido, caso contrário será inserido a string 'Unknown'.

  @param tail Ponteiro para a estrutura onde será inserido a nova tupla.
  @param attr_name String indicando o nome da tupla.
  @param attr_value String indicando o valor da tupla.
  @param id Inteiro que indica o id da tupla.
  @param attr_desc String que indica a descrição da tupla.
*/
void insert_tuple(ldc_info_t * tail, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

#endif /* INFO_VIDEO */
