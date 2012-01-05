#include "info_wireless.h"


// TOFIX: do this using libhd, not parsing hwinfo output
ldc_info_t * info(int log){
	ldc_info_t * ret = NULL;

	ret = enqueue_ldc_info_t(ret, exec_hwinfo_info(NULL, hw_network_ctrl, &info_wireless));

	if (log){
		insert_info_log(ret);
	}

	return ret;
}


ldc_info_t * info_wireless (ldc_info_t * log, hd_t * hd) {
	ldc_info_t * current = NULL;

	//Solução para eliminar placas wireless não classificadas pelo hwinfo
	if (hd->unix_dev_names != NULL && strstr(hd->unix_dev_names->str, "eth") == NULL) {
		hd_res_t *res;
		char buffer [200];
		str_list_t *ptr;

		current = new_ldc_info_t("wireless");

		if (hd->vendor.name != NULL){
			set_vendor(current, "vendor", hd->vendor.name, -1, "Vendor");
		} else {
			set_vendor(current, "vendor", "Unknown", -1, "Vendor");
		}
		if (hd->device.name != NULL){
			set_model(current, "device", hd->device.name, -1, "Model");
		} else {
			set_model(current, "device", "Unknown", -1, "Model");
		}

		//Driver
		if (hd->driver_modules){
			insert_tuple(current, "driver", hd->driver_modules->str, -1, "Netcard Driver");
		} else {
			insert_tuple(current, "driver", "Unknown", -1, "Netcard Driver");
		}

		//Device File
		insert_tuple(current, "device_file", hd->unix_dev_names->str, -1, "Netcard Device File");

		for(res = hd->res; res; res = res->next) {
			if (res->any.type == res_wlan){
				if(res->wlan.channels) {
					buffer[0] = '\0';
					for (ptr = res->wlan.channels; ptr; ptr = ptr->next) {
						sprintf (buffer, "%s %s", buffer, ptr->str);
					}
					insert_tuple(current, "channels", buffer, -1, "Channels");
				} else{
					insert_tuple(current, "channels", "Unknown", -1, "Channels");
				}
				if(res->wlan.enc_modes) {
					buffer[0] = '\0';
					for (ptr = res->wlan.enc_modes; ptr; ptr = ptr->next) {
						sprintf (buffer, "%s %s", buffer, ptr->str);
					}
					insert_tuple(current, "encryption_modes", buffer, -1, "Encryption Modes");
				} else {
					insert_tuple(current, "encryption_modes", "Unknown", -1, "Encryption Modes");
				}
				if(res->wlan.auth_modes) {
					buffer[0] = '\0';
					for (ptr = res->wlan.auth_modes; ptr; ptr = ptr->next) {
						sprintf (buffer, "%s %s", buffer, ptr->str);
					}
					insert_tuple(current, "authentication_modes", buffer, -1, "Authentication Modes");
				} else {
					insert_tuple(current, "authentication_modes", "Unknown", -1, "Authentication Modes");
				}
			}
		}

		operation_mode (hd->unix_dev_names->str, current);

	}

	return current;
}

void operation_mode(char *net_dev, ldc_info_t * current){
	char cmd[200];
	FILE * cmd_output = NULL;
	char mode_buffer[101];

	sprintf(cmd, "iwconfig %s 2> /dev/null | grep 802.11 | cut -d ' ' -f 7", net_dev);
	execute_command_create_output(cmd, &cmd_output);

	sprintf(mode_buffer, "Unknown");
	fscanf(cmd_output, "%s", mode_buffer);
	add_info_tuple(current, "wifimode", mode_buffer, -1, "Wi-Fi 802.11 Op. Mode");
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
