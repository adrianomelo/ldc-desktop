#include "diag_usb.h"

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_diag_t * head = NULL;
	ldc_diag_t * tail = NULL;

	tail = new_ldc_diag_t("USB");
	head = enqueue_ldc_diag_t(head, tail);

	char cmd[200];
	FILE * cmd_output;

//	sprintf(cmd, "echo hello");
	sprintf(cmd, "lsusb | grep -v 'root hub' | cut -d ' ' -f 7- | sed ':a;$!N;s/\\n/; /g;ta'");
// lsusb | grep -v 'root hub' | cut -d " " -f 7- | sed ':a;$!N;s/\n/; /g;ta'
	execute_command_create_output(cmd, &cmd_output);

	process_lsusb_output(&tail->info, cmd_output);

	if (log){
		insert_diag_log(head);
	}

	return head;
}

void process_lsusb_output(tuple_t ** head, FILE * f){

	char name[100];
	char value[1000];
	int id;
	char  description[100];

	SETUP_TUPLE("plugged_devices", "NULL", -1, "Dispositivos USB");
	fscanf(f, "%[^\n]", value);

	*head = enqueue_new_tuple_t(*head, name, value, id, description);
}
