#ifndef DIAG_NETWORK
#define DIAG_NETWORK

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)

/**
  @brief Executa o teste de diagn�stico de rede, que consiste em informar se o link est� ativo (up), o MAC e
  as configura��es de rede (IP, netmask, gateway e DNS).

  @param log Indica se ser� gerado o log
  @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagn�stico
*/
ldc_diag_t * diag(int log, ldc_info_t * info);

/**
  @brief Procura qual o endere�o de MAC correspondente a placa passada como par�metro e ir� inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa de rede que ser� testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde ser� inserido o MAC da placa.
*/
void net_mac (char *net_dev, ldc_diag_t * current);

/**
  @brief Utiliza o ifconfig para achar o IP e netmask configurado para a placa passada como par�metro e ir� inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa de rede que ser� testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde ser� inserido o endere�o IP e netmask da placa.
*/
void net_conf(char *net_dev, ldc_diag_t * current);

/**
  @brief Procura no arquivo /etc/resolv.conf os servidores DNS configurados e ir� inserir o resultado
  na estrutura 'current'.

  @param current Ponteiro para a estrutura ldc_diag_t onde ser�o inseridos os endere�os dos servidores DNS configurados.
*/
void net_dns(ldc_diag_t * current);

/**
  @brief Utiliza o comando route para identificar o default gateway configurado para a placa passada como par�metro e ir� inserir
  o resultado na estrutura 'current'.

  @param net_dev Indica a placa de rede que ser� testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde ser� inserido o endere�o do gateway da placa.
*/
void net_gw(char *net_dev, ldc_diag_t * current);

/**
  @brief Verifica atrav�s do comando ifconfig se o link da placa passada como par�metro est� ativo (UP) e ir� inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa de rede que ser� testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde ser� inserido 0 ou 1 para inticar se o link est� ativo (UP)
*/
void net_link(char *net_dev, ldc_diag_t * current);

#endif /* DIAG_NETWORK */

