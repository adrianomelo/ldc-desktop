#include "diag_modem.h"

/*
 * RQF15.C : Diagnóstico - Informar se algum dos possíveis drivers foi carregado (ltmodem, sfmodem e hsfmodem).
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_diag_t * ret = NULL;
	ldc_info_t * cur_info = info;

	for (; cur_info; cur_info = cur_info->next) {
		ldc_diag_t * cur_diag = diag_libhd_modem(log, cur_info);

		ret = enqueue_ldc_diag_t(ret, cur_diag);
	}

	if (log){
		insert_diag_log(ret);
	}
	return ret;
}

//ldc_diag_t * diag_libhd_modem (int log, hd_t * hd) {
ldc_diag_t * diag_libhd_modem (int log, ldc_info_t * info) {
	ldc_diag_t * ret = new_ldc_diag_t("modem");

	FILE * cmd_output = NULL;

	execute_command_create_output ("lsmod | grep -E 'ltmodem|sfmodem|hsfmodem|hsfserial' | awk '{print $1}'", &cmd_output);

	ret->return_status = process_lsmod(&ret->info, cmd_output);

	return ret;
}

int process_lsmod(tuple_t ** head, FILE * f) {
	int ret = 0;

	int counter = 0;

	char title[100];
	char * value; char _value[200]; value = _value;
	int id;
	char  description[100];

	id = -1;
	sprintf(description, "Loaded driver module");

	while (fscanf(f, "%s", value) && (! feof(f))) {
		sprintf(title, "driver_mod_%d", counter++);

		*head = enqueue_new_tuple_t(*head, title, value, id, description);

		ret = 1;
	}

	return ret;
}
