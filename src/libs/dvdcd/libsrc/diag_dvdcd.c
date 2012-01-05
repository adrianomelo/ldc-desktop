#include "diag_dvdcd.h"

/*
 * RQF08.C : Diagnostico - Através de um CD-RW de teste, efetuar a gravação e a leitura do CRC.
 * RQF08.D : Diagnostico - Através de um DVD-RW de teste, efetuar a gravação e a leitura do CRC.
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_diag_t * ret = new_ldc_diag_t("dvdcd");

	printf("DVDCD - Diag Stub\n");

	return NULL;
}
