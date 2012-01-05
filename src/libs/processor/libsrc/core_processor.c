#include "core_processor.h"

void process_dmi_type_4_version(tuple_t ** head, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Version");

	if (tmp) {
		sprintf(value, "%s", tmp);
		dmi_free(tmp);
	} else {
		sprintf(value, "%s", "Unknown");
	}

	sprintf(title, "version");
	sprintf(description, "DMI Processor Name");

	*head = enqueue_new_tuple_t(*head, title, value, -1, description);
}


void process_dmi_type_4_socket(tuple_t ** head, tuple_t ** log, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Socket Designation");

	if (tmp) {
		sprintf(value, "%s", tmp);
		dmi_free(tmp);
	} else {
		sprintf(value, "%s", "Unknown");
	}

	sprintf(title, "socket_type");
	sprintf(description, "Socket Type");

	*head = enqueue_new_tuple_t(*head, title, value, -1, description);
	*log = enqueue_new_tuple_t(*log, title, value, -1, description);
}


void process_dmi_type_4_voltage(tuple_t ** head, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Voltage");

	if (tmp) {
		sprintf(value, "%s", tmp);
		dmi_free(tmp);
	} else {
		sprintf(value, "%s", "Unknown");
	}

	sprintf(title, "voltage");
	sprintf(description, "Voltage");

	*head = enqueue_new_tuple_t(*head, title, value, -1, description);
}


void process_dmi_type_4_clock(tuple_t ** head, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(title, "cpu_clock");
	value = NULL;
	tmp = dmi_read_value(f, "Current Speed");

	if (tmp) {
		char ** split = split_string (tmp);
		id = atoi(split[0]);
		sprintf(description, "CPU clock (in %s)", split[1]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
}


void process_dmi_type_4_fsb(tuple_t ** head, tuple_t ** log, FILE * f) {
	PROCESS_DMI_LOCAL_VARS;

	int id = -1;
	sprintf(title, "fsb_clock");
	value = NULL;
	tmp = dmi_read_value(f, "External Clock");

	if (tmp) {
		char ** split = split_string (tmp);
		id = atoi(split[0]);
		sprintf(description, "FSB clock (in %s)", split[1]);

		dmi_free(tmp);
	}

	*head = enqueue_new_tuple_t(*head, title, value, id, description);
	*log = enqueue_new_tuple_t(*log, title, value, id, description);
}


void process_dmi_type_7_socket(tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Socket Designation");

	if (tmp) {
		sprintf(module_socket, "%s", tmp);
		free(tmp);
	} else {
		sprintf(module_socket, "%s", "Unknown");
	}
}


void process_dmi_type_7_installed_size(tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Installed Size");

	if (tmp) {
		char ** split = split_string (tmp);

		sprintf(title, "%s_size", module_socket);
		int id = atoi(split[0]);
		sprintf(description, "%s size (in %s)", module_socket, split[1]);

		*head = enqueue_new_tuple_t(*head, title, NULL, id, description);
		*log = enqueue_new_tuple_t(*log, title, NULL, id, description);
		dmi_free(tmp);
	}
}


void process_dmi_type_7_associativity(tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Associativity");

	if (tmp) {
		sprintf(title, "%s_associativity", module_socket);
		sprintf(description, "%s associativity", module_socket);

		*head = enqueue_new_tuple_t(*head, title, tmp, -1, description);
		dmi_free(tmp);
	}
}


void process_dmi_type_7_operational_mode(tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Operational Mode");

	if (tmp) {
		sprintf(title, "%s_opmode", module_socket);
		sprintf(description, "%s operational mode", module_socket);

		*head = enqueue_new_tuple_t(*head, title, tmp, -1, description);
		*log = enqueue_new_tuple_t(*log, title, tmp, -1, description);
		dmi_free(tmp);
	}
}


void process_dmi_type_7_supported_types(tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Supported SRAM Types");

	if (tmp) {
		sprintf(title, "%s_sup_sram_types", module_socket);
		sprintf(description, "%s supported SRAM types", module_socket);

		*head = enqueue_new_tuple_t(*head, title, tmp, -1, description);
		*log = enqueue_new_tuple_t(*log, title, tmp, -1, description);
		dmi_free(tmp);
	}
}


void process_dmi_type_7_err_correction_type(tuple_t ** head, FILE * f, char * module_socket) {
	PROCESS_DMI_LOCAL_VARS;

	tmp = dmi_read_value(f, "Error Correction Type");

	if (tmp) {
		sprintf(title, "%s_err_correction_type", module_socket);
		sprintf(description, "%s error correction type", module_socket);

		*head = enqueue_new_tuple_t(*head, title, tmp, -1, description);
		dmi_free(tmp);
	}
}
