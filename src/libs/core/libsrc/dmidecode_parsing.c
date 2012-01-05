#include "dmidecode_parsing.h"

char * dmi_next_type(FILE * f, int type) {
	int found = 0;

	char r_buffer[501];

	int n_handler = -1;
	int n_type = -1;
	int n_size = -1;

	char * ret = NULL;

	while (!found && fgets(r_buffer, 500, f) != NULL) {
		if (sscanf(r_buffer, "Handle %x, DMI type %d, %d bytes", &n_handler, &n_type, &n_size) == 3) {
			if (n_type == type) {
				found = 1;
			}
		}
	}

	if (found) {
		ret = (char *) malloc (sizeof(char) * (strlen(r_buffer) + 1));
		strcpy(ret, r_buffer);
	}

	return ret;
}

char * dmi_read_value(FILE * f, char * label) {
	int found = 0;
	int block_end = 0;

	char r_buffer[500];
	char r_format_single[500];
	char r_format_multi[500];

	char n_value[500];

	char * ret = NULL;

	fpos_t start_block;

	fgetpos(f, &start_block);

	sprintf(r_format_single, "\t%s: %%[^\n]", label);
	sprintf(r_format_multi, "\t%s%%[^\n]", label);

	while (!found && !block_end && fgets(r_buffer, 500, f) != NULL) {
		if (r_buffer[0] == '\n') {
			block_end = 1;
//			printf("Block-end!\n");
		} else if (sscanf(r_buffer, r_format_single, &n_value) == 1) {
			found = 1;
		} else if (sscanf(r_buffer, r_format_multi, &n_value) == 1) {
			fpos_t start;

			fgetpos(f, &start);

			if (n_value[0] == ':' && (n_value[1] == '\0' || n_value[1] == '\n')) {
				int values_end = 0;

				char line_value[500];

				n_value[0] = '\0';

				while (!values_end && fgets(r_buffer, 500, f) != NULL) {
					sscanf(r_buffer, "\t\t%[^\n]", line_value);

					if (strstr(line_value, ":") == NULL) {
						sprintf(n_value, "%s%s%s", n_value, line_value, "|");
					} else {
						values_end = 1;
					}
				}

				found = 1;

				fsetpos(f, &start);
			}
		}
	}

	if (found) {
		ret = (char *) malloc (sizeof(char) * (strlen(n_value) + 1));
		strcpy(ret, n_value);
	}

	fsetpos(f, &start_block);

	return ret;
}


void dmi_free(void * mem) {
	free (mem);
}


void execute_dmidecode (FILE ** tmp_file) {
	char * tmp_file_name = NULL;

	tmp_file_name = create_tmp_file(tmp_file);


	// TODO: aprimorar essa execucao pra que o resultado contenha menos linhas
	execute_command ("/usr/sbin/dmidecode", tmp_file_name);
}


void process_dmi_type(int type, FILE * tmp_file, tuple_t ** head, tuple_t ** log, void (* dmi_type_processor)(tuple_t **, tuple_t **, FILE *), char * error_msg) {
	char * dmiType = dmi_next_type (tmp_file, type);

	if (dmiType != NULL) {
		while (dmiType != NULL) {
			dmi_free(dmiType);
			(* dmi_type_processor)(head, log, tmp_file);

			dmiType = dmi_next_type (tmp_file, type);
		}
	} else {
		printf("%s", error_msg);
	}

	rewind(tmp_file);
}
