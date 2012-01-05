#include "info_sound.h"

/*
 * RQF11.A : Identificar - Fabricante, produto, modelo e driver.
 */

ldc_info_t * info (int log) {
	hd_data_t * hd_data = new_hd_data_t();
	hd_t *hd;

	hd = hd_list(hd_data, hw_sound, 1, NULL);

	ldc_info_t * head = NULL;
	ldc_info_t * tail = NULL;

	for(; hd; hd = hd->next) {
		if (! head) {
			head = new_ldc_info_t("sound");
			tail = head;
		} else {
			tail->next = new_ldc_info_t("sound");
			tail = tail->next;
		}

		//vendor
		if (hd->vendor.name){
			set_vendor (tail, "vendor", hd->vendor.name, hd->vendor.id, "Vendor");
		} else {
			set_vendor (tail, "vendor", "Unknown", -1, "Vendor");
		}

		//device
		if (hd->device.name){
			set_model (tail, "device", hd->device.name, hd->device.id, "Device");
		} else {
			set_model (tail, "device", "Unknown", -1, "Device");
		}

		//model
		if (hd->model){
			add_info_tuple(tail, "model", hd->model, -1, "Model");
		} else {
			add_info_tuple(tail, "model", "Unknown", -1, "Model");
		}

		//driver modules; driver active; device id
		if (hd->driver_info){
			driver_info_t *di;
			for(di = hd->driver_info; di; di = di->next) {
				if (di->any.type == di_module) {
					str_list_t * mod_list = di->module.names;
					add_info_tuple(tail, "driver_active", NULL, di->module.active, "Driver Active");

					for (; mod_list; mod_list = mod_list->next){
						add_info_tuple(tail, "driver_modules", mod_list->str, -1, "Driver Modules");
						device_id(tail, mod_list->str);
					}
				}
			}
		} else {
			add_info_tuple(tail, "driver_modules", "Unknown", -1, "Driver Modules");
			add_info_tuple(tail, "driver_active", NULL, -1, "Driver Active");
		}

		tail->return_status = 1;
	}

	free_hd_structs (hd_data, hd);

	if (log){
		insert_info_log(head);
	}

	return head;
}

void device_id(ldc_info_t * tail, char *mod){
	char cmd [100];
	FILE * cmd_output = NULL;
	char r_buffer[50];

	sprintf(cmd, "cat /proc/asound/modules | grep %s | awk '{print $1}'", mod);
	execute_command_create_output(cmd, &cmd_output);

	sprintf(r_buffer, "Unknown");

	fscanf(cmd_output, "%s", r_buffer);

	add_info_tuple(tail, "device_id", r_buffer, -1, "Device ID");
}
