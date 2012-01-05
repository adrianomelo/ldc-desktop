#ifndef DIAG_HARDDISK
#define DIAG_HARDDISK

#include <string.h>
#include <ctype.h>

#include <ldc_core.h>

#define SETUP_TUPLE(NAME,VALUE,ID,DESCRIPTION) 	sprintf(name, NAME); \
												sprintf(value, VALUE); \
												id = ID; \
												sprintf(description, DESCRIPTION)
/**
  @brief Executa o teste de diagnóstico de HD, que consiste em obter as informações dos particionamentos, do espaço livre e da temperatura.
  Caso o HD possua o recurso SMART, será executado o teste overall-health self-assesment.

  @param log Indica se será gerado o log
  @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnóstico
*/
ldc_diag_t * diag(int log, ldc_info_t * info);

/**
  @brief Habilita a opção de smart no HD passado como parâmetro, e retornará um int indicando se conseguiu habilitar.

  @param dev_file Indica o local do HD no dev

  @return Resultado indicando se conseguiu habilitar a opção de smart.

  @retval 1 Foi habilitado o smart.
  @retval 0 Não foi possível ser habilitado o smart.
*/
int enable_smart(char *dev_file);

/**
  @brief Recebe o output do comando parted contendo as informações das partições de um HD, com o tamanho e tipo de arquivo. Serão armazenadas essas
  duas informações no head e será retornado a quantidade de partições detectadas.

  @param head Ponteiro para a estrutura onde será armazenado as informações
  @param f Arquivo com o output do comando parted.

  @return Número de partições detectadas.
*/
int process_parted_partition_info(tuple_t ** head, FILE * f);

/**
  @brief Recebe o output do comando df contendo as informações das partições de um HD, com o seu tamanho livre e seu ponto de montagem. Serão armazenadas
  essas duas informações no head.

  @param head Ponteiro para a estrutura onde será armazenado as informações
  @param f Arquivo com o output do comando df.
*/
void process_df_partition_info(tuple_t ** head, FILE * f);

/**
  @brief Recebe o output do comando smartctl contendo a temperatura do HD. Essa informação da temperatura será inserida no head.

  @param head Ponteiro para a estrutura onde será armazenado a temperatura
  @param f Arquivo com o output do comando smartctl.
*/
void process_smartctl_Temperature(tuple_t ** head, FILE * f);

/**
  @brief Recebe o output do comando smartctl contendo o resultado do teste overall-health self-assesment. Esse resultado será inserido no head.

  @param head Ponteiro para a estrutura onde será armazenado o resultado do teste
  @param f Arquivo com o output do comando smartctl.
*/
void process_smartctl_OverallTest(tuple_t ** head, FILE * f);

#endif /* DIAG_HARDDISK */

