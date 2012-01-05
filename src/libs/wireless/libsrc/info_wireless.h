#ifndef INFO_WIRELESS
#define INFO_WIRELESS

#include <ldc_core.h>

/**
  @brief Captura as informacoes da wireless.

  @param log Indica se sera gerado o log

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
ldc_info_t * info_wireless (ldc_info_t * log, hd_t * hd);

/**
  @brief Verifica os modos de operacao da placa de rede sem fio.

  @param net_dev Indica a placa wireless da qual se quer descobrir a informacao.
  @param current Ponteiro para a estrutura ldc_info_t onde sera inserida a informacao.
*/
void operation_mode(char *net_dev, ldc_info_t * current);

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

#endif /* INFO_WIRELESS */
