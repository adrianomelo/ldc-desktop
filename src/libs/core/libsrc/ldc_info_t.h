#ifndef LDC_INFO_T
#define LDC_INFO_T

#include "ldc_tuple_t.h"

/*
 * @brief Elemento de lista ligada que representa as informacoes de cada dispositivo.
 */
struct ldc_info_ret {
	/*
	 * Library name
	 * eg.: libmouse
	 */
	char * lib_name;

	/*
	 * Return status:
	 *	0 - Success
	 *	1 - Success with warnings
	 *	2 - Failure
	 */
	int return_status;

	/*
	 * TO DOC
	 */
	tuple_t * vendor;

	/*
	 * TO DOC
	 */
	tuple_t * model;

	/*
	 * Linked list of device properties/attributes
	 */
	tuple_t * info;

	/*
	 * Next device
	 */
	struct ldc_info_ret * next;
};

typedef struct ldc_info_ret ldc_info_t;

/*
 * @brief Aloca uma nova estrutura de informacao.
 *
 * @param libname Nome da biblioteca do dispositivo.
 *
 * @return Nova estrutura.
 */
ldc_info_t * new_ldc_info_t (const char * libname);

/*
 * @brief Remove uma estrutura da memoria.
 *
 * @param t Estrutura a ser removida da memoria.
 */
void free_ldc_info_t (ldc_info_t * t);

/*
 * @brief Funcao conveniente, que cria uma instancia de tuple_t, com os parametros passados e
 * define esta tupla como o vendor da estrutura informativa.
 *
 * @param ret Estrutura onde a informacao sera adicionada.
 * @param attr_name Nome do atributo.
 * @param attr_value Valor do atributo.
 * @param id Valor numerico do atributo.
 * @param attr_desc Descricao do atributo
 */
void set_vendor (ldc_info_t * ret, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

/*
 * @brief Funcao disponibilizada por conveniencia, que cria uma instancia de tuple_t, com os parametros passados e
 * define esta tupla como o model da estrutura informativa.
 *
 * @param ret Estrutura onde a informacao sera adicionada.
 * @param attr_name Nome do atributo.
 * @param attr_value Valor do atributo.
 * @param id Valor numerico do atributo.
 * @param attr_desc Descricao do atributo
 */
void set_model (ldc_info_t * ret, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

/*
 * @brief Adiciona um novo elemento no final de uma lista de estruturas informativas.
 *
 * @param head Cabeca da fila.
 * @param n Elemento a ser adicionado.
 *
 * @return A nova cabeca da fila. Caso head seja NULL, retorna o proprio
 * elemento adicionado. Caso contrario, a cabeca retornada e o head original.
 */
ldc_info_t * enqueue_ldc_info_t(ldc_info_t * head, ldc_info_t * n);

/*
 * @brief Funcao disponibilizada por conveniencia, que aloca e preenche os atributos de uma nova
 * estrutura informativa e, em seguida, a adiciona a uma lista.
 *
 * @param t Cabeca da fila.
 * @param info_name Nome da biblioteca do dispositivo.
 *
 * @return A nova cabeca da fila. Caso head seja NULL, retorna o novo elemento.
 * Caso contrario, a cabeca retornada e o head original.
 */
ldc_info_t * enqueue_new_ldc_info_t(ldc_info_t * t, const char * info_name);

/*
 * @brief Funcao disponibilizada por conveniencia, que cria uma instancia de tuple_t, com os parametros passados e
 * adiciona esta tupla a lista de tuplas info da estrutura informativa.
 *
 * @param ret Estrutura onde a informacao sera adicionada.
 * @param attr_name Nome do atributo.
 * @param attr_value Valor do atributo.
 * @param id Valor numerico do atributo.
 * @param attr_desc Descricao do atributo.
 */
void add_info_tuple (ldc_info_t * ret, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

/*
 * @brief Funcao auxiliar, que imprime a estrutura na saida padrao, de uma forma legivel.
 *
 * @param t Estrutura a ser impressa.
 */
void print_ldc_info_t(ldc_info_t * r);

#endif /* LDC_INFO_T */
