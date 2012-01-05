#include "info_dvdcd.h"

/*
 * RQF08.A : Identificar - Fabricante, modelo, driver, dispositivo e mídias suportadas.
 */

ldc_info_t * info (int log) {
	hd_data_t * hd_data = new_hd_data_t();
	hd_t *hd;

	hd = hd_list(hd_data, hw_cdrom, 1, NULL);

	ldc_info_t * head = NULL;
	ldc_info_t * tail = NULL;

	char buffer[500];

	for(; hd; hd = hd->next) {
		if (! head) {
			head = new_ldc_info_t("dvdcd");
			tail = head;
		} else {
			tail->next = new_ldc_info_t("dvdcd");
			tail = tail->next;
		}

		set_vendor(tail, "vendor", hd->vendor.name, hd->vendor.id, "Vendor");
		set_model(tail, "model", hd->device.name, hd->device.id, "Model");

		add_info_tuple(tail, "device", hd->unix_dev_names->str, -1, "Device file");
		add_info_tuple(tail, "drivers", format_drivers(hd, buffer), -1, "Drivers");
		add_info_tuple(tail, "medias", format_medias(hd, buffer), -1, "Supported media types");

		tail->return_status = 1;
	}

	if (log){
		insert_info_log(head);
	}

	free_hd_structs (hd_data, hd);

	return head;
}


char * format_drivers(hd_t * hd, char * buffer) {
	char * pt_char = hd_join("|", hd->drivers);

	sprintf (buffer, "%s", pt_char);

	free(pt_char);

	return buffer;
}

char * format_medias(hd_t * hd, char * buffer) {
	buffer[0] = '\0';

	sprintf(buffer, "%s%s", buffer, hd->is.cdr ? "CD-R|" : "");
	sprintf(buffer, "%s%s", buffer, hd->is.cdrw ? "CD-RW|" : "");
	sprintf(buffer, "%s%s", buffer, hd->is.dvd ? "DVD|" : "");
	sprintf(buffer, "%s%s", buffer, hd->is.dvdr ? "DVD-R|" : "");
	sprintf(buffer, "%s%s", buffer, hd->is.dvdrw ? "DVD-RW|" : "");
	sprintf(buffer, "%s%s", buffer, hd->is.dvdpr ? "DVD+R|" : "");
	sprintf(buffer, "%s%s", buffer, hd->is.dvdprw ? "DVD+RW|" : "");
	sprintf(buffer, "%s%s", buffer, hd->is.dvdprdl ? "DVD+DL|" : "");
	sprintf(buffer, "%s%s", buffer, hd->is.dvdram ? "DVDRAM|" : "");

	return buffer;
}
