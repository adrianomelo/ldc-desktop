#include "ldc_log.h"

void insert_diag_log(ldc_diag_t *diag){
	ldc_diag_t * current = diag;

	//criar ou abrir arquivo para leitura
	FILE * log = fopen(LOG_FILE,"a+");

	//para cada tuple
	while (current != NULL) {
		insert_device (log, current->lib_name, "diag", current->info, NULL, NULL);
		current = current->next;
		fprintf(log,"\n\n");
	}

	fclose(log);
}

void insert_info_log(ldc_info_t * info){
	ldc_info_t * current = info;

	//criar ou abrir arquivo para leitura
	FILE * log = fopen(LOG_FILE,"a+");

	//para cada tuple
	while (current != NULL) {
		insert_device (log, current->lib_name, "info", current->info, current->vendor, current->model);
		current = current->next;
		fprintf(log,"\n\n");
	}

	fclose(log);
}

void insert_device(FILE *log, char *lib_name, char *type, tuple_t * info_list, tuple_t * vendor, tuple_t * model){
	char device_result[5000];
	char tmp[300];

	//chamar método que irá iserir data, hora
	insert_date_time(tmp);
	fprintf(log, "DATA#HORA");
	sprintf(device_result, tmp);

	//iserir libname
	sprintf(tmp, "#%s", lib_name);
	fprintf(log, tmp);
	strcat(device_result, tmp);

	//inserir 'info'/'diag'
	sprintf(tmp, "#%s", type);
	fprintf(log, tmp);
	strcat(device_result, tmp);

	//procurar no arquivo header os itens e imprimir o valor de cada um no log
	print_itens(log, info_list, vendor, model, device_result);

}

void insert_date_time(char *date_time){
	struct tm *now = NULL;
	time_t time_value = 0;
	char buffer[80];

	time_value = time(NULL);
	now = localtime(&time_value);

	strftime (buffer,80,"%d/%m/%y", now);
	sprintf(date_time, buffer);

	strftime (buffer,80,"#%H:%M:%S", now);
	strcat(date_time, buffer);


}

void print_itens (FILE * log, tuple_t * info_list, tuple_t * vendor, tuple_t * model, char *device_result){
	char result [300];

	if (vendor){
		get_value(vendor, result);
		print_item(log, vendor->name, result, device_result);
	}
	if (model){
		get_value(model, result);
		print_item(log, model->name, result, device_result);
	}
	while (info_list != NULL) {
		get_value(info_list, result);
		print_item(log, info_list->name, result, device_result);
		info_list = info_list->next;
	}
	fprintf(log, "\n%s", device_result);
}

void print_item (FILE *log, char * name, char * value, char * device_result){
	char tmp [300];

	fprintf(log, "#%s", name);
	sprintf(tmp, "#%s", value);
	strcat(device_result, tmp);
}

void get_value(tuple_t *tuple, char * value){
	value[0] = '\0'; //Inicializando para string vazias
	if(strcmp(tuple->value,"NULL") != 0){
		if (tuple->id != -1) {
			sprintf(value, "%s (0x%X)", tuple->value, tuple->id);
		} else {
			sprintf(value, "%s", tuple->value);
		}
	} else {
		sprintf(value, "%d", tuple->id);
	}
}


