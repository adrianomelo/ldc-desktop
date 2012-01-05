#include "ldc_info_t.h"


ldc_info_t * new_ldc_info_t (const char * libname) {
	ldc_info_t * ret = (ldc_info_t *) calloc (1, sizeof(ldc_info_t));

	ret->lib_name = (char *) calloc (strlen(libname) + 1, sizeof(char));
	ret->return_status = -1;

	strcpy (ret->lib_name, libname);

	return ret;
}


void free_ldc_info_t (ldc_info_t * t) {
	free(t->lib_name);

	free_tuple_t(t->vendor);
	free_tuple_t(t->model);
	free_tuple_t(t->info);

	if (t->next) {
		free_ldc_info_t(t->next);
	}

	free(t);
}


void set_vendor (ldc_info_t * ret, const char * attr_name, const char * attr_value, const int id, const char * attr_desc) {
	tuple_t * new = new_tuple_t (attr_name, attr_value, id, attr_desc);

	if (ret != NULL) {
		ret->vendor = new;
	} else {
		printf ("ERROR : set_vendor : ret == NULL\n");
	}
}


void set_model (ldc_info_t * ret, const char * attr_name, const char * attr_value, const int id, const char * attr_desc) {
	tuple_t * new = new_tuple_t (attr_name, attr_value, id, attr_desc);

	if (ret != NULL) {
		ret->model = new;
	} else {
		printf ("ERROR : set_model : ret == NULL\n");
	}
}

ldc_info_t * enqueue_ldc_info_t(ldc_info_t * head, ldc_info_t * n) {
	ldc_info_t * ret = NULL;

	if (head != NULL) {
		ret = head;

		ldc_info_t * last = head;

		while (last->next != NULL) {
			last = last->next;
		}

		last->next = n;
	} else {
		ret = n;
	}

	return ret;
}


ldc_info_t * enqueue_new_ldc_info_t(ldc_info_t * t, const char * info_name) {
	ldc_info_t * n = new_ldc_info_t(info_name);

	return enqueue_ldc_info_t(t, n);
}


void add_info_tuple (ldc_info_t * ret, const char * attr_name, const char * attr_value, const int id, const char * attr_desc) {
	if (ret != NULL) {
		ret->info = enqueue_new_tuple_t(ret->info, attr_name, attr_value, id, attr_desc);
	} else {
		printf ("ERROR : add_info_tuple : ret == NULL\n");
	}
}


void print_ldc_info_t(ldc_info_t * r) {
	ldc_info_t * current = r;

	while (current != NULL) {
		printf("Name: %s\n", current->lib_name);
		printf("Status: %d\n", current->return_status);
		print_tuple_t(current->vendor);
		print_tuple_t(current->model);
		printf("----INFO----\n");
		print_tuple_t(current->info);

		printf("\n");

		current = current->next;
	}
}
