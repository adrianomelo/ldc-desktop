#include "diag_usbstorage.h"

/*
 * RQF10.C Diagnostico - Verificar montagem.
 * RQF10.D Diagnostico - Verificar particionamento.
 * RQF10.E Diagnostico - Se o sistema de arquivos permitir, executar o comando fsck correspondente.
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_info_t * current_info;

	ldc_diag_t * head = NULL;
	ldc_diag_t * tail = NULL;

	for (current_info = info; current_info != NULL; current_info = current_info->next) {
		tail = new_ldc_diag_t("usbstorage");
		head = enqueue_ldc_diag_t(head, tail);

		// find the logical_name in info
		tuple_t * current_tuple;

		for (current_tuple = current_info->info; current_tuple != NULL && strcmp(current_tuple->name, "device_file") != 0; current_tuple = current_tuple->next);
			if (current_tuple) {
				char name[100];
				char value[1000];
				int id;
				char  description[100];

				int* part_list = get_part_list(current_info);
				int part_result = check_part(part_list);
				SETUP_TUPLE("partition_check", "NULL", part_result, "Partition Check");
				tail->info = enqueue_new_tuple_t(tail->info, name, value, id, description);

				int mount_result = mount_test(current_tuple->value, part_list);
				SETUP_TUPLE("mount_test", "NULL", mount_result, "Mount Test");
				tail->info = enqueue_new_tuple_t(tail->info, name, value, id, description);

				int fsck_result = fsck_test(current_tuple->value, part_list);
				SETUP_TUPLE("fsck_test", "NULL", fsck_result, "Fsck Test");
				tail->info = enqueue_new_tuple_t(tail->info, name, value, id, description);
			}
	}

	if (log){
		insert_diag_log(head);
	}

	return head;
}


int mount_test(char *dev_file, int* part_list){
	int result = 1;
	int i = 0;
	int size = sizeof( part_list ) / sizeof( int );
	char * cmd = NULL;
	FILE * tmp_file = NULL;
	char * tmp_file_name = NULL;
	char r_buffer[101];

	tmp_file_name = create_tmp_file(&tmp_file);

	if (tmp_file_name){
		for (i = 0; i < size && part_list[i] > 0; i++ ){
			cmd = (char *)calloc(strlen(dev_file) + 100, sizeof(char));
			sprintf (cmd, "umount %s%d", dev_file, part_list[i]);
			execute_command (cmd, tmp_file_name);
			sprintf (cmd, "mkdir /mnt/tmp");
			execute_command (cmd, tmp_file_name);
			sprintf(cmd, "mount %s%d /mnt/tmp", dev_file, part_list[i]);
			execute_command (cmd, tmp_file_name);

			while (!feof(tmp_file)) {
				if (!fgets (r_buffer, 100, tmp_file)){
					if (strstr(r_buffer, "mount:") != NULL){
						result = 0;
					}
				}
			}
			sprintf (cmd, "umount %s%d", dev_file, part_list[i]);
			execute_command (cmd, tmp_file_name);
			free(cmd);
		}
	}

	return result;
}

int * get_part_list(ldc_info_t * current_info){
	int *result = (int *)calloc(10, sizeof(int));
	int size = 10;
	char part_name[50];
	tuple_t * current_tuple;
	int i = 0;

	for (current_tuple = current_info->info; current_tuple != NULL; current_tuple = current_tuple->next){
		sprintf(part_name, "partition_%d_fileType", current_tuple->id);
		if (strcmp(current_tuple->name, part_name) == 0){
			if (i < size){
				result[i] = current_tuple->id;
				i++;
			}
		}
	}

	return result;
}

int check_part(int * part_list){
	int result = 0;
	int i;
	int end = 0;
	int size = sizeof( part_list ) / sizeof( int );

	for (i = 0; i < size && !end; i++){
		if (part_list[i] != 0){
			result = 1;
			end = 1;
		}
	}

	return result;
}

int fsck_test(char *dev_file, int* part_list){
	int result = 0;
	int i = 0;
	int size = sizeof( part_list ) / sizeof( int );
	char * cmd = NULL;
	FILE * tmp_file = NULL;
	char * tmp_file_name = NULL;
	char r_buffer[101];

	tmp_file_name = create_tmp_file(&tmp_file);

	if (tmp_file_name){
		for (i = 0; i < size && part_list[i] > 0; i++ ){
			cmd = (char *)calloc(strlen(dev_file) + 100, sizeof(char));
			sprintf (cmd, "fsck %s%d", dev_file, part_list[i]);
			execute_command (cmd, tmp_file_name);

			while (!feof(tmp_file)) {
				if (!fgets (r_buffer, 100, tmp_file)){
					if (strstr(r_buffer, "files") != NULL && strstr(r_buffer, "clusters") != NULL){
						result = 1;
					}
				}
			}

			free(cmd);
		}
	}

	return result;
}
