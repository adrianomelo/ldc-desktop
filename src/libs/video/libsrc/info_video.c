#include "info_video.h"


ldc_info_t * info (int log) {
	ldc_info_t * head = NULL;

	head = enqueue_ldc_info_t(head, videocard_module());

	if (log){
		insert_info_log(head);
	}
	return head;
}

ldc_info_t * videocard_module () {
	hd_data_t * hd_data;
	hd_t * hd;

	ldc_info_t * head = NULL;

	int primary_display = -1;

	hd_data = new_hd_data_t();
	hd = hd_list(hd_data, hw_display, 1, NULL);

	primary_display =  hd_display_adapter(hd_data);

	for (; hd; hd = hd->next) {
		if (primary_display != -1 && primary_display == hd->idx){
			ldc_info_t * current = new_ldc_info_t("videocard");

			driver_info_t * di;

			str_list_t * tmp_sl;

			char buffer[100];


			if (hd->vendor.name != NULL){
				set_vendor (current, "vendor", hd->vendor.name, hd->vendor.id, "Vendor");
			} else {
				set_vendor (current, "vendor", "Unknown", -1, "Vendor");
			}
			if (hd->model != NULL){
				set_model (current, "device", hd->model, hd->device.id, "Model");
			} else {
				set_model (current, "device", "Unknown", -1, "Model");
			}

			if (hd->driver_info) {
				di = hd->driver_info;
				for (; di; di = di->next) {
					if (di->any.type == di_x11){
						// XFree86 Server Module
						insert_tuple(current, "xf86_module_name", di->x11.server, -1, "XFree86 Server Module");
		//
						// 3D Support
						insert_tuple(current, "xf86_module_3d", NULL, di->x11.x3d, "XFree86 Server Module 3D Support");
		//
						// Extensions
						if (di->x11.extensions) {
							buffer[0] = '\0';

							for (tmp_sl = di->x11.extensions; tmp_sl; tmp_sl = tmp_sl->next) {
								sprintf (buffer, "%s%s|", buffer, tmp_sl->str);
							}
						}
						insert_tuple(current, "xf86_module_ext", buffer, -1, "XFree86 Server Module Extensions");

					} else {
						add_info_tuple(current, "xf86_module_name", "Unknown", -1, "XFree86 Server Module");
						add_info_tuple(current, "xf86_module_3d", NULL, -1, "XFree86 Server Module 3D Support");
						add_info_tuple(current, "xf86_module_ext", "Unknown", -1, "XFree86 Server Module Extensions");
					}

				}
			} else {
				add_info_tuple(current, "xf86_module_name", "Unknown", -1, "XFree86 Server Module");
				add_info_tuple(current, "xf86_module_3d", NULL, -1, "XFree86 Server Module 3D Support");
				add_info_tuple(current, "xf86_module_ext", "Unknown", -1, "XFree86 Server Module Extensions");
			}

			current->return_status = 1;

			head = enqueue_ldc_info_t(head, current);
		}
	}

	free_hd_structs (hd_data, hd);

	return head;
}

void insert_tuple(ldc_info_t * tail, const char * attr_name, const char * attr_value, const int id, const char * attr_desc){
	if (attr_value){
		add_info_tuple(tail, attr_name, attr_value, id, attr_desc);
	} else if (id != -1) {
		add_info_tuple(tail, attr_name, attr_value, id, attr_desc);
	}
	else {
		add_info_tuple(tail, attr_name, "Unknown", -1, attr_desc);
	}
}

