#include "diag_video.h"


ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_diag_t * ret = NULL;
	ldc_info_t * current_info;

	for (current_info = info; current_info != NULL; current_info = current_info->next) {
		ret = enqueue_ldc_diag_t(ret, exec_hwinfo_diag(log, hw_monitor, &monitor_module));
	}

	if (log){
		insert_diag_log(ret);
	}

	return ret;
}

ldc_diag_t * monitor_module (int log, hd_t * hd) {
	ldc_diag_t * current = new_ldc_diag_t("monitor");

	hd_res_t * res;

	driver_info_t * di = hd->driver_info;
	monitor_info_t * mi = hd->detail->monitor.data;

	char buffer[100];

	if (hd->vendor.name){
		add_diag_tuple (current, "vendor", hd->vendor.name, hd->vendor.id, "Vendor");
	} else {
		add_diag_tuple (current, "vendor", "Unknown", -1, "Vendor");
	}
	if (hd->device.name){
		add_diag_tuple (current, "model", hd->device.name, hd->device.id, "Model");
	} else {
		add_diag_tuple (current, "model", "Unknown", -1, "Model");
	}

	// Supported Resolutions
	for (res = hd->res; res; res = res->next) {

		if (res->any.type == res_size) {
			if (res->size.val1 && res->size.val2){
				sprintf(buffer, "%ux%u", (unsigned int) res->size.val1, (unsigned int) res->size.val2);
				add_diag_tuple(current, "screen_size", buffer, -1, "Screen Size");
			} else {
				add_diag_tuple(current, "screen_size", "Unknown", -1, "Screen Size");
			}
		}
	}

	// Avaliable detailed timings
	if (mi) {

		// Current Resolution
		if (mi->width && mi->height) {
			sprintf(buffer, "%ux%u", mi->width, mi->height);
			add_diag_tuple(current, "cur_resolution", buffer, -1, "Current Resolution");
		} else {
			add_diag_tuple(current, "cur_resolution", "Unknown", -1, "Current Resolution");
		}
	}


	// Avaliable driver diag
	if (di) {

		// Max. Resolution
		if (di->display.width && di->display.height) {
			sprintf(buffer, "%ux%u", di->display.width, di->display.height);
			add_diag_tuple(current, "max_resolution", buffer, -1, "Maximum Resolution");
		} else {
			add_diag_tuple(current, "max_resolution", "Unknown", -1, "Maximum Resolution");
		}


		// Vert. Sync Range
		if (di->display.min_vsync && di->display.max_vsync) {
			sprintf(buffer, "%u-%u Hz", di->display.min_vsync, di->display.max_vsync);
			add_diag_tuple(current, "vsync_range", buffer, -1, "Vertical Sync Range");
		} else {
			add_diag_tuple(current, "vsync_range", "Unknown", -1, "Vertical Sync Range");
		}


		// Hor. Sync Range
		if (di->display.min_hsync && di->display.max_hsync) {
			sprintf(buffer, "%u-%u Hz", di->display.min_hsync, di->display.max_hsync);
			add_diag_tuple(current, "hsync_range", buffer, -1, "Horizontal Sync Range");
		} else{
			add_diag_tuple(current, "vsync_range", "Unknown", -1, "Vertical Sync Range");
		}
	}

	current->return_status = 1;


	return current;
}
