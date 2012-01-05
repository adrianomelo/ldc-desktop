#include "diag_processor.h"

/*
 * RQF05.C	Diagnostico - Caso o teste de compatibilidade tenha falhado para este item,
 * informar o nome do processador encontrado atraves do "dmidecode".
 */

// TODO : Diagnosticar TODOS os procs ou só os contidos no info? Se todos, ok. Se os do info,
// pensar em como fazer isso, pois, atualmente, todos sao testados (os q foram retornados pelo
// hwinfo)

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_diag_t * ret = NULL;

	// For each element of type 'hw_cpu', 'diag_libhd_processor' will be called
	ret = enqueue_ldc_diag_t(ret, exec_hwinfo_diag(log, hw_cpu, &diag_libhd_processor));

	if (log){
		insert_diag_log(ret);
	}
	return ret;
}

ldc_diag_t * diag_libhd_processor (int log, hd_t * hd) {
	ldc_diag_t * ret = new_ldc_diag_t("processor");

	FILE * dmidecode_output = NULL;

	execute_dmidecode(&dmidecode_output);
	diag_dmidecode_sections(&ret->info, dmidecode_output);

	if (ret->info){
		ret->return_status = 0; //Success
	}

	return ret;
}

void diag_dmidecode_sections(tuple_t ** head, FILE * f) {
	// Processor Information Section
	process_dmi_type(4, f, head, NULL, &diag_process_dmi_type_4, "Processor Information Error: Block not found!\n");
}

void diag_process_dmi_type_4(tuple_t ** head, tuple_t ** log, FILE * f) {
	// Version ----------------------------------------------------
	process_dmi_type_4_version(head, f);
}
