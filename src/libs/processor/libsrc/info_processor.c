#include "info_processor.h"

/*
 * RQF05.A	Identificar - Fabricante, modelo, clock, caches (tamanho, associatividade, modo de
 * 			operacao, operacoes SRAM suportadas, tipo de correcao de erro), tensao, numero de
 * 			"cores" (nucleos), "features" (ex: MMX, SSE, HTT, MSR, etc).
 */

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)

ldc_info_t * info(int log) {
	ldc_info_t * ret = NULL;
	ldc_info_t * log_tuple = new_ldc_info_t("processor");

	// For each element of type 'hw_cpu', 'info_libhd_processor' will be called
	ret = enqueue_ldc_info_t(ret, exec_hwinfo_info(log_tuple, hw_cpu, &info_libhd_processor));

	if (log){
		insert_info_log(log_tuple);
	}
	return ret;
}

char * format_flags(hd_t * hd, char * buffer);

ldc_info_t * info_libhd_processor(ldc_info_t * log, hd_t * hd) {
	ldc_info_t * ret = new_ldc_info_t("processor");
	ldc_info_t * log_tuple = new_ldc_info_t("processor");

	cpu_info_t * ct;

	if(! hd->detail || hd->detail->type != hd_detail_cpu) {
		fprintf(stderr, "Problema na CPU\n");
	} else if(! (ct = hd->detail->cpu.data)) {
		fprintf(stderr, "Problema na CPU 2\n");
	} else {
		char name[100];
		char value[1000];
		int id;
		char  description[100];

		// Vendor
		SETUP_TUPLE("vendor", "Unknown", -1, "Vendor");
		if (ct->vend_name) sprintf(value, "%s", ct->vend_name);
		set_vendor(ret, name, value, id, description);
		set_vendor(log_tuple, name, value, id, description);

		// Model
		SETUP_TUPLE("device", "Unknown", -1, "Model");
		if (ct->model_name) sprintf(value, "%s", ct->model_name);
		set_model(ret, name, value, id, description);
		set_model(log_tuple, name, value, id, description);

		// Flags
		char * flags = hd_join("|", ct->features);
		SETUP_TUPLE("features", flags, -1, "Supported features");
		ret->info = enqueue_new_tuple_t(ret->info, name, value, id, description);
		free(flags);

		// Cores
		SETUP_TUPLE("n_cores", "NULL", ct->units, "# of cores");
		ret->info = enqueue_new_tuple_t(ret->info, name, NULL, id, description);

		// Clock
		SETUP_TUPLE("clock", "NULL", ct->clock, "Clock");
		ret->info = enqueue_new_tuple_t(ret->info, name, NULL, id, description);
		log_tuple->info = enqueue_new_tuple_t(log_tuple->info, name, NULL, id, description);

		// DMIDecode Stuff
		FILE * dmidecode_output = NULL;

		execute_dmidecode(&dmidecode_output);

		info_dmidecode_sections(&ret->info, &log_tuple->info, dmidecode_output);

		ret->return_status = 1; // Success
	}

	if (log->info == NULL){
		*log = *log_tuple;
	} else {
		enqueue_ldc_info_t(log, log_tuple);
	}

	return ret;
}


void info_dmidecode_sections(tuple_t ** head, tuple_t ** log, FILE * f) {
	// Processor Information Section
	process_dmi_type(4, f, head, log, &info_process_dmi_type_4, "Processor Information Error: Block not found!\n");

	// Cache Information Section
	process_dmi_type(7, f, head, log, &info_process_dmi_type_7, "Cache Information Error: Block not found!\n");
}


void info_process_dmi_type_4(tuple_t ** head, tuple_t ** log, FILE * f) {
	// Socket Designation ----------------------------------------------------
	process_dmi_type_4_socket(head, log, f);

	// Voltage ----------------------------------------------------
	process_dmi_type_4_voltage(head, f);

	// CPU Clock --------------------------------------------------------
	// process_dmi_type_4_clock(head, f);

	// FSB Clock ----------------------------------------------------------
	process_dmi_type_4_fsb(head, log, f);
}


void info_process_dmi_type_7(tuple_t ** head, tuple_t ** log, FILE * f) {
	char module_socket[100];

	// Socket Designation ----------------------------------------------------
	process_dmi_type_7_socket(head, f, module_socket);

	// Installed Size --------------------------------------------
	process_dmi_type_7_installed_size(head, log, f, module_socket);

	// Associativity --------------------------------------------
	process_dmi_type_7_associativity(head, f, module_socket);

	// Operational Mode --------------------------------------------
	process_dmi_type_7_operational_mode(head, log, f, module_socket);

	// Supported SRAM Types --------------------------------------------
	process_dmi_type_7_supported_types(head, log, f, module_socket);

	// Error Correction Type --------------------------------------------
	process_dmi_type_7_err_correction_type(head, f, module_socket);
}

char * format_flags(hd_t * hd, char * buffer) {
	char * pt_char = hd_join("|", hd->drivers);

	sprintf (buffer, "%s", pt_char);

	free(pt_char);

	return buffer;
}
