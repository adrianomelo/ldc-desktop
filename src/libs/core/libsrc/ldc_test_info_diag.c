#include "ldc_core.h"

ldc_diag_t * test_diag(ldc_info_t * info);
ldc_info_t * test_info();
void print_help(char * prog_name);

int main(int argc, char **argv) {
	int ret;

	ldc_info_t * info;
	ldc_diag_t * diag;

	if (argc > 1) {
		switch(atoi(argv[1])) {
			case 0:
				info = test_info();
				print_ldc_info_t(info);
				ret = 0;
				break;
			case 1:
				info = test_info();
				diag = test_diag(info);
				print_ldc_diag_t(diag);
				ret = 0;
				break;
			default:
				print_help(argv[0]);
				ret = 1;
				break;
		}
	}

	return ret;
}


void print_help(char * prog_name) {
	printf("Usage: %s 0|1 - 0 = info ; 1 = diag", prog_name);
}


ldc_diag_t * test_diag(ldc_info_t * info) {
	ldc_diag_t * ret = diag(1, info);

	return ret;
}


ldc_info_t * test_info() {
	ldc_info_t * ret = info(1);

	return ret;
}
