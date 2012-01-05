#ifndef INFO_KEYBOARD
#define INFO_KEYBOARD

#include <ldc_core.h>

/*
 * @brief Captura as informações do teclado, utilizando as informações disponíveis no hwinfo.
 *
 * @param log Indica se será gerado o log.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info (int log);

/*
 * @brief Função auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informações de um teclado.
 * Então, salva na estrutura de retorno todas a infomações do dispositivo.
 *
 * @param log
 * @param hd Ponteiro para a estrutura da libhd que contém as informações do teclado.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info_libhd_keyboard (ldc_info_t * log, hd_t * hd);

/**
  @brief Função auxiliar que recebe o output do xorg.conf pre-processado e busca por informacoes sobre XkbRules, XkbModel e XkbLayout.
  Depois, a informação será inserida na estrutura passada como parâmetro.

  @param head Ponteiro para a estrutura onde será inserido as informações.
  @param f Arquivo que contém o output do xorg.conf pre-processado.
*/
void process_xorg_xkb(tuple_t ** head, FILE * f);

#endif /* INFO_KEYBOARD */
