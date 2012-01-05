#ifndef DIAG_USB
#define DIAG_USB

#include <string.h>
#include <ctype.h>

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)
/*
 * @brief Executa o teste de diagnostico das portas USB.
 *
 * @param log Indica se sera gerado o log.
 * @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 *
 * @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnostico.
 */
ldc_diag_t * diag(int log, ldc_info_t * info);

/*
 * @brief Funcao auxiliar que trata as informacoes do lsusb.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do lsusb, de onde a informacao deve ser lida.
 */
void process_lsusb_output(tuple_t ** head, FILE * f);

#endif /* DIAG_USB */

