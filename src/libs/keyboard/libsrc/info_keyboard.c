#include "info_keyboard.h"

/*
 * RQF17.A : Identificar - Configuracao e tipo.
 */

ldc_info_t * info (int log) {
	ldc_info_t * ret = NULL;

	// For each element of type 'hw_keyboard', 'info_libhd_keyboard' will be called
	ret = enqueue_ldc_info_t(ret, exec_hwinfo_info(NULL, hw_keyboard, &info_libhd_keyboard));

	if (log){
		insert_info_log(ret);
	}
	return ret;
}

ldc_info_t * info_libhd_keyboard (ldc_info_t * log, hd_t * hd) {
	ldc_info_t * ret = new_ldc_info_t("keyboard");

	char name[100];
	char * value; char _value[200]; value = _value;
	int id;
	char  description[100];

	char cmd [500];
	FILE * xorg_output;

	set_vendor (ret, "vendor", hd->vendor.name, hd->vendor.id, "Vendor");
	set_model (ret, "device", hd->device.name, hd->device.id, "Model");

	// Bus type
	sprintf(name, "bus");
	sprintf(value, hd->bus.name);
	id = hd->bus.id;
	sprintf(description, "Bus type");

	ret->info = enqueue_new_tuple_t(ret->info, name, value, id, description);

	// Device file
	sprintf(name, "device");
	sprintf(value, hd->unix_dev_names->str);
	id = -1;
	sprintf(description, "Device file");

	ret->info = enqueue_new_tuple_t(ret->info, name, value, id, description);

	sprintf(cmd, "grep -v -E \"#|$^\" /etc/X11/xorg.conf | awk -f $LDC_PATH/src/libs/keyboard/keyboard.awk | grep -E \"XkbRules|XkbModel|XkbLayout\" | awk '{ print $3 }' | sed 's/\"//g'");
	execute_command_create_output(cmd, &xorg_output);
	process_xorg_xkb(&ret->info, xorg_output);

	ret->return_status = 1;

	return ret;
}

void process_xorg_xkb(tuple_t ** head, FILE * f) {
	char name[100];
	char * value; char _value[200]; value = _value;
	int id;
	char  description[100];

	// XKB Rules
	sprintf(name, "xkb_rules");
	id = -1;
	sprintf(description, "XKB Rules");

	if (fscanf(f, "%s", value) == EOF) {
		sprintf(value, "Unknown");
	}

	*head = enqueue_new_tuple_t(*head, name, value, id, description);

	// XKB Model
	sprintf(name, "xkb_model");
	id = -1;
	sprintf(description, "XKB Model");

	if (fscanf(f, "%s", value) == EOF) {
		sprintf(value, "Unknown");
	}

	*head = enqueue_new_tuple_t(*head, name, value, id, description);

	// XKB Layout
	sprintf(name, "xkb_layout");
	id = -1;
	sprintf(description, "XKB Layout");

	if (fscanf(f, "%s", value) == EOF) {
		sprintf(value, "Unknown");
	}

	*head = enqueue_new_tuple_t(*head, name, value, id, description);
}
