#include "info_mouse.h"


ldc_info_t * info (int log) {
	hd_data_t * hd_data = new_hd_data_t();
	hd_t *hd;

	hd = hd_list(hd_data, hw_mouse, 1, NULL);

	driver_info_t * di;

	ldc_info_t * head = NULL;
	ldc_info_t * tail = NULL;

	for(; hd; hd = hd->next) {
		if (! head) {
			head = new_ldc_info_t("mouse");
			tail = head;
		} else {
			tail->next = new_ldc_info_t("mouse");
			tail = tail->next;
		}

		di = hd->driver_info;

		set_vendor (tail, "vendor", hd->vendor.name, hd->vendor.id, "Vendor");
		set_model (tail, "device", hd->device.name, hd->device.id, "Model");

		add_info_tuple(tail, "bus", hd->bus.name, hd->bus.id, "Bus type");
		add_info_tuple(tail, "device", hd->unix_dev_names->str, -1, "Device file");

		add_info_tuple(tail, "buttons", NULL, di->mouse.buttons, "# of buttons");
		add_info_tuple(tail, "wheels", NULL, di->mouse.wheels, "Has wheels");
		add_info_tuple(tail, "gpm", di->mouse.gpm, -1, "GPM protocol");
		add_info_tuple(tail, "xf86", di->mouse.xf86, -1, "XFree86 protocol");

		tail->return_status = 1;
	}

	free_hd_structs (hd_data, hd);

	if (log){
		insert_info_log(head);
	}

	return head;
}

