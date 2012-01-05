#include "ldc_core.h"
#include <stdio.h>
#include <string.h>


hd_data_t * new_hd_data_t () {
	hd_data_t *hd_data;
	hd_data = calloc(1, sizeof *hd_data);

	return hd_data;
}


void free_hd_structs (hd_data_t * hd_data, hd_t * hd) {
	hd_free_hd_list(hd);          /* free it */
	hd_free_hd_data(hd_data);

	free(hd_data);
}


void execute_command (char * cmd, char * output_file) {
	char full_cmd[300];

	if (output_file) {
		sprintf (full_cmd, "%s > %s 2>&1", cmd, output_file); //Solu��o provis�ria (output error)
	} else {
		sprintf (full_cmd, "%s", cmd);
	}

	system(full_cmd);
}


void execute_command_create_output (char * cmd, FILE ** tmp_file) {
	char * tmp_file_name = NULL;

	tmp_file_name = create_tmp_file(tmp_file);

	execute_command (cmd, tmp_file_name);
}


ldc_info_t * exec_hwinfo_info (ldc_info_t * log, hd_hw_item_t type, ldc_info_t * (* type_process)(ldc_info_t *, hd_t*)) {
	hd_data_t * hd_data;
	hd_t * hd;

	ldc_info_t * head = NULL;
	ldc_info_t * tail = NULL;

	hd_data = new_hd_data_t();
	hd = hd_list(hd_data, type, 1, NULL);

	for (; hd; hd = hd->next) {
		tail = (* type_process)(log, hd);
		if (tail != NULL) {
			head = enqueue_ldc_info_t(head, tail);
		}
	}

	free_hd_structs (hd_data, hd);

	return head;
}

ldc_info_t * exec_hwinfo_info_restricted (int log, hd_hw_item_t type, hd_hw_item_t undesired_type, ldc_info_t * (* type_process)(int, hd_t*)) {
	hd_data_t * hd_data;
	hd_t * hd;
	hd_t * restriction;
	int can_enqueue = 1;

	ldc_info_t * head = NULL;
	ldc_info_t * tail = NULL;

	hd_data = new_hd_data_t();
	hd = hd_list(hd_data, type, 1, NULL);
	restriction = hd_list(hd_data, undesired_type, 1, NULL);

	for (; hd; hd = hd->next) {
		hd_t * restr_head = restriction;
		can_enqueue = 1;

		for (; restriction; restriction = restriction->next){
			if(!strcmp(restriction->udi, hd->udi)){
				can_enqueue = 0;
				break;
			} else {
				break;
			}
		}
		restriction = restr_head;

		if (can_enqueue){
			tail = (* type_process)(log, hd);
			if (tail != NULL) {
				head = enqueue_ldc_info_t(head, tail);
			}
		}
	}

	free_hd_structs (hd_data, hd);

	return head;
}


ldc_diag_t * exec_hwinfo_diag (int log, hd_hw_item_t type, ldc_diag_t * (* type_process)(int, hd_t*)) {
	hd_data_t * hd_data;
	hd_t * hd;

	ldc_diag_t * head = NULL;
	ldc_diag_t * tail = NULL;

	hd_data = new_hd_data_t();
	hd = hd_list(hd_data, type, 1, NULL);

	for (; hd; hd = hd->next) {
		tail = (* type_process)(log, hd);
		head = enqueue_ldc_diag_t(head, tail);
	}

	free_hd_structs (hd_data, hd);

	return head;
}


char ** split_string(char * str) {
	int n = 20;
	int i = 0;
	char ** ret = (char **) malloc (sizeof (char *) * n);
	char * current = NULL;

	current = strtok(str, " ");

	for (i = 0; i < n && current != NULL; i++) {
		ret[i] = current;

		current = strtok(NULL, " ");
	}


	// Removing first element ' ' and '\t'
	current = ret[0];

	if (current[0] == ' ' || current[0] == '\t') {
		int counter = 1;
		int i = 0;

		while (current[counter] == ' ' || current[counter] == '\t') {
			counter ++;
		}

		for (i = 0; i < (strlen(current) - counter); i ++) {
			if (i < counter);
			current[i] = current[i + counter];
		}

		current[i] = '\0';
	}

	// Removing last element '\n'
	current = ret[i-1];

	if (current[strlen(current) - 1] == '\n') {
		current[strlen(current) - 1] = '\0';
	}

	// Last array element == NULL
	ret[i] = (char *) 0;

	return ret;
}


char * create_tmp_file (FILE ** f) {
	char * ret = (char *) malloc (sizeof (char) * 35);

	int fd = -1;

	strcpy(ret, "/var/tmp/libldc_tmp_file.XXXXXX");

	if ((fd = mkstemp(ret)) == -1 || (*f = fdopen(fd, "w+")) == NULL) {
		if (fd != -1) {
			// unlink(tmp_file_name);
			fclose(*f);
		}

		fprintf(stderr, "%s: %s\n", ret, strerror(errno));
	}

	return ret;
}
