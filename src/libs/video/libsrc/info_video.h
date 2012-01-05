#ifndef INFO_VIDEO
#define INFO_VIDEO

#include <ldc_core.h>

extern unsigned hd_display_adapter(hd_data_t *hd_data);

/**
  @brief Captura as informa��es dos dispositivos

  @param log Indica se ser� gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info (int log);

/*
 * @brief Fun��o auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informa��es do dispositivo.
 * Ent�o, salva na estrutura de retorno todas a infoma��es do dispositivo.
 *
 * @param log
 * @param hd Ponteiro para a estrutura da libhd que cont�m as informa��es do dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * videocard_module ();

/**
  @brief M�todo auxiliar que recebe um ponteiro para a estrutura 'tail' e ir� inserir uma nova tupla com os valores passados como par�metros.
  Tamb�m � verificado se o valor de attr_value � v�lido, caso contr�rio ser� inserido a string 'Unknown'.

  @param tail Ponteiro para a estrutura onde ser� inserido a nova tupla.
  @param attr_name String indicando o nome da tupla.
  @param attr_value String indicando o valor da tupla.
  @param id Inteiro que indica o id da tupla.
  @param attr_desc String que indica a descri��o da tupla.
*/
void insert_tuple(ldc_info_t * tail, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

#endif /* INFO_VIDEO */
