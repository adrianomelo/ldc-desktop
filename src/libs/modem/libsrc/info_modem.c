/*
 * RQF15.A : Identificar - Modelo, fabricante e driver.
 */

#include "info_modem.h"

ldc_info_t * info (int log) {
	ldc_info_t * ret = NULL;

	char * dev_file = calloc(sizeof(char), 100);

	// Try to fetch '/dev/modem' link target
	if (get_dev_modem_link(dev_file) > 0) {

		// Check for /dev/modem link and retrieve the target device.
		prepare_for_hwinfo_call(dev_file);

		// For each element of type 'hw_modem', 'info_libhd_modem' will be called
		ret = enqueue_ldc_info_t(ret, exec_hwinfo_info(NULL, hw_modem, &info_libhd_modem));

		// Revert changes done by prepare_for_hwinfo_call
		revert_prepare_for_hwinfo_call(dev_file);
	} else {
		char cmd[500];
		FILE * cmd_output;

		sprintf(cmd, "grep -v -E \"#\" /usr/share/misc/pci.ids | awk -f $LDC_PATH/src/libs/modem/modem.awk | grep -E \"`lspci -n | awk 'BEGIN{res=\"NONE:NONE\"};{res=sprintf(\"%%s|%%s\", res, $3)};END{print res}'`\"");
		execute_command_create_output(cmd, &cmd_output);

		ret = process_lspci_modem(cmd_output);
	}

	free(dev_file);

	if (log){
		insert_info_log(ret);
	}
	return ret;
}

/*
 * Escreve em dev_file o alvo do link /dev/modem, retornando 1 se tal link existe
 * ou 0, caso /dev/modem não seja encontrado.
 */
int get_dev_modem_link(char * dev_file) {
	int ret;
	char cmd[500];
	FILE * cmd_output;

	sprintf(cmd, "my_var=`ls --full-time /dev/modem 2> /dev/null`; if [ \"$my_var\" != \"\" ]; then echo $my_var | awk '{print \"/dev/\" $11}'; fi");
	execute_command_create_output(cmd, &cmd_output);

	ret = fscanf(cmd_output, "%s", dev_file);

	return ret;
}

/*
 * Se o dispositivo de modem for outro que não /dev/ttyS0, esta função
 * cria um link para este dispositivo em /dev/ttyS0, escrevendo o endereço
 * original do dispositivo em dev_file. O dispositivo em /dev/ttyS0, se
 * não é o modem, é movido para uma localização temporária. Para reverter
 * estas modificações, revert_prepare_for_hwinfo_call deve ser utilizado.
 */
void prepare_for_hwinfo_call(char * dev_file) {
	char cmd[500];
	FILE * cmd_output;

	if (strcmp(dev_file, "/dev/ttyS0") != 0) {
		sprintf(cmd, "if [ -e /dev/ttyS0 ]; then mv /dev/ttyS0 /dev/ttyS0.ldc_backup; fi; ln -sf %s /dev/ttyS0", dev_file);
		execute_command_create_output(cmd, &cmd_output);
	}
}

/*
 * Desfaz as alterações possivelmente feitas por prepare_for_hwinfo_call
 */
void revert_prepare_for_hwinfo_call(char * dev_file) {
	char cmd[500];
	FILE * cmd_output;

	if (strcmp(dev_file, "/dev/ttyS0") != 0) {
		sprintf(cmd, "if [ -e /dev/ttyS0.ldc_backup ]; then rm -f /dev/ttyS0; mv /dev/ttyS0.ldc_backup /dev/ttyS0; fi");
		execute_command_create_output(cmd, &cmd_output);
	}
}

ldc_info_t * process_lspci_modem(FILE * f) {
	ldc_info_t * ret = NULL;

	char str [500];

	if (fscanf(f, "%[^\n]", str) > 0) {
		int vendor_id;
		char vendor_name [300];

		int model_id;
		char model_name [300];

		char * str_ptr;

		str_ptr = strtok(str, ":");
		vendor_id = atoi(str_ptr);

		str_ptr = strtok(NULL, ":");
		model_id = atoi(str_ptr);

		str_ptr = strtok(NULL, ":");
		strcpy(vendor_name, str_ptr);

		str_ptr = strtok(NULL, ":");
		strcpy(model_name, str_ptr);

		ret = new_ldc_info_t("modem");

		// Vendor
		set_vendor(ret, "vendor", vendor_name, vendor_id, "Vendor");

		// Model
		set_model(ret, "device", model_name, model_id, "Model");

		// Device file
		ret->info = enqueue_new_tuple_t(ret->info, "dev_file", "Unknown", -1, "Device file");

		// Status
		ret->return_status = 1; // Success
	}

	return ret;
}

ldc_info_t * info_libhd_modem (ldc_info_t * log, hd_t * hd) {
	ldc_info_t * ret = new_ldc_info_t("modem");

	// Vendor
	set_vendor(ret, "vendor", hd->vendor.name, hd->vendor.id, "Vendor");

	// Model
	set_model(ret, "device", hd->device.name, hd->device.id, "Model");

	char dev_file[100];
	get_dev_modem_link(dev_file);

	// Device file
	ret->info = enqueue_new_tuple_t(ret->info, "dev_file", dev_file, -1, "Device file");

	// Status
	ret->return_status = 1; // Success

	return ret;
}
