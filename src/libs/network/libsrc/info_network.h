#ifndef INFO_NETWORK
#define INFO_NETWORK

#include <ldc_core.h>

/**
  @brief Captura as informacoes da placa de rede. Utilizando as informacoes do hwinfo (--netcard) e ethtool.

  @param log Indica se sera gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/**
  @brief Funcao auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informacoes de um placa de rede.
  Entao, salva na estrutura de retorno todas a infomacoes do dispositivo.

  @param log Indica se sera gerado o log
  @param hd Ponteiro para a estrutura da libhd que contem as informacoes da placa de rede.

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * network_module (int log, hd_t * hd);

#endif /* INFO_NETWORK */
