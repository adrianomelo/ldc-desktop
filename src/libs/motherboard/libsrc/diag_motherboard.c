#include "diag_motherboard.h"

/*
 * RQF04.C : Diagnóstico - Caso algum dispositivo nao tenha sido identificado
 * 				corretamente no teste de compatibilidade (identificado como
 * 				"unknown"), sugerir a atualizacao do arquivo de definicoes pciids.
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_diag_t * ret = new_ldc_diag_t("motherboard");

	printf("MOTHERBOARD - Diag Stub\n");

	return ret;
}
