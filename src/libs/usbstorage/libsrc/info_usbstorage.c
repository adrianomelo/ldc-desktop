#include "info_usbstorage.h"


ldc_info_t * info (int log) {
	ldc_info_t * head = NULL;
	ldc_info_t * tail = NULL;

	hd_data_t * hd_data = new_hd_data_t();
	hd_t *hd;
	hd_res_t *res;

	hd = hd_list(hd_data, hw_usb, 1, NULL);

	for(; hd; hd = hd->next) {
		if (hd->hw_class){
			if (hd->hw_class == hw_disk){ //apenas os discos usb
				if (hd->device.name && (strstr(hd->device.name, "Card") == NULL && strstr(hd->device.name, "card") == NULL )){
					if (! head) {
						head = new_ldc_info_t("pendrive");
						tail = head;
					} else {
						tail->next = new_ldc_info_t("pendrive");
						tail = tail->next;
					}

					if(hd->vendor.name){
						set_vendor (tail, "vendor", hd->vendor.name, -1, "Vendor");
					} else {
						set_vendor (tail, "vendor", "Unknown", -1, "Vendor");
					}
					if (hd->device.name){
						set_model (tail, "device", hd->device.name, -1, "Model");
					} else {
						set_model (tail, "device", "Unknown", -1, "Model");
					}

					if(hd->drivers) {
						char *s = hd_join("; ", hd->drivers);
						add_info_tuple(tail, "driver", s, -1, "Driver");
						free(s);
					} else {
						add_info_tuple(tail, "driver", "Unknown", -1, "Driver");
					}
					if (hd->unix_dev_name){
						add_info_tuple(tail, "device_file", hd->unix_dev_name, -1, "Device File");
						partitions_info(hd->unix_dev_name, tail);
					} else {
						add_info_tuple(tail, "device_file", "Unknown", -1, "Device File");
					}
					int speed = -1;
					int size = -1;
					for(res = hd->res; res; res = res->next) {
						switch(res->any.type) {
							case res_baud:
								//convertendo para Mbps (divisão por 10^6)
								speed = res->baud.speed/1000000;
								break;
							case res_size:
								if(res->size.unit == size_unit_sectors){
									//FIXME: adicionado 1 e feito floor => usar ceil
									size = ((res->size.val1*res->size.val2)/1073741824.0) + 1; //byte => GB
								}
								break;
							default:
								break;
						}
					}
					add_info_tuple(tail, "speed", NULL, speed, "Speed (in Mbps)");
					add_info_tuple(tail, "Size", NULL, size, "Size (in GB)");
				}
			}
		}
	}

	if (tail) {
		tail->return_status = 1;
	} else {
		//printf("Não foi detectado nenhum pen drive!!\n");

		//FIXME: deve ser padronizado o retorno
		//head = new_ldc_info_t("pendrive");
	}

	free_hd_structs (hd_data, hd);

	if (log){
		insert_info_log(head);
	}

	return head;
}

void insert_tuple (ldc_info_t * tail, char *name, char *value, int id, char* desc, void (* type_process)(ldc_info_t *, char *,char *, int, char*)){
	char *in_value = "Unknown";
	int in_id = -1;
	if (value){
		in_value = value;
	}
	if (id > 0){
		in_id = id;
	}

	(* type_process) (tail, name, value, id, desc);
}


void partitions_info (char *devFile, ldc_info_t * tail){
	int numpart = 0;
	char * cmd = NULL;
	FILE * tmp_file = NULL;
	char * tmp_file_name = NULL;
	char r_buffer[101];
	char *tokens = NULL;
	char name[100];

	tmp_file_name = create_tmp_file(&tmp_file);

	if (tmp_file_name){
		cmd = (char *)calloc(strlen(devFile) + 50, sizeof(char));
		strcpy (cmd, "parted -m ");
		strcat (cmd, devFile);
		//strcat (cmd, "/dev/sda");
		strcat (cmd, " print");

		execute_command (cmd, tmp_file_name);

		while (!feof(tmp_file)) {
			if (fgets (r_buffer, 100, tmp_file)){
				tokens = strtok(r_buffer, ":");
				int num_token = 0;
				int end = 0;
				while (!end && tokens != NULL) {
				    if (num_token == 0){
				    	if (isdigit(tokens[0])){
				    		numpart++;
				    	} else {
				    		end = 1;
				    	}
				    }
				    if (num_token == 3){
						sprintf(name, "partition_%d_size", numpart);
						add_info_tuple(tail, name, tokens, numpart, "Partição e Tamanho");
					}
					if (num_token == 4){
						sprintf(name, "partition_%d_fileType", numpart);
						add_info_tuple(tail, name, tokens, numpart, "Partição e Sistema de arquivos");
						end = 1;
					}
				    tokens = strtok (NULL, ":");
				    num_token++;
				}
			}
		}

		free(cmd);
	}
}
