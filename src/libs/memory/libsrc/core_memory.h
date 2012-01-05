#ifndef CORE_MEMORY
#define CORE_MEMORY

#include <ldc_core.h>

/*
 * @brief Obtem as informacoes sobre o tamanho maximo de cada modulo, do controlador de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_5_max_mod_size(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Obtem as informacoes sobre o tamanho maximo de memoria total, do controlador de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_5_max_total_size(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Obtem as informacoes sobre as velocidades suportadas, do controlador de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_5_speeds(tuple_t ** head, FILE * f);

/*
 * @brief Obtem as informacoes sobre os tipos de memoria suportados, do controlador de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_5_types(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Obtem as informacoes sobre a voltagem maxima dos modulos, do controlador de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_5_voltage(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Obtem as informacoes sobre o socket, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_6_socket(tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre a velocidade, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_6_speed(tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o tipo, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_6_type(tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o tamanho, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_6_size(tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o socket, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_17_socket(tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre a velocidade, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_17_speed (tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o tipo, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_17_type (tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o 'form factor', do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_17_ffactor (tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o tamanho, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_17_size (tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o fabricante, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_17_vendor (tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o numero de serie, do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_17_sn (tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o 'part number', do modulo de memoria.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_17_pn (tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o tamanho total de memoria informado pelo /proc/meminfo
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do /proc/meminfo, de onde a informacao deve ser lida.
 */
void process_proc_meminfo_MemTotal(tuple_t ** head, FILE * f);

#endif /* CORE_MEMORY */
