#ifndef LDC_TUPLE_T
#define LDC_TUPLE_T

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * @brief Elemento de lista ligada que representa cada propriedade/atributo do dispositivo
 */
struct tuple {
	/*
	 * Attribute name
	 */
	char * name;

	/*
	 * Attribute value (if any)
	 */
	char * value;

	/*
	 * Attribute id (if any)
	 */
	int id;

	/*
	 * TO DOC
	 */
	char * description;

	/*
	 * Next attribute
	 */
	struct tuple * next;
};

typedef struct tuple tuple_t;

/*
 * @brief Aloca uma nova tupla e preenche seus atributos, segundo os parametros.
 *
 * @param attr_name Nome do atributo
 * @param attr_value Valor do atributo.
 * @param id Valor numerico do atributo.
 * @param attr_desc Descricao do atributo.
 *
 * @return Nova tupla, criada a partir dos parametros.
 */
tuple_t * new_tuple_t (const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

/*
 * @brief Remove uma tupla da memoria.
 *
 * @param t Tupla a ser removida.
 */
void free_tuple_t (tuple_t * t);

/*
 * @brief Adiciona um novo elemento no final de uma lista de tuplas.
 *
 * @param head Cabeca da fila.
 * @param n Elemento a ser adicionado.
 *
 * @return A nova cabeca da fila. Caso head seja NULL, retorna o proprio
 * elemento adicionado. Caso contrario, a cabeca retornada e o head original.
 */
tuple_t * enqueue_tuple_t(tuple_t * head, tuple_t * n);

/*
 * @brief Funcao disponibilizada por conveniencia, que aloca e preenche os atributos de uma nova
 * tupla e, em seguida, a adiciona a uma lista.
 *
 * @param t Cabeca da fila.
 * @param attr_name Nome do atributo
 * @param attr_value Valor do atributo.
 * @param id Inteiro identificador do atributo.
 * @param attr_desc Descricao do atributo.
 *
 * @return A nova cabeca da fila. Caso head seja NULL, retorna o novo elemento.
 * Caso contrario, a cabeca retornada e o head original.
 */
tuple_t * enqueue_new_tuple_t(tuple_t * t, const char * attr_name, const char * attr_value, const int id, const char * attr_desc);

/*
 * @brief Funcao auxiliar, que imprime a tupla na saida padrao, de uma forma legivel.
 *
 * @param t Tupla a ser impressa.
 */
void print_tuple_t(tuple_t * t);

#endif /* LDC_TUPLE_T */
