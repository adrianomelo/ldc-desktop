#include "diag_harddisk.h"

/*
 * RQF07.C : Diagn�stico - Informar os particionamentos,  o espa�o livre e a temperatura dos discos. Caso os discos possuam o recurso .SMART., executar o teste .overall-health self-assesment..
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_info_t * current_info;

	ldc_diag_t * head = NULL;
	ldc_diag_t * tail = NULL;

	int num_part;

	for (current_info = info; current_info != NULL; current_info = current_info->next) {
		tail = new_ldc_diag_t("harddisk");
		head = enqueue_ldc_diag_t(head, tail);

		// find the logical_name in info
		tuple_t * current_tuple;

		for (current_tuple = current_info->info; current_tuple != NULL && strcmp(current_tuple->name, "device_file") != 0; current_tuple = current_tuple->next);

		if (current_tuple) {
			char name[100];
			char value[1000];
			int id;
			char  description[100];

			char cmd[300];
			FILE * cmd_output;

			SETUP_TUPLE("device_file", current_tuple->value, -1, "Logical name");
			tail->info = enqueue_new_tuple_t(tail->info, name, value, id, description);

			// Partitions
			sprintf(cmd, "parted -m %s print | grep -v BYT | grep -v dev | cut -d ':' -f 1,4,5 | sed 's/:/ /g'", current_tuple->value);
			execute_command_create_output(cmd, &cmd_output);
			num_part = process_parted_partition_info(&tail->info, cmd_output);

			if (num_part > 0) {
				// Partition free space & mounting point
				// char * escaped_device_file = strrplc(current_tuple->value, "/", "\\/");
				char device[50];

				strcpy(device, current_tuple->value);

				char * last_dev_part = NULL;
				char * cur = strtok(device, "/");

				while (cur != NULL) {
					last_dev_part = cur;
					cur = strtok(NULL, "/");
				}

				sprintf(cmd, "df -hT --exclude-type=tmpfs | grep %s | awk '{print $1,$5,$7}' | sed 's/\\/dev\\/%s//g'", current_tuple->value, last_dev_part);
				execute_command_create_output(cmd, &cmd_output);
				process_df_partition_info(&tail->info, cmd_output);

				if (enable_smart(current_tuple->value)) {
					// Temperature
					sprintf(cmd, "smartctl -A %s | grep -i \"Temperature\" | awk '{print $10}'", current_tuple->value);
					execute_command_create_output (cmd, &cmd_output);
					process_smartctl_Temperature(&tail->info, cmd_output);

					// Overall Test
					sprintf(cmd, "MY_VAR=`smartctl -H %s | grep PASSED`; if [ MY_VAR != '' ]; then echo '1'; fi", current_tuple->value);
					execute_command_create_output (cmd, &cmd_output);
					process_smartctl_OverallTest(&tail->info, cmd_output);
				}
			}
		}
	}

	if (log){
		insert_diag_log(head);
	}
	return head;
}

int enable_smart(char *dev_file){
	int result = 0;

	char * cmd = NULL;
	FILE * tmp_file = NULL;
	char * tmp_file_name = NULL;
	char r_buffer[101];

	tmp_file_name = create_tmp_file(&tmp_file);

	if (tmp_file_name){
		cmd = (char *)calloc(strlen(dev_file) + 100, sizeof(char));
		strcpy (cmd, "smartctl --smart=on ");
		strcat (cmd, dev_file);

		execute_command (cmd, tmp_file_name);

		while (!feof(tmp_file)) {
			if (fgets (r_buffer, 100, tmp_file)){
				if (strstr(r_buffer, "SMART Enabled") != NULL){
					result = 1; //the disk have SMART support and it is enabled
				}
			}
		}

		free(cmd);
	}

	return result;
}

void process_smartctl_Temperature(tuple_t ** head, FILE * f) {
	char name[100];
	char value[1000];
	int id;
	char  description[100];

	SETUP_TUPLE("temperature", "NULL", -1, "Temperatura");
	fscanf(f, "%d", &id);

	*head = enqueue_new_tuple_t(*head, name, NULL, id, description);
}

void process_smartctl_OverallTest(tuple_t ** head, FILE * f) {
	char name[100];
	char value[1000];
	int id;
	char  description[100];

	SETUP_TUPLE("overall_health_test", "NULL", -1, "Overall-health self-assessment test");
	fscanf(f, "%d", &id);

	*head = enqueue_new_tuple_t(*head, name, NULL, id, description);
}

int process_parted_partition_info(tuple_t ** head, FILE * f) {
	char name[100];
	char value[1000];
	int id;
	char description[100];

	char lineBuffer[1000];

	int partNum;
	char partSize[100];
	char filesystem[100];

	int count = 0;

	while(! feof(f) && 1 == fscanf(f, "%[^\n]", lineBuffer) && getc(f)) {
		if (3 == sscanf(lineBuffer, "%d %s %s", &partNum, partSize, filesystem)) {
			count++;

			SETUP_TUPLE("part_X_size", partSize, -1, "Partição - Tamanho");
			sprintf(name, "part_%d_size", partNum);
			*head = enqueue_new_tuple_t(*head, name, partSize, id, description);

			SETUP_TUPLE("part_X_filesystem", filesystem, -1, "Partição - Sistema de arquivos");
			sprintf(name, "part_%d_filesystem", partNum);
			*head = enqueue_new_tuple_t(*head, name, value, id, description);
		}
	}

	return count;
}

void process_df_partition_info(tuple_t ** head, FILE * f) {
	char name[100];
	char value[1000];
	int id;
	char description[100];

	int partNum;
	char partFree[100];
	char partMount[200];

	while(! feof(f) && 3 == fscanf(f, "%d %s %s", &partNum, partFree, partMount)) {
		SETUP_TUPLE("part_#_free_size", partFree, -1, "Partição - Tamanho Livre");
		sprintf(name, "part_%d_free_size", partNum);
		*head = enqueue_new_tuple_t(*head, name, value, id, description);

		SETUP_TUPLE("part_#_mounting_point", partMount, -1, "Partição - Ponto de montagem");
		sprintf(name, "part_%d_mounting_point", partNum);
		*head = enqueue_new_tuple_t(*head, name, value, id, description);
	}
}
