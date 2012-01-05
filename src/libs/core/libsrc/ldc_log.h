#ifndef LDC_LOG
#define LDC_LOG

#include <stdio.h>
#include <time.h>
#include <string.h>

#include "ldc_core.h"
#include "ldc_types.h"

#define LOG_FILE "/var/tmp/ldc.log" //local e nome do arquivo de log.

/**
  @brief Fun��o que recebe um ponteiro para a estrutura info contendo as informa��es que ser�o inseridas no log.
  Para cada dispositivo ser� inserido um entrada no log, sendo a primeira linha com os tipos de informa��es e a segunda
  com os valores dessas informa��es, na mesma ordem.

  @param info Ponteiro para a estrutura contendo as informa��es que ser�o inseridas no log.
*/
void insert_info_log(ldc_info_t * info);

/**
  @brief Fun��o que recebe um ponteiro para a estrutura diag contendo as informa��es de diagn�stico que ser�o inseridas no log.
  Para cada dispositivo ser� inserido um entrada no log, sendo a primeira linha com os tipos de informa��es e a segunda
  com os valores dessas informa��es, na mesma ordem.

  @param diag Ponteiro para a estrutura contendo as informa��es de diagn�stico que ser�o inseridas no log.
*/
void insert_diag_log(ldc_diag_t *diag);

/**
  @brief Fun��o auxiliar que ser� chamada por 'insert_info_log' e 'insert_diag_log' as informa��es a serem inseridas no log.
  No caso do diagn�stico, por n�o possuir 'vendor' nem 'model', ser� passado NULL.

  @param log Ponteiro para o arquivo onde ser�o inseridas as informa��es.
  @param lib_name String contendo o nome da biblioteca.
  @param type String contendo o tipo ('info' ou 'diag').
  @param info_list Ponteiro para a lista com as informa��es do dispositivo.
  @param vendor Ponteiro para a tupla com as informa��es de fabricante.
  @param model Ponteiro para a tupla com as informa��es de modelo.
*/
void insert_device(FILE *log, char *lib_name, char *type, tuple_t * info_list, tuple_t * vendor, tuple_t * model);

/**
  @brief Fun��o auxiliar que recebe como par�metro um ponteiro para char onde ser� inserido as informa��es de data e hora.
  O formato da string ser� DATA#HORA.

  @param date_time Ponteiro para a char onde ser� inserido as informa��es de data e hora.
*/
void insert_date_time(char * date_time);

/**
  @brief Fun��o que chama o 'print_item' para cada um das tuplas passadas como par�metro, e armazena os resultados
  a serem inseridos na segunda linha do log na vari�vel device_result.

  @param log Ponteiro para o arquivo onde ser�o inseridas as informa��es.
  @param info_list Ponteiro para a lista com as informa��es do dispositivo.
  @param vendor Ponteiro para a tupla com as informa��es de fabricante.
  @param model Ponteiro para a tupla com as informa��es de modelo.
  @param device_result Ponteiro para char onde ser�o armazenados os valores a serem inseridos na 2� linha do log.
*/
void print_itens (FILE * log, tuple_t * info_list, tuple_t * vendor, tuple_t * model, char *device_result);

/**
  @brief Fun��o auxiliar que recebe o nome e o valor da informa��o a ser inserida no log e no 'device_result'.

  @param log Ponteiro para o arquivo onde ser�o inseridas as informa��es.
  @param name String contendo o nome do informa��o a ser inserida no log.
  @param value Stringo contendo o valor da informa��o a ser inserida no log.
  @param device_result Ponteiro para char onde ser�o armazenados os valores a serem inseridos na 2� linha do log.
*/
void print_item (FILE *log, char * name, char * value, char * device_result);

/**
  @brief Fun��o auxiliar que formata o resultado a ser inserido no log, ou seja, se ser� o 'value', 'id' ou
  'value (id)'. O resultado � armazenado no ponteiro 'value' passado como par�metro.

  @param tuple Ponteiro para a estrutura contendo as informa��es.
  @param value Ponteiro onde ser� armazenado o valor resultante no formato correto a ser inserido no log.
*/
void get_value(tuple_t *tuple, char * value);

#endif /* LDC_LOG */
