#ifndef CORE_PROCESSOR
#define CORE_PROCESSOR

#include <ldc_core.h>

/*
 * @brief Obtem as informacoes sobre a versao do processador.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_4_version(tuple_t ** head, FILE * f);

/*
 * @brief Obtem as informacoes sobre o tipo do socket do processador.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_4_socket(tuple_t ** head,  tuple_t ** log, FILE * f);

/*
 * @brief Obtem as informacoes sobre a tensao do processador.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_4_voltage(tuple_t ** head, FILE * f);

/*
 * @brief Obtem as informacoes sobre o clock do processador.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_4_clock(tuple_t ** head, FILE * f);

/*
 * @brief Obtem as informacoes sobre o FSB do processador.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_4_fsb(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Obtem as informacoes sobre o tipo de socket da memoria cache.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_7_socket(tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o tamanho da memoria cache.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_7_installed_size(tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o tipo de associatividade da memoria cache.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_7_associativity(tuple_t ** head, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre os modos de operacao da memoria cache.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_7_operational_mode(tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre os tipos de memoria cache suportados.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_7_supported_types(tuple_t ** head, tuple_t ** log, FILE * f, char * module_socket);

/*
 * @brief Obtem as informacoes sobre o tipo de correcao de erros da memoria cache.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void process_dmi_type_7_err_correction_type(tuple_t ** head, FILE * f, char * module_socket);

#endif /* CORE_PROCESSOR */
