#include "ldc_tuple_t.h"

tuple_t * new_tuple_t (const char * attr_name, const char * attr_value, const int id, const char * attr_desc) {
	tuple_t * ret = (tuple_t *) malloc (sizeof (tuple_t));

	if (attr_name) {
		ret->name = (char *) malloc (sizeof (char) * (strlen (attr_name) + 1));
		strcpy (ret->name, attr_name);
	} else {
		ret->name = (char *) malloc (sizeof (char) * (strlen ("NULL") + 1));
		strcpy (ret->name, "NULL");
	}

	if (attr_value) {
		ret->value = (char *) malloc (sizeof (char) * (strlen (attr_value) + 1));
		strcpy (ret->value, attr_value);
	} else {
		ret->value = (char *) malloc (sizeof (char) * (strlen ("NULL") + 1));
		strcpy (ret->value, "NULL");
	}

	ret->id = id;

	if (attr_desc) {
		ret->description = (char *) malloc (sizeof (char) * (strlen (attr_desc) + 1));
		strcpy (ret->description, attr_desc);
	} else {
		ret->description = (char *) malloc (sizeof (char) * (strlen ("NULL") + 1));
		strcpy (ret->description, "NULL");
	}

	ret->next = NULL;

	return ret;
}


void free_tuple_t (tuple_t * t) {
	free(t->name);
	free(t->value);
	free(t->description);

	if (t->next) {
		free_tuple_t (t->next);
	}

	free(t);
}


tuple_t * enqueue_tuple_t(tuple_t * head, tuple_t * n) {
	tuple_t * ret = NULL;

	if (head != NULL) {
		ret = head;

		tuple_t * last = head;

		while (last->next != NULL) {
			last = last->next;
		}

		last->next = n;
	} else {
		ret = n;
	}

	return ret;
}


tuple_t * enqueue_new_tuple_t(tuple_t * t, const char * attr_name, const char * attr_value, const int id, const char * attr_desc) {
	tuple_t * n = new_tuple_t(attr_name, attr_value, id, attr_desc);

	return enqueue_tuple_t(t, n);
}


void print_tuple_t(tuple_t * t) {
	tuple_t * current = t;

	while (current != NULL) {
		printf ("\t%s = %s (%d) : %s\n", current->name, current->value, current->id, current->description);
		current = current->next;
	}
}
