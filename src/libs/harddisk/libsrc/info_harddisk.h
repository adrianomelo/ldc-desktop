#ifndef INFO_HARDDISK
#define INFO_HARDDISK

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)

extern char * hd_join (char * del, str_list_t * str); /* from libhd */

/**
  @brief Captura as informações do HD. Utilizando as informações do hwinfo (--disk) e o 'smartctl --info'.

  @param log Indica se será gerado o log

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info(int log);

/**
  @brief Função auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informações de um HD.
  Então, salva na estrutura de retorno todas a infomações do dispositivo.

  @param log Indica se será gerado o log
  @param hd Ponteiro para a estrutura da libhd que contém as informações do HD.

  @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa
*/
ldc_info_t * info_libhd_harddisk(ldc_info_t * log, hd_t * hd);

/**
  @brief Função auxiliar que recebe o output do comando smartctl --info e irá buscar a família do modelo do HD.
  Depois, a informação será inserida na estrutura passada como parâmetro.

  @param head Ponteiro para a estrutura onde será inserido as informações.
  @param f Arquivo que contém o output do comando smartctl --info.
*/
void process_smartctl_ModelFamily(tuple_t ** head, FILE * f);

#endif /* INFO_HARDDISK */
