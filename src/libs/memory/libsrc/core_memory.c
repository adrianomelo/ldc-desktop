#include "core_memory.h"

void process_dmi_type_5_max_mod_size(tuple_t ** head, tuple_t ** log, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "max_mem_mod_size");
	sprintf(description, "Maximum Memory Module Size");

	tmp = dmi_read_value(f, "Maximum Memory Module Size");

	if (tmp) {
		char ** split = split_string(tmp);

		if (split[0]) {
			id = atoi(split[0]);
			value = NULL;
		}

		if (split[1]) sprintf(description, "Maximum Memory Module Size (in %s)", split[1]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
	*log = enqueue_new_tuple_t(*log, title, value, id, description);
}


void process_dmi_type_5_max_total_size(tuple_t ** head, tuple_t ** log, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "max_total_mem_size");
	sprintf(description, "Maximum Total Memory Size");

	tmp = dmi_read_value(f, "Maximum Total Memory Size");

	if (tmp) {
		char ** split = split_string(tmp);

		if (split[0]) {
			id = atoi(split[0]);
			value = NULL;
		}

		if (split[1]) sprintf(description, "Maximum Total Memory Size (in %s)", split[1]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
	*log = enqueue_new_tuple_t(*log, title, value, id, description);
}


void process_dmi_type_5_speeds(tuple_t ** head, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "sup_speeds");
	sprintf(description, "Supported Speeds");

	tmp = dmi_read_value(f, "Supported Speeds");

	if (tmp) {
		sprintf(value, "%s", tmp);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}


void process_dmi_type_5_types(tuple_t ** head, tuple_t ** log, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "sup_types");
	sprintf(description, "Supported Memory Types");

	tmp = dmi_read_value(f, "Supported Memory Types");

	if (tmp) {
		sprintf(value, "%s", tmp);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
	*log = enqueue_new_tuple_t(*log, title, value, id, description);
}


void process_dmi_type_5_voltage(tuple_t ** head, tuple_t ** log, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "mem_mod_volt");
	sprintf(description, "Memory Module Voltage (in V)");

	tmp = dmi_read_value(f, "Memory Module Voltage");

	if (tmp) {
		sprintf(value, "%s", tmp);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
	*log = enqueue_new_tuple_t(*log, title, value, id, description);
}


void process_dmi_type_6_socket(tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Socket Designation");

	if (tmp) {
		sprintf(module_socket, "%s", tmp);
		free(tmp);
	} else {
		sprintf(module_socket, "%s", "Unknown");
	}
}


void process_dmi_type_6_speed(tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_speed", module_socket);
	sprintf(description, "Module @ %s speed", module_socket);

	tmp = dmi_read_value(f, "Current Speed");

	if (tmp) {
		char ** split = split_string(tmp);

		if (split[0]) {
			id = atoi(split[0]);
			value = NULL;
		}

		if (split[1]) sprintf(description, "Module @ %s speed (in %s)", module_socket, split[1]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}


void process_dmi_type_6_type(tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_type", module_socket);
	sprintf(description, "Module @ %s type", module_socket);

	tmp = dmi_read_value(f, "Type");

	if (tmp) {
		char ** split = split_string (tmp);

		if (split[0]) sprintf(value, "%s", split[0]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}


void process_dmi_type_6_size(tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_size", module_socket);
	sprintf(description, "Module @ %s size", module_socket);

	tmp = dmi_read_value(f, "Installed Size");

	if (tmp) {
		char ** split = split_string (tmp);

		if (split[0]) {
			id = atoi(split[0]);
			value = NULL;
		}

		if (split[1]) sprintf(description, "Module @ %s size (in %s)", module_socket, split[1]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}


void process_dmi_type_17_socket(tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Locator");

	if (tmp) {
		sprintf(module_socket, "%s", tmp);
		free(tmp);
	} else {
		sprintf(module_socket, "%s", "Unknown");
	}
}


void process_dmi_type_17_speed (tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_speed", module_socket);
	sprintf(description, "Module @ %s speed", module_socket);

	tmp = dmi_read_value(f, "Speed");

	if (tmp) {
		char ** split = split_string(tmp);

		if (split[0]) {
			id = atoi(split[0]);

			if (atoi(split[0]) != 0) {
				id = atoi(split[0]);
				value = NULL;
			} else {
				sprintf(value, "%s", split[0]);
			}
		}

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}


void process_dmi_type_17_type (tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_type", module_socket);
	sprintf(description, "Module @ %s type", module_socket);

	tmp = dmi_read_value(f, "Type");

	if (tmp) {
		char ** split = split_string (tmp);

		if (split[0]) sprintf(value, "%s", split[0]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
	*log = enqueue_new_tuple_t(*log, title, value, id, description);
}


void process_dmi_type_17_ffactor (tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_ffactor", module_socket);
	sprintf(description, "Module @ %s form factor", module_socket);

	tmp = dmi_read_value(f, "Form Factor");

	if (tmp) {
		char ** split = split_string (tmp);

		if (split[0]) sprintf(value, "%s", split[0]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
	*log = enqueue_new_tuple_t(*log, title, value, id, description);
}


void process_dmi_type_17_size (tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_size", module_socket);
	sprintf(description, "Module @ %s size", module_socket);


	tmp = dmi_read_value(f, "Size");

	if (tmp) {
		char ** split = split_string (tmp);

		if (split[0]) {
			id = atoi(split[0]);
			value = NULL;
		}

		if (split[1]) sprintf(description, "Module @ %s size (in %s)", module_socket, split[1]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
	if (log){
		*log = enqueue_new_tuple_t(*log, title, value, id, description);
	}
}


void process_dmi_type_17_vendor (tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_vendor", module_socket);
	sprintf(description, "Module @ %s vendor", module_socket);

	tmp = dmi_read_value(f, "Manufacturer");

	if (tmp) {
		char ** split = split_string (tmp);

		sprintf(value, "%s", split[0]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}


void process_dmi_type_17_sn (tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_serial", module_socket);
	sprintf(description, "Module @ %s serial number", module_socket);

	tmp = dmi_read_value(f, "Serial Number");

	if (tmp) {
		char ** split = split_string (tmp);

		if (split[0]) sprintf(value, "%s", split[0]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}


void process_dmi_type_17_pn (tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(value, "%s", "Unknown");
	sprintf(title, "%s_part", module_socket);
	sprintf(description, "Module @ %s part number", module_socket);

	tmp = dmi_read_value(f, "Part Number");

	if (tmp) {
		char ** split = split_string (tmp);

		if (split[0]) sprintf(value, "%s", split[0]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}

void process_proc_meminfo_MemTotal(tuple_t ** head, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	// I hate gcc warnings about unused vars... ¬¬
	tmp = NULL;

	int id = -1;
	value = NULL;
	sprintf(title, "proc_meminfo_total_size");
	sprintf(description, "Total Memory Size by /proc/meminfo");

	if (! fscanf(f, "%d", &id)) {
		sprintf(value, "%s", "Unknown");
		id = -1;
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}
