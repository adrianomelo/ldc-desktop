#ifndef DIAG_NETWORK
#define DIAG_NETWORK

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)

/**
  @brief Executa o teste de diagnóstico de rede, que consiste em informar se o link está ativo (up), o MAC e
  as configurações de rede (IP, netmask, gateway e DNS).

  @param log Indica se será gerado o log
  @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnóstico
*/
ldc_diag_t * diag(int log, ldc_info_t * info);

/**
  @brief Procura qual o endereço de MAC correspondente a placa passada como parâmetro e irá inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa de rede que será testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde será inserido o MAC da placa.
*/
void net_mac (char *net_dev, ldc_diag_t * current);

/**
  @brief Utiliza o ifconfig para achar o IP e netmask configurado para a placa passada como parâmetro e irá inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa de rede que será testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde será inserido o endereço IP e netmask da placa.
*/
void net_conf(char *net_dev, ldc_diag_t * current);

/**
  @brief Procura no arquivo /etc/resolv.conf os servidores DNS configurados e irá inserir o resultado
  na estrutura 'current'.

  @param current Ponteiro para a estrutura ldc_diag_t onde serão inseridos os endereços dos servidores DNS configurados.
*/
void net_dns(ldc_diag_t * current);

/**
  @brief Utiliza o comando route para identificar o default gateway configurado para a placa passada como parâmetro e irá inserir
  o resultado na estrutura 'current'.

  @param net_dev Indica a placa de rede que será testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde será inserido o endereço do gateway da placa.
*/
void net_gw(char *net_dev, ldc_diag_t * current);

/**
  @brief Verifica através do comando ifconfig se o link da placa passada como parâmetro está ativo (UP) e irá inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa de rede que será testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde será inserido 0 ou 1 para inticar se o link está ativo (UP)
*/
void net_link(char *net_dev, ldc_diag_t * current);

#endif /* DIAG_NETWORK */

