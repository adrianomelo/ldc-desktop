#include "info_motherboard.h"


ldc_info_t * info (int log) {
	hd_data_t * hd_data = new_hd_data_t();
	hd_t *hd;
	hd_smbios_t *sm;

	hd = hd_list(hd_data, hw_bios, 1, NULL);

	ldc_info_t * tail = new_ldc_info_t("motherboard");
	ldc_info_t * log_tuple = new_ldc_info_t("motherboard");

	if(!hd_data->smbios) {
		fprintf(stderr, "Problema na Placa Mãe\n");
		return NULL;
	} else if(! (sm = hd_data->smbios)) {
		fprintf(stderr, "Problema na Placa Mãe 2\n");
		return NULL;
	}

	for(; sm; sm = sm->next) {
		switch(sm->any.type) {
			case sm_biosinfo: //bios info
				insert_tuple(tail, log_tuple, "bios_vendor", sm->biosinfo.vendor, -1, "BIOS - Vendor");
				insert_tuple(tail, log_tuple, "bios_version", sm->biosinfo.version, -1, "BIOS - Version");
				insert_tuple(tail, log_tuple, "bios_date", sm->biosinfo.date, -1, "BIOS - Date");
				break;
			case sm_boardinfo: //motherboard info
				if (sm->boardinfo.manuf) {
					set_vendor (tail, "vendor", sm->boardinfo.manuf, -1, "Vendor");
					set_vendor (log_tuple, "vendor", sm->boardinfo.manuf, -1, "Vendor");
				} else {
					set_vendor (tail, "vendor", "Unknown", -1, "Vendor");
					set_vendor (log_tuple, "vendor", "Unknown", -1, "Vendor");
				}
				if (sm->boardinfo.product){
					set_model (tail, "device", sm->boardinfo.product, -1, "Model");
					set_model (log_tuple, "device", sm->boardinfo.product, -1, "Model");
				} else {
					set_model (tail, "device", "Unknown", -1, "Model");
					set_model (log_tuple, "device", "Unknown", -1, "Model");
				}
				insert_tuple(tail, log_tuple, "version", sm->boardinfo.version, -1, "Version");
				insert_tuple(tail, NULL, "serial", sm->boardinfo.serial, -1, "Serial");
				break;
			default:
				break;
		}

	}

	free_hd_structs (hd_data, hd);

	//chipset
	hd_data = new_hd_data_t();
	hd = hd_list(hd_data, hw_bridge, 1, NULL);

	for(; hd; hd = hd->next) {
		if (hd->sub_class.id == 0){ //Host bridge subclass id
			insert_tuple(tail, log_tuple, "chipset_device", hd->device.name, hd->device.id, "Chipset - Device");
			insert_tuple(tail, log_tuple,  "chipset_vendor", hd->vendor.name, hd->vendor.id, "Chipset - Vendor");
			if(hd->driver_modules) {
				str_list_t * mod_list = hd->driver_modules;
				for (; mod_list; mod_list = mod_list->next){
					insert_tuple(tail, log_tuple,  "chipset_driver_modules", mod_list->str, -1, "Chipset - Driver Modules");
				}
			 }
		}
	}

	tail->return_status = 1;

	free_hd_structs (hd_data, hd);

	if (log){
		insert_info_log(log_tuple);
	}

	return tail;
}

void insert_tuple(ldc_info_t * tail, ldc_info_t * log_tuple, const char * attr_name, const char * attr_value, const int id, const char * attr_desc){
	if (attr_value){
		add_info_tuple(tail, attr_name, attr_value, id, attr_desc);
		if (log_tuple){
			add_info_tuple(log_tuple, attr_name, attr_value, id, attr_desc);
		}
	} else {
		add_info_tuple(tail, attr_name, "Unknown", id, attr_desc);
		if (log_tuple){
			add_info_tuple(log_tuple, attr_name, "Unknown", id, attr_desc);
		}
	}
}

