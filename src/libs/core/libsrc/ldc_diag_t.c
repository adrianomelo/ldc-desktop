#include "ldc_diag_t.h"

ldc_diag_t * new_ldc_diag_t (const char * libname) {
	ldc_diag_t * ret = (ldc_diag_t *) calloc (1, sizeof(ldc_diag_t));

	ret->lib_name = (char *) calloc (strlen(libname) + 1, sizeof(char));
	ret->return_status = -1;

	strcpy (ret->lib_name, libname);

	return ret;
}


void free_ldc_diag_t (ldc_diag_t * t) {
	free(t->lib_name);

	free_tuple_t(t->info);

	if (t->next) {
		free_ldc_diag_t(t->next);
	}

	free(t);
}


ldc_diag_t * enqueue_ldc_diag_t(ldc_diag_t * head, ldc_diag_t * n) {
	ldc_diag_t * ret = NULL;

	if (head != NULL) {
		ret = head;

		ldc_diag_t * last = head;

		while (last->next != NULL) {
			last = last->next;
		}

		last->next = n;
	} else {
		ret = n;
	}

	return ret;
}


ldc_diag_t * enqueue_new_ldc_diag_t(ldc_diag_t * t, const char * diag_name) {
	ldc_diag_t * n = new_ldc_diag_t(diag_name);

	return enqueue_ldc_diag_t(t, n);
}


void add_diag_tuple (ldc_diag_t * ret, const char * attr_name, const char * attr_value, const int id, const char * attr_desc) {
	if (ret != NULL) {
		ret->info = enqueue_new_tuple_t(ret->info, attr_name, attr_value, id, attr_desc);
	} else {
		printf ("ERROR : add_diag_tuple : ret == NULL\n");
	}
}

void print_ldc_diag_t(ldc_diag_t * r) {
	ldc_diag_t * current = r;

	while (current != NULL) {
		printf("Name: %s\n", current->lib_name);
		printf("Status: %d\n", current->return_status);
		printf("----INFO----\n");
		print_tuple_t(current->info);

		printf("\n");

		current = current->next;
	}
}
