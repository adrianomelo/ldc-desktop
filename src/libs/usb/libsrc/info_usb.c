#include "info_usb.h"

/*
 * Identificar - Número e versão das portas USB, dispositivos conectados ao barramento, drivers (OHCI, UHCI, EHCI).
 *
 * sudo lsusb -v | grep iManufacturer | grep hcd | cut -d " " -f 15- | grep ohci -m 1
 * sudo lsusb -v | grep iManufacturer | grep hcd | cut -d " " -f 15- | grep uhci -m 1
 * sudo lsusb -v | grep iManufacturer | grep hcd | cut -d " " -f 15- | grep ehci -m 1
 *
 */

ldc_info_t * info(int log) {
	ldc_info_t * ret = new_ldc_info_t("USB");

	char name[100];
	char value[1000];
	int id;
	char  description[100];

	int i;

	//call function
	// lsusb | grep "root hub" | cut -d " " -f 9 | sed -n $=
	i = process_lsusb_numeric_info("lsusb | grep 'root hub' | cut -d ' ' -f 9 | sed -n $=");
	SETUP_TUPLE("usb_total", "NULL", i, "USB HUBs Count");
	add_info_tuple(ret, name, value, id, description);

	//call function
	// lsusb | grep "root hub" | cut -d " " -f 9 | grep 1.0 | sed -n $=
	i = process_lsusb_numeric_info("lsusb | grep 'root hub' | cut -d ' ' -f 9 | grep 1.0 | sed -n $=");
	SETUP_TUPLE("low_speed_total", "NULL", i, "USB 1.0 Count");
	add_info_tuple(ret, name, value, id, description);

	//call function
	// lsusb | grep "root hub" | cut -d " " -f 9 | grep 1.1 | sed -n $=
	i = process_lsusb_numeric_info("lsusb | grep 'root hub' | cut -d ' ' -f 9 | grep 1.1 | sed -n $=");
	SETUP_TUPLE("full_speed_total", "NULL", i, "USB 1.1 Count");
	add_info_tuple(ret, name, value, id, description);

	//call function
	// lsusb | grep "root hub" | cut -d " " -f 9 | grep 2.0 | sed -n $=
	i = process_lsusb_numeric_info("lsusb | grep 'root hub' | cut -d ' ' -f 9 | grep 2.0 | sed -n $=");
	SETUP_TUPLE("high_speed_total", "NULL", i, "USB 2.0 Count");
	add_info_tuple(ret, name, value, id, description);


	//call function
	// sudo lsusb -v | grep iProduct | grep "Host Controller" | cut -d " " -f 20 | grep OHCI | sed -n $=
	i = process_lsusb_numeric_info("sudo lsusb -v | grep iProduct | grep 'Host Controller' | cut -d ' ' -f 20 | grep OHCI | sed -n $=");
	SETUP_TUPLE("ohci_total", "NULL", i, "OHCI Host Controller Count");
	add_info_tuple(ret, name, value, id, description);

	//call function
	// sudo lsusb -v | grep iProduct | grep "Host Controller" | cut -d " " -f 20 | grep UHCI | sed -n $=
	i = process_lsusb_numeric_info("sudo lsusb -v | grep iProduct | grep 'Host Controller' | cut -d ' ' -f 20 | grep UHCI | sed -n $=");
	SETUP_TUPLE("uhci_total", "NULL", i, "UHCI Host Controller Count");
	add_info_tuple(ret, name, value, id, description);

	//call function
	// sudo lsusb -v | grep iProduct | grep "Host Controller" | cut -d " " -f 20 | grep EHCI | sed -n $=
	i = process_lsusb_numeric_info("sudo lsusb -v | grep iProduct | grep 'Host Controller' | cut -d ' ' -f 20 | grep EHCI | sed -n $=");
	SETUP_TUPLE("ehci_total", "NULL", i, "EHCI Host Controller Count");
	add_info_tuple(ret, name, value, id, description);

	if (log){
		insert_info_log(ret);
	}

	return ret;
}

int process_lsusb_numeric_info(char * cmd) {
	int i;
	FILE * f;

	execute_command_create_output(cmd, &f);

	if (fscanf(f, "%i", &i)){
		}
	else {
		i = 0;
	}

	if (i<0) i=0;

	return i;
}
