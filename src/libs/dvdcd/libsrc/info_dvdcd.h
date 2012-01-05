#ifndef INFO_DVDCD
#define INFO_DVDCD

#include <ldc_core.h>

/**
  @brief Converte uma lista de strings em uma string unica. Esta funcao e importada da biblioteca libhd.

  @param del String delimitadora.
  @param str Lista de strings. O tipo str_list_t esta definido na biblioteca libhd.

  @return Ponteiro o buffer com a string final armazenada.
*/
extern char * hd_join (char * del, str_list_t * str); /* from libhd */

/*
 * @brief Captura as informações do CD/DVD, utilizando as informações disponíveis no hwinfo.
 *
 * @param log Indica se será gerado o log.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info (int log);

/*
 * @brief Utiliza a funcao hd_join para concatenar a lista dos drivers utilizados pelo dispositivo.
 *
 * @param hd Ponteiro para a estrutura hd_t que contem as informacoes desejadas.
 * @param buffer Buffer onde sera armazenado o resultado da concatenacao.
 *
 * @return O proprio conteudo do parametro buffer.
 */
char * format_drivers(hd_t * hd, char * buffer);

/*
 * @brief Cria uma string com a lista dos tipos de midia suportados pelo dispositivo.
 *
 * @param hd Ponteiro para a estrutura hd_t que contem as informacoes desejadas.
 * @param buffer Buffer onde sera armazenado o resultado da concatenacao.
 *
 * @return O proprio conteudo do parametro buffer.
 */
char * format_medias(hd_t * hd, char * buffer);

#endif /* INFO_DVDCD */

