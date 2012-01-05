#include "info_memory.h"

/*
 * RQF06.A	Identificar - Controlador: velocidades suportadas, tipos de módulos suportados,
 * 			tensão dos módulos, tamanho máximo de cada módulo, tamanho total máximo e espaço
 * 			de endereçamento. - TODO faltando espaco de enderecamento
 * RQF05.B 	Identificar - Módulos: Tamanho, modelo (SDRAM, DRAM, SGRAM, etc), tipo (DIMM, SIMM,
 * 			etc), velocidade, localização (DIMM0, DIMM1, etc). - OK
 */

ldc_info_t * info (int log) {
	ldc_info_t * ret = NULL;
	ldc_info_t * log_tuple =  new_ldc_info_t("memory");

	// For each element of type 'hw_memory', 'info_libhd_memory' will be called
	ret = enqueue_ldc_info_t(ret, exec_hwinfo_info(log_tuple, hw_memory, &info_libhd_memory));

	if (log){
		insert_info_log(log_tuple);
	}
	return ret;
}

ldc_info_t * info_libhd_memory (ldc_info_t * log, hd_t * hd) {
	ldc_info_t * ret = new_ldc_info_t("memory");
	ldc_info_t * log_tuple = new_ldc_info_t("memory");

	hd_res_t * res = hd->res;

	char name[100];
	char * value; char _value[200]; value = _value;
	int id;
	char  description[100];

	// Memory Start
	sprintf(name, "start_addr");
	sprintf(value, "Unknown");
	id = -1;
	sprintf(description, "Start address");

	sprintf(value, "0x%08lX", (unsigned long) (res->mem.base));
	ret->info = enqueue_new_tuple_t(ret->info, name, value, id, description);

	// Memory End
	sprintf(name, "end_addr");
	sprintf(value, "Unknown");
	id = -1;
	sprintf(description, "End address");

	if (res->mem.range) sprintf(value, "0x%08lX", (unsigned long) (res->mem.base + res->mem.range - 1));
	ret->info = enqueue_new_tuple_t(ret->info, name, value, id, description);

	FILE * dmidecode_output = NULL;

	execute_dmidecode(&dmidecode_output);

	info_dmidecode_sections(&ret->info, &log_tuple->info, dmidecode_output);

	ret->return_status = 1; // Success

	if (log->info == NULL){
		*log = *log_tuple;
	} else {
		enqueue_ldc_info_t(log, log_tuple);
	}

	return ret;
}

void info_dmidecode_sections(tuple_t ** head, tuple_t ** log, FILE * f) {
	// Memory Controller Section
	process_dmi_type(5, f, head, log, &info_process_dmi_type_5, "Memory Controller Error: Block not found!\n");

	// Memory Module Section
	process_dmi_type(6, f, head, NULL, &info_process_dmi_type_6, "Memory Module Error: Block not found!\n");

	// Memory Device Section
	process_dmi_type(17, f, head, log, &info_process_dmi_type_17, "Memory Device Error: Block not found!\n");
}

void info_process_dmi_type_5(tuple_t ** head, tuple_t ** log, FILE * f) {
	// Maximum Memory Module Size --------------------------------------------
	process_dmi_type_5_max_mod_size(head, log, f);

	// Maximum Total Memory Size ---------------------------------------------
	process_dmi_type_5_max_total_size(head, log, f);

	// Supported Speeds ------------------------------------------------------
	process_dmi_type_5_speeds(head, f);

	// Supported Memory Types ------------------------------------------------
	process_dmi_type_5_types(head, log, f);

	// Memory Module Voltage -------------------------------------------------
	process_dmi_type_5_voltage(head, log, f);

}

void info_process_dmi_type_6(tuple_t ** head, tuple_t ** log, FILE * f) {
	char module_socket [100];

	// Socket Designation ----------------------------------------------------
	process_dmi_type_6_socket(head, f, module_socket);

	// Memory Module Speed ---------------------------------------------------
	process_dmi_type_6_speed(head, f, module_socket);

	// Type ------------------------------------------------------------------
	process_dmi_type_6_type(head, f, module_socket);

	// Installed Size --------------------------------------------------------
	process_dmi_type_6_size(head, f, module_socket);
}

void info_process_dmi_type_17(tuple_t ** head, tuple_t ** log, FILE * f) {
	char module_socket [100];

	// Locator ---------------------------------------------------------------
	process_dmi_type_17_socket(head, f, module_socket);

	// Memory Module Speed ---------------------------------------------------
	process_dmi_type_17_speed (head, f, module_socket);

	// Type ------------------------------------------------------------------
	process_dmi_type_17_type (head, log, f, module_socket);

	// Form Factor -----------------------------------------------------------
	process_dmi_type_17_ffactor (head, log, f, module_socket);

	// Installed Size --------------------------------------------------------
	process_dmi_type_17_size (head, log, f, module_socket);

	// Manufacturer ----------------------------------------------------------
	process_dmi_type_17_vendor (head, f, module_socket);

	// Serial Number ---------------------------------------------------------
	process_dmi_type_17_sn (head, f, module_socket);

	// Part Number -----------------------------------------------------------
	process_dmi_type_17_pn (head, f, module_socket);
}
