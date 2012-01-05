#ifndef LDC_LOG
#define LDC_LOG

#include <stdio.h>
#include <time.h>
#include <string.h>

#include "ldc_core.h"
#include "ldc_types.h"

#define LOG_FILE "/var/tmp/ldc.log" //local e nome do arquivo de log.

/**
  @brief Função que recebe um ponteiro para a estrutura info contendo as informações que serão inseridas no log.
  Para cada dispositivo será inserido um entrada no log, sendo a primeira linha com os tipos de informações e a segunda
  com os valores dessas informações, na mesma ordem.

  @param info Ponteiro para a estrutura contendo as informações que serão inseridas no log.
*/
void insert_info_log(ldc_info_t * info);

/**
  @brief Função que recebe um ponteiro para a estrutura diag contendo as informações de diagnóstico que serão inseridas no log.
  Para cada dispositivo será inserido um entrada no log, sendo a primeira linha com os tipos de informações e a segunda
  com os valores dessas informações, na mesma ordem.

  @param diag Ponteiro para a estrutura contendo as informações de diagnóstico que serão inseridas no log.
*/
void insert_diag_log(ldc_diag_t *diag);

/**
  @brief Função auxiliar que será chamada por 'insert_info_log' e 'insert_diag_log' as informações a serem inseridas no log.
  No caso do diagnóstico, por não possuir 'vendor' nem 'model', será passado NULL.

  @param log Ponteiro para o arquivo onde serão inseridas as informações.
  @param lib_name String contendo o nome da biblioteca.
  @param type String contendo o tipo ('info' ou 'diag').
  @param info_list Ponteiro para a lista com as informações do dispositivo.
  @param vendor Ponteiro para a tupla com as informações de fabricante.
  @param model Ponteiro para a tupla com as informações de modelo.
*/
void insert_device(FILE *log, char *lib_name, char *type, tuple_t * info_list, tuple_t * vendor, tuple_t * model);

/**
  @brief Função auxiliar que recebe como parâmetro um ponteiro para char onde será inserido as informações de data e hora.
  O formato da string será DATA#HORA.

  @param date_time Ponteiro para a char onde será inserido as informações de data e hora.
*/
void insert_date_time(char * date_time);

/**
  @brief Função que chama o 'print_item' para cada um das tuplas passadas como parâmetro, e armazena os resultados
  a serem inseridos na segunda linha do log na variável device_result.

  @param log Ponteiro para o arquivo onde serão inseridas as informações.
  @param info_list Ponteiro para a lista com as informações do dispositivo.
  @param vendor Ponteiro para a tupla com as informações de fabricante.
  @param model Ponteiro para a tupla com as informações de modelo.
  @param device_result Ponteiro para char onde serão armazenados os valores a serem inseridos na 2ª linha do log.
*/
void print_itens (FILE * log, tuple_t * info_list, tuple_t * vendor, tuple_t * model, char *device_result);

/**
  @brief Função auxiliar que recebe o nome e o valor da informação a ser inserida no log e no 'device_result'.

  @param log Ponteiro para o arquivo onde serão inseridas as informações.
  @param name String contendo o nome do informação a ser inserida no log.
  @param value Stringo contendo o valor da informação a ser inserida no log.
  @param device_result Ponteiro para char onde serão armazenados os valores a serem inseridos na 2ª linha do log.
*/
void print_item (FILE *log, char * name, char * value, char * device_result);

/**
  @brief Função auxiliar que formata o resultado a ser inserido no log, ou seja, se será o 'value', 'id' ou
  'value (id)'. O resultado é armazenado no ponteiro 'value' passado como parâmetro.

  @param tuple Ponteiro para a estrutura contendo as informações.
  @param value Ponteiro onde será armazenado o valor resultante no formato correto a ser inserido no log.
*/
void get_value(tuple_t *tuple, char * value);

#endif /* LDC_LOG */
