#include "info_webcam.h"

// TOFIX: no 'goto', please
ldc_info_t * info (int log) {
	ldc_info_t * retorno = NULL;

	int i;
	int num_udis = -1;
	char **udis;
	DBusError error;

	LibHalContext *hal_ctx;
	hal_ctx = libhal_ctx_new();
	dbus_error_init (&error);

	if (hal_ctx == NULL){
		// printf("Could not create libhal context.\n");
		dbus_error_free (&error);
		goto fallback;
	}

	if (!libhal_ctx_set_dbus_connection (hal_ctx, dbus_bus_get (DBUS_BUS_SYSTEM, &error))){
		// printf("libhal_ctx_set_dbus_connection: %s, %s.\n", error.name, error.message);
		dbus_error_free (&error);
		goto fallback;
	}

	if (!libhal_ctx_init (hal_ctx, &error)){
		if (dbus_error_is_set (&error)){
			// printf("libhal_ctx_init: %s, %s.\n", error.name, error.message);
			dbus_error_free (&error);
		}
		printf ("Could not initialise connection to hald (hal daemon).\n");
		goto fallback;
	}

	udis = libhal_find_device_by_capability(hal_ctx, "video4linux", &num_udis, &error);

	if (dbus_error_is_set (&error)){
		// printf("libhal_find_device_by_capability: %s, %s.\n", error.name, error.message);
		dbus_error_free (&error);
	}

	for (i = 0; i < num_udis; i++){

		ldc_info_t * webcam_ret = new_ldc_info_t("webcam");

		char	*property_name;
		char	*parent_udi = NULL;
		char	*subsystem = NULL;
		int sprintf_ok = 0;

		int vendor_id = -1;
		int product_id = -1;
		char *vendor;
		char *product;
		char *model;
		char *driver;
		char *device_file;
		int return_status = 0;

		parent_udi = libhal_device_get_property_string (hal_ctx, udis[i], "info.parent", &error);
		if (parent_udi != NULL){
			// printf("UDI: %s \n", udis[i]);
			// printf("info.parent: %s \n", parent_udi);
			subsystem = libhal_device_get_property_string (hal_ctx, parent_udi, "info.subsystem", NULL);
			if (subsystem == NULL) continue; //TODO check bug possibilities here

			property_name = malloc (100);
			sprintf_ok = sprintf(property_name, "%s.%s", subsystem, "vendor_id");
			vendor_id = libhal_device_get_property_int (hal_ctx, parent_udi, property_name, &error);
			if (dbus_error_is_set (&error)){
				// printf("error getting vendor id: %s, %s.\n", error.name, error.message);
				dbus_error_free (&error);
				vendor_id = -1;
				return_status = 1;
			} else {
				// printf ("Vendor id: %i\n", vendor_id);
			}
			free(property_name);

			property_name = malloc (100);
			sprintf_ok = sprintf(property_name, "%s.%s", subsystem, "vendor");
			vendor = libhal_device_get_property_string (hal_ctx, parent_udi, property_name, &error);
			if (dbus_error_is_set (&error)){
				// printf("error getting vendor: %s, %s.\n", error.name, error.message);
				dbus_error_free (&error);
				vendor = "";
				return_status = 1;
			} else {
				//printf ("Vendor: %s\n", vendor);
			}
			free(property_name);

			property_name = malloc (100);
			sprintf_ok = sprintf(property_name, "%s.%s", subsystem, "product_id");
			product_id = libhal_device_get_property_int (hal_ctx, parent_udi, property_name, &error);
			if (dbus_error_is_set (&error)){
				// printf("error getting product id: %s, %s.\n", error.name, error.message);
				dbus_error_free (&error);
				product_id = -1;
				return_status = 1;
			} else {
				//printf ("Product id: %i\n", product_id);
			}
			free(property_name);

			property_name = malloc (100);
			sprintf_ok = sprintf(property_name, "%s.%s", subsystem, "product");
			product = libhal_device_get_property_string (hal_ctx, parent_udi, property_name, &error);
			if (dbus_error_is_set (&error)){
				// printf("error getting product: %s, %s.\n", error.name, error.message);
				dbus_error_free (&error);
				product = "";
				return_status = 1;
			} else {
				//printf ("Product: %s\n", product);
			}
			free(property_name);

			property_name = malloc (100);
			sprintf_ok = sprintf(property_name, "%s.%s", subsystem, "interface.description");
			model = libhal_device_get_property_string (hal_ctx, parent_udi, property_name, &error);
			if (dbus_error_is_set (&error)){
				// printf("error getting model/interface description: %s, %s.\n", error.name, error.message);
				dbus_error_free (&error);
				model = "";
				return_status = 1;
			} else {
				//printf ("Model: %s\n", model);
			}
			free(property_name);

			//TODO Aumentar a consistência de informações de driver entre libhal e libhd.
			driver = libhal_device_get_property_string (hal_ctx, parent_udi, "info.linux.driver", &error);
			if (dbus_error_is_set (&error)){
				// printf("error getting driver: %s, %s.\n", error.name, error.message);
				dbus_error_free (&error);
				driver = "";
				return_status = 1;
			} else {
				//printf ("Driver: %s\n", driver);
			}

			device_file = libhal_device_get_property_string (hal_ctx, udis[i], "linux.device_file", &error);
			if (dbus_error_is_set (&error)){
				// printf("error getting device file: %s, %s.\n", error.name, error.message);
				dbus_error_free (&error);
				device_file = "";
				return_status = 1;
			} else {
				//printf ("Device File: %s\n", device_file);
			}
		}

		set_vendor(webcam_ret, "vendor", vendor, vendor_id, "Vendor");
		set_model(webcam_ret, "product", product, product_id, "Product");
		add_info_tuple(webcam_ret, "model", model, -1, "Model");
		add_info_tuple(webcam_ret, "driver", driver, -1, "Driver");
		add_info_tuple(webcam_ret, "device", device_file, -1, "Device File");
		add_info_tuple(webcam_ret, "hal_udi", udis[i], -1, "HAL UDI");
		webcam_ret->return_status = return_status;

		if (retorno == NULL){
			retorno = webcam_ret;
		} else {
			webcam_ret->next = retorno;
			retorno = webcam_ret;
		}


	}

	if (num_udis == 0){
//		printf("INFO: No webcam detected!\n");
		retorno = new_ldc_info_t("webcam");
		retorno->return_status = 1;
	}

fallback:
	if (num_udis != 0 && retorno == NULL){
		printf("INFO: Error loading info from libhal!\n");
		retorno = new_ldc_info_t("webcam");
		retorno->return_status = 2;
	}

	if (log){
		insert_info_log(retorno);
	}

	return retorno;
}

