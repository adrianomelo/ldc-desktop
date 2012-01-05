#include "info_network.h"

/*
 * RQF13.A : Identificar - Produto, fabricante, driver, device file e velocidade.
 */

ldc_info_t * info (int log) {
	ldc_info_t * head = NULL;
	ldc_info_t * current = NULL;
	ldc_info_t * tail = NULL;

	current = exec_hwinfo_info_restricted(log, hw_network_ctrl, hw_wlan, &network_module);

	head = current;
	tail = current;

	if (log){
		insert_info_log(head);
	}
	return head;
}


ldc_info_t * network_module (int log, hd_t * hd) {
	ldc_info_t * current = NULL;

	//Solução para eliminar placas wireless não classificadas pelo hwinfo
	if (hd->unix_dev_names != NULL && strstr(hd->unix_dev_names->str, "wlan") == NULL) {
		current = new_ldc_info_t("network");

		char buffer[100];

		char cmd[300];
		FILE * cmd_output;

		set_vendor(current, "vendor", hd->vendor.name, hd->vendor.id, "Vendor");
		set_model(current, "device", hd->device.name, hd->device.id, "Model");

		// Netcard Driver
		add_info_tuple(current, "driver", hd->driver_modules->str, -1, "Netcard Driver");


		// Netcard Device File
		add_info_tuple(current, "device_file", hd->unix_dev_names->str, -1, "Netcard Device File");


		// Network Speed
		sprintf(cmd, "ethtool %s | grep Speed | awk '{print $2}'", hd->unix_dev_names->str);
		execute_command_create_output(cmd, &cmd_output);

		fscanf(cmd_output, "%s", buffer);

		if (buffer[strlen(buffer) - 1] == '!') {
			buffer[strlen(buffer) - 1] = '\0';
		}

		add_info_tuple(current, "speed", buffer, -1, "Netcard Speed");


		// Link State
		sprintf(cmd, "ethtool %s | grep Link | awk '{print $3}'", hd->unix_dev_names->str);
		execute_command_create_output(cmd, &cmd_output);

		fscanf(cmd_output, "%s", buffer);

		int link_state = 0;

		if (strcmp("yes", buffer) == 0) {
			link_state = 1;
		}

		add_info_tuple(current, "link_state", NULL, link_state, "Netcard Link State");


		current->return_status = 1;

	}
	return current;
}
