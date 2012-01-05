#include "diag_memory.h"

/*
 * RQF06.D	Diagnóstico - Informar o tamanho da memória obtido através do "/proc" e o
 * 			tamanho obtido através do dmidecode (a diferença entre os dois valores,
 * 			provavelmente, será a memória alocada para vídeo). - OK
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_diag_t * ret = NULL;

	// For each element of type 'hw_memory', 'diag_libhd_memory' will be called
	ret = enqueue_ldc_diag_t(ret, exec_hwinfo_diag(log, hw_memory, &diag_libhd_memory));

	if (log){
		insert_diag_log(ret);
	}
	return ret;
}

ldc_diag_t * diag_libhd_memory (int log, hd_t * hd) {
	ldc_diag_t * ret = new_ldc_diag_t("memory");

	FILE * dmidecode_output = NULL;
	FILE * proc_output = NULL;

	execute_dmidecode(&dmidecode_output);
	diag_dmidecode_sections(&ret->info, dmidecode_output);

	execute_command_create_output ("grep MemTotal /proc/meminfo | awk '{print $2}'", &proc_output);
	process_proc_meminfo_MemTotal(&ret->info, proc_output);

	int dmidecode_size = 0;
	int procmeminfo_size = 0;

	tuple_t * current = ret->info;

	while(current != NULL) {
		// Do not change the testing sequence!
		if (strstr(current->name, "meminfo") != NULL) {
			procmeminfo_size += current->id;
		} else if (strstr(current->name, "_size") != NULL) {
			dmidecode_size += current->id;
		}

		current = current->next;
	}

	if (dmidecode_size * 1024 == procmeminfo_size) {
		ret->return_status = 1;
	} else {
		ret->return_status = 0;
	}

	return ret;
}

void diag_dmidecode_sections(tuple_t ** head, FILE * f) {
	// Memory Device Section
	process_dmi_type(17, f, head, NULL, &diag_process_dmi_type_17, "Memory Device Error: Block not found!\n");
}

void diag_process_dmi_type_17(tuple_t ** head, tuple_t ** log, FILE * f) {
	char module_socket [100];

	// Locator ---------------------------------------------------------------
	process_dmi_type_17_socket(head, f, module_socket);

	// Installed Size --------------------------------------------------------
	process_dmi_type_17_size (head, NULL, f, module_socket);
}
