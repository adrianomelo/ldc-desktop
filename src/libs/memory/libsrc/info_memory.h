#ifndef INFO_MEMORY
#define INFO_MEMORY

#include "core_memory.h"

/*
 * @brief Captura as informações da memoria, utilizando as informações disponíveis no dmidecode e hwinfo.
 *
 * @param log Indica se será gerado o log.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info(int log);

/*
 * @brief Função auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informações do dispositivo.
 * Então, salva na estrutura de retorno todas a infomações do dispositivo.
 *
 * @param log
 * @param hd Ponteiro para a estrutura da libhd que contém as informações do dispositivo.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info_libhd_memory (ldc_info_t * log, hd_t * hd);

/*
 * @brief Funcao auxiliar que centraliza o tratamento das informacoes disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void info_dmidecode_sections(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Funcao auxiliar que trata as informacoes sobre o controlador de memoria, disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void info_process_dmi_type_5(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Funcao auxiliar que trata as informacoes sobre os modulos de memoria (DMI TYPE 6), disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void info_process_dmi_type_6(tuple_t ** head, tuple_t ** log, FILE * f);

/*
 * @brief Funcao auxiliar que trata as informacoes sobre os modulos de memoria (DMI TYPE 17), disponiveis no dmidecode.
 *
 * @param head Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param log Ponteiro para a cabeca da lista de tuplas, onde essa informacao deve ser inserida.
 * @param f Arquivo contendo o output do dmidecode, de onde a informacao deve ser lida.
 */
void info_process_dmi_type_17(tuple_t ** head, tuple_t ** log, FILE * f);

#endif /* INFO_MEMORY */
