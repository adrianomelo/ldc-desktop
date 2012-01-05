#ifndef DIAG_WIRELESS
#define DIAG_WIRELESS

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)
/*
 * @brief Executa o teste de diagnostico do adaptador wireless.
 *
 * @param log Indica se sera gerado o log.
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnostico.
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

/**
  @brief Procura qual o endereco de MAC correspondente a placa passada como parametro e ira inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa wireless que sera testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde sera inserido o MAC da placa.
*/
void net_mac (char *net_dev, ldc_diag_t * current);

/**
  @brief Utiliza o ifconfig para achar o IP e netmask configurado para a placa passada como parametro e ira inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa wireless que sera testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde sera inserido o endereco IP e netmask da placa.
*/
void net_conf(char *net_dev, ldc_diag_t * current);

/**
  @brief Procura no arquivo /etc/resolv.conf os servidores DNS configurados e ira inserir o resultado
  na estrutura 'current'.

  @param current Ponteiro para a estrutura ldc_diag_t onde serao inseridos os enderecos dos servidores DNS configurados.
*/
void net_dns(ldc_diag_t * current);

/**
  @brief Utiliza o comando route para identificar o default gateway configurado para a placa passada como parametro e ira inserir
  o resultado na estrutura 'current'.

  @param net_dev Indica a placa wireless que sera testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde sera inserido o endereco do gateway da placa.
*/
void net_gw(char *net_dev, ldc_diag_t * current);

/**
  @brief Verifica atraves do comando ifconfig se o link da placa passada como parametro esta ativo (UP) e ira inserir o resultado
  na estrutura 'current'.

  @param net_dev Indica a placa wireless que sera testada.
  @param current Ponteiro para a estrutura ldc_diag_t onde sera inserido 0 ou 1 para inticar se o link esta ativo (UP)
*/
void net_link(char *net_dev, ldc_diag_t * current);

#endif /* DIAG_WIRELESS */

