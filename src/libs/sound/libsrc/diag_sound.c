#include "diag_sound.h"

/*
 * RQF11.C : Diagnóstico - Utilizar o pacote alsa para aumentar/diminuir o volume e
 * 				habilitar/desabilitar a placa de som. Informar o resultado obtido através da
 * 				utilização do pacote alsa. Caso haja algum problema, sugerir ao usuário que
 * 				execute o teste de compatibilidade, e solicitar que ele cheque as caixas de som.
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_info_t * current_info;

	ldc_diag_t * head = NULL;
	ldc_diag_t * tail = NULL;

	for (current_info = info; current_info != NULL; current_info = current_info->next) {
		tail = new_ldc_diag_t("sound");
		head = enqueue_ldc_diag_t(head, tail);

		// find the logical_name in info
		tuple_t * current_tuple;
		for (current_tuple = current_info->info; current_tuple != NULL && strcmp(current_tuple->name, "device_id") != 0; current_tuple = current_tuple->next);

		if (current_tuple != NULL && current_tuple->value != NULL && strcmp(current_tuple->value, "Unknown") != 0 && strcmp(current_tuple->value, "-1") != 0){
			volume_test(tail, current_tuple->value);
			mute_unmute_test(tail, current_tuple->value);
		} else {
			add_diag_tuple(tail, "volume_test", NULL, 0, "Volume Test");
			add_diag_tuple(tail, "mute_unmute_test", NULL, 0, "Mute/Unmute Test");
		}
	}

	if (log){
		insert_diag_log(head);
	}

	return head;
}

void volume_test(ldc_diag_t * current, char *dev){
	int result = set_volume(dev, 40) && set_volume(dev, 80);
	add_diag_tuple(current, "volume_test", NULL, result, "Volume Test");

}

int set_volume (char *dev, int vol){
	int result = 0;
	char cmd [100];
	FILE * cmd_output = NULL;
	char r_buffer[1000];

	sprintf(cmd, "amixer -c %s set Master %d%%", dev, vol);
	execute_command_create_output(cmd, &cmd_output);

	while (!feof(cmd_output)) {
		if (fgets (r_buffer, 100, cmd_output)){
			if ((strstr(r_buffer, "Front Left:") != NULL) || (strstr(r_buffer, "Front Right:") != NULL) ){
				result = 1;
			}
		}
	}
	return result;
}

void mute_unmute_test(ldc_diag_t * current, char *dev){
	int result = mute(dev) && unmute(dev);
	add_diag_tuple(current, "mute_unmute_test", NULL, result, "Mute/Unmute Test");
}

int mute (char *dev){
	int result = exec_amixer(dev, "mute", "[off]", "PCM") || exec_amixer(dev, "mute", "[off]", "Master");
	return result;
}

int unmute (char *dev){
	int result = exec_amixer(dev, "unmute", "[on]", "PCM") || exec_amixer(dev, "unmute", "[on]", "Master");
	return result;
}

int exec_amixer(char *dev, char *type_test, char *strcmp, char *type_dev){
	int result = 0;
	char cmd [200];
	FILE * cmd_output = NULL;
	char r_buffer[1000];

	sprintf(cmd, "amixer -c %s sset %s %s", dev, type_dev, type_test);
	execute_command_create_output(cmd, &cmd_output);

	while (!feof(cmd_output)) {
		if (fgets (r_buffer, 100, cmd_output)){
			if (strstr(r_buffer, strcmp) != NULL ){
				result = 1;
			}
		}
	}
	return result;
}
