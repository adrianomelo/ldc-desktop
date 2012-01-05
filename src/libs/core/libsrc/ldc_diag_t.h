#ifndef LDC_DIAG_T
#define LDC_DIAG_T

#include "ldc_tuple_t.h"

/*
 * @brief Elemento de lista ligada que representa o diagnostico de cada dispositivo.
 */
struct ldc_diag_ret {
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
	 * Linked list of tuples, holding diagnostic informations/messages
	 */
	tuple_t * info;

	/*
	 * Next result
	 */
	struct ldc_diag_ret * next;
};

typedef struct ldc_diag_ret ldc_diag_t;

/*
 * @brief Aloca uma nova estrutura de diagnostico.
 *
 * @param libname Nome da biblioteca do dispositivo.
 *
 * @return Nova estrutura.
 */
ldc_diag_t * new_ldc_diag_t (const char * libname);

/*
 * @brief Remove uma estrutura da memoria.
 *
 * @param t Estrutura a ser removida da memoria.
 */
void free_ldc_diag_t (ldc_diag_t * t);

/*
 * @brief Adiciona um novo elemento no final de uma lista de estruturas de diagnostico.
 *
 * @param head Cabeca da fila.
 * @param n Elemento a ser adicionado.
 *
 * @return A nova cabeca da fila. Caso head seja NULL, retorna o proprio
 * elemento adicionado. Caso contrario, a cabeca retornada e o head original.
 */
ldc_diag_t * enqueue_ldc_diag_t(ldc_diag_t * head, ldc_diag_t * n);

/*
 * @brief Funcao disponibilizada por conveniencia, que aloca e preenche os atributos de uma nova
 * estrutura de diagnostico e, em seguida, a adiciona a uma lista.
 *
 * @param t Cabeca da fila.
 * @param info_name Nome da biblioteca do dispositivo.
 *
 * @return A nova cabeca da fila. Caso head seja NULL, retorna o novo elemento.
 * Caso contrario, a cabeca retornada e o head original.
 */
ldc_diag_t * enqueue_new_ldc_diag_t(ldc_diag_t * t, const char * diag_name);

/*
 * @brief Funcao disponibilizada por conveniencia, que cria uma instancia de tuple_t, com os parametros passados e
 * adiciona esta tupla a lista de tuplas info da estrutura de diagnostivo.
 *
 * @param ret Estrutura onde a informacao sera adicionada.
 * @param attr_name Nome do atributo.
 * @param attr_value Valor do atributo.
 * @param id Valor numerico do atributo.
 * @param attr_desc Descricao do atributo.
 */
void add_diag_tuple (ldc_diag_t * ret, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

/*
 * @brief Funcao auxiliar, que imprime a estrutura na saida padrao, de uma forma legivel.
 *
 * @param t Estrutura a ser impressa.
 */
void print_ldc_diag_t(ldc_diag_t * r);

#endif /* LDC_DIAG_T */
