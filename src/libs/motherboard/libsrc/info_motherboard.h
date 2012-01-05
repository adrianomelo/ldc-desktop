#ifndef INFO_MOTHERBOARD
#define INFO_MOTHERBOARD

#include <ldc_core.h>

/**
  @brief Captura as informa��es da placa m�e. Utilizando as informa��es dispon�veis no hwinfo (--bios, --bridge).

  @param log Indica se ser� gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/**
  @brief M�todo auxiliar que recebe um ponteiro para a estrutura 'tail' e ir� inserir uma nova tupla com os valores passados como par�metros.
  Se o o ponteiro para a estrutura 'log' for diferente de NULL, tamb�m ser� inserido a tupla nela. Tamb�m � verificado se o valor de attr_value �
  v�lido, caso contr�rio ser� inserido a string 'Unknown'.

  @param tail Ponteiro para a estrutura onde ser� inserido a nova tupla.
  @param log Ponteiro para a estrutura de log onde ser� inserido a nova tupla
  @param attr_name String indicando o nome da tupla.
  @param attr_value String indicando o valor da tupla.
  @param id Inteiro que indica o id da tupla.
  @param attr_desc String que indica a descri��o da tupla.
*/
void insert_tuple(ldc_info_t * tail, ldc_info_t * log, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

#endif /* INFO_MOTHERBOARD */
