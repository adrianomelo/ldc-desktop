#ifndef INFO_KEYBOARD
#define INFO_KEYBOARD

#include <ldc_core.h>

/*
 * @brief Captura as informa��es do teclado, utilizando as informa��es dispon�veis no hwinfo.
 *
 * @param log Indica se ser� gerado o log.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info (int log);

/*
 * @brief Fun��o auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informa��es de um teclado.
 * Ent�o, salva na estrutura de retorno todas a infoma��es do dispositivo.
 *
 * @param log
 * @param hd Ponteiro para a estrutura da libhd que cont�m as informa��es do teclado.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info_libhd_keyboard (ldc_info_t * log, hd_t * hd);

/**
  @brief Fun��o auxiliar que recebe o output do xorg.conf pre-processado e busca por informacoes sobre XkbRules, XkbModel e XkbLayout.
  Depois, a informa��o ser� inserida na estrutura passada como par�metro.

  @param head Ponteiro para a estrutura onde ser� inserido as informa��es.
  @param f Arquivo que cont�m o output do xorg.conf pre-processado.
*/
void process_xorg_xkb(tuple_t ** head, FILE * f);

#endif /* INFO_KEYBOARD */
