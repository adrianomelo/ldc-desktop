#include "diag_network.h"

/*
 * RQF13.D : Diagnóstico - Informar se o link está ativo (up),
 * 						   informar o endereço de enlace (mac) e
 * 						   as configurações de rede (endereço IP, máscara de rede (netmask), endereço IP do
 *                                                    default gateway e endereço do(s) servidor(es) DNS).
 */

ldc_diag_t * diag(int log, ldc_info_t * info) {
	ldc_info_t * current_info;

	ldc_diag_t * head = NULL;
	ldc_diag_t * tail = NULL;


	for (current_info = info; current_info != NULL; current_info = current_info->next) {
		tail = new_ldc_diag_t("network");
		head = enqueue_ldc_diag_t(head, tail);

		// find the logical_name in info
		tuple_t * current_tuple;

		for (current_tuple = current_info->info; current_tuple != NULL && strcmp(current_tuple->name, "device_file") != 0; current_tuple = current_tuple->next);

		if (current_tuple) {
			char name[100];
			char value[1000];
			int id;
			char  description[100];

			char *net_dev = current_tuple->value;

			SETUP_TUPLE("device_file", net_dev, -1, "Netcard Device File");
			tail->info = enqueue_new_tuple_t(tail->info, name, value, id, description);

			//link ativo (up)
			net_link(net_dev, tail);

			//MAC
			net_mac(net_dev, tail);

			//IP e Netmask
			net_conf(net_dev, tail);

			//DNS
			net_dns(tail);

			//Default gateway
			net_gw(net_dev, tail);

		}
	}

	if (log){
		insert_diag_log(head);
	}

	return head;
}

void net_mac (char *net_dev, ldc_diag_t * current) {
	hd_data_t * hd_data;
	hd_t * hd;
	hd_res_t * res;
	int find = 0;

	hd_data = new_hd_data_t();
	hd = hd_list(hd_data, hw_network_ctrl, 1, NULL);

	for (; hd; hd = hd->next) {
		// Netcard Device File
		if (strcmp (hd->unix_dev_names->str, net_dev) == 0) {
			for (res = hd->res; res; res = res->next) {
				//MAC
				if (res->any.type == res_hwaddr) {
					add_diag_tuple(current, "mac", res->hwaddr.addr, -1, "MAC Address");
					find = 1;
				}
			}
		}
	}

	if (!find){
		add_diag_tuple(current, "mac", "Unknown", -1, "MAC Address");
	}

	free_hd_structs (hd_data, hd);
}

void net_conf(char *net_dev, ldc_diag_t * current) {
	char cmd[200];
	FILE * cmd_output = NULL;
	char ip_buffer[101];
	char mask_buffer[101];

	//IP e Netmask
	sprintf (cmd, "ifconfig %s | grep Bcast: | sed 's/[A-Za-z ]*:/:/g' | awk 'BEGIN { FS = \":\" } ; {print $2 \" \" $4}'", net_dev);
	execute_command_create_output(cmd, &cmd_output);

	sprintf(ip_buffer, "Unknown");
	sprintf(mask_buffer, "Unknown");
	fscanf(cmd_output, "%s %s", ip_buffer, mask_buffer);

	add_diag_tuple(current, "ip", ip_buffer, -1, "IP Address");
	add_diag_tuple(current, "netmask", mask_buffer, -1, "Netmask");
}

void net_link(char *net_dev, ldc_diag_t * current) {
	char cmd[100];
	FILE * cmd_output = NULL;
	char r_buffer[101];
	int result = 0;

	sprintf (cmd, "ifconfig %s | grep 'UP'", net_dev);
	execute_command_create_output(cmd, &cmd_output);

	while (!feof(cmd_output)) {
		if (fgets (r_buffer, 100, cmd_output)){
			if (strstr(r_buffer, "UP") != NULL){
				result = 1;
			}
		}
	}

	add_diag_tuple(current, "link_up", NULL, result, "Link UP");
}

void net_dns(ldc_diag_t * current) {
	char cmd [100];
	FILE * cmd_output = NULL;
	char r_buffer[101];
	char dns_name[50];
	int i = 1;

	sprintf (cmd, "cat /etc/resolv.conf | grep \"nameserver\" | grep -v \"#\" | awk '{print $2}'");
	execute_command_create_output(cmd, &cmd_output);

	while(fscanf(cmd_output, "%s", r_buffer) != EOF){
		sprintf(dns_name, "dns_server_%d", i);
		add_diag_tuple(current, dns_name, r_buffer, -1, "DNS Server");
		i++;
	}
	if (i == 1){ //Não encontrou nenhum DNS server (não entrou no while)
		add_diag_tuple(current, "dns_server", "Unknown", -1, "DNS Server");
	}
}

void net_gw(char * net_dev, ldc_diag_t * current) {
	char cmd [100];
	FILE * cmd_output = NULL;
	char r_buffer[50];

	sprintf(cmd, "route -n | grep %s | grep G | awk '{print $2}'", net_dev);
	execute_command_create_output(cmd, &cmd_output);

	sprintf(r_buffer, "Unknown");

	fscanf(cmd_output, "%s", r_buffer);

	add_diag_tuple(current, "gateway", r_buffer, -1, "Default Gateway");
}

