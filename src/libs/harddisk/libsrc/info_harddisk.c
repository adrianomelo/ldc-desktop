#include "info_harddisk.h"

/*
 * RQF07.A : Identificar - Fabricante, produto, modelo, tamanho, device file (logical name) e driver.
 */

ldc_info_t * info(int log) {
	ldc_info_t * ret = NULL;

	// For each element of type 'hw_disk', 'info_libhd_harddisk' will be called
	ret = enqueue_ldc_info_t(ret, exec_hwinfo_info(NULL, hw_disk, &info_libhd_harddisk));

	if (log){
		insert_info_log(ret);
	}

	return ret;
}

ldc_info_t * info_libhd_harddisk(ldc_info_t * log, hd_t * hd) {
	ldc_info_t * ret = new_ldc_info_t("harddisk");

	hd_res_t * current;

	FILE * smartctl_output = NULL;

	char name[100];
	char value[1000];
	int id;
	char  description[100];

	// Vendor
	SETUP_TUPLE("vendor", hd->vendor.name, -1, "Vendor");
	set_vendor(ret, name, value, id, description);

	// Model
	SETUP_TUPLE("device", hd->model, -1, "Model");
	set_model(ret, name, value, id, description);

	// Bus
	SETUP_TUPLE("bus", hd->bus.name, -1, "Bus type");
	ret->info = enqueue_new_tuple_t(ret->info, name, value, id, description);

	// Device File
	SETUP_TUPLE("device_file", hd->unix_dev_name, -1, "Device file");
	ret->info = enqueue_new_tuple_t(ret->info, name, value, id, description);

	// Driver
	char * drivers = hd_join("|", hd->drivers);
	if (strstr(drivers, "usb-storage") != NULL) {
		free_ldc_info_t(ret);
		free(drivers);
		return NULL;
	}
 	SETUP_TUPLE("drivers", drivers, -1, "Device drivers");
	ret->info = enqueue_new_tuple_t(ret->info, name, value, id, description);
	free(drivers);


	// Model Family
	char cmd[200];
	sprintf(cmd, "smartctl --info %s | grep \"Model Family\" | cut -d \" \" -f 7-", hd->unix_dev_name);
	execute_command_create_output (cmd, &smartctl_output);
	process_smartctl_ModelFamily(&ret->info, smartctl_output);

	// Size
	SETUP_TUPLE("size", "NULL", -1, "Size (in MB)");
	current = hd->res;
	for (current = hd->res; current != NULL && current->size.type != res_size && current->size.unit != size_unit_sectors; current = (hd_res_t *) current->next);
	if (current->size.type == res_size && current->size.unit == size_unit_sectors && current->size.val1 && current->size.val2) {
		id = (current->size.val1 * current->size.val2) / (1024 * 1024);
	}
	ret->info = enqueue_new_tuple_t(ret->info, name, NULL, id, description);

	return ret;
}

void process_smartctl_ModelFamily(tuple_t ** head, FILE * f) {
	char name[100];
	char value[1000];
	int id;
	char  description[100];

	SETUP_TUPLE("model_family", "Unknown", -1, "Model family");
	fscanf(f, "%[^\n]", value);

	*head = enqueue_new_tuple_t(*head, name, value, id, description);
}
