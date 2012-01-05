#ifndef INFO_HARDDISK
#define INFO_HARDDISK

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)

extern char * hd_join (char * del, str_list_t * str); /* from libhd */

/**
  @brief Captura as informa��es do HD. Utilizando as informa��es do hwinfo (--disk) e o 'smartctl --info'.

  @param log Indica se ser� gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info(int log);

/**
  @brief Fun��o auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informa��es de um HD.
  Ent�o, salva na estrutura de retorno todas a infoma��es do dispositivo.

  @param log Indica se ser� gerado o log
  @param hd Ponteiro para a estrutura da libhd que cont�m as informa��es do HD.

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info_libhd_harddisk(ldc_info_t * log, hd_t * hd);

/**
  @brief Fun��o auxiliar que recebe o output do comando smartctl --info e ir� buscar a fam�lia do modelo do HD.
  Depois, a informa��o ser� inserida na estrutura passada como par�metro.

  @param head Ponteiro para a estrutura onde ser� inserido as informa��es.
  @param f Arquivo que cont�m o output do comando smartctl --info.
*/
void process_smartctl_ModelFamily(tuple_t ** head, FILE * f);

#endif /* INFO_HARDDISK */
