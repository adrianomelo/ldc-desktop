#include "diag_keyboard.h"

/*
 * RQF17.C : Diagnostico - Verificar se o teclado esta plugado.
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_diag_t * ret = new_ldc_diag_t("keyboard");

	printf("KEYBOARD - Diag Stub\n");

	return ret;
}
