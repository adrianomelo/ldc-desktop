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
  @brief Executa o teste de diagn�stico de HD, que consiste em obter as informa��es dos particionamentos, do espa�o livre e da temperatura.
  Caso o HD possua o recurso SMART, ser� executado o teste overall-health self-assesment.

  @param log Indica se ser� gerado o log
  @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagn�stico
*/
ldc_diag_t * diag(int log, ldc_info_t * info);

/**
  @brief Habilita a op��o de smart no HD passado como par�metro, e retornar� um int indicando se conseguiu habilitar.

  @param dev_file Indica o local do HD no dev

  @return Resultado indicando se conseguiu habilitar a op��o de smart.

  @retval 1 Foi habilitado o smart.
  @retval 0 N�o foi poss�vel ser habilitado o smart.
*/
int enable_smart(char *dev_file);

/**
  @brief Recebe o output do comando parted contendo as informa��es das parti��es de um HD, com o tamanho e tipo de arquivo. Ser�o armazenadas essas
  duas informa��es no head e ser� retornado a quantidade de parti��es detectadas.

  @param head Ponteiro para a estrutura onde ser� armazenado as informa��es
  @param f Arquivo com o output do comando parted.

  @return N�mero de parti��es detectadas.
*/
int process_parted_partition_info(tuple_t ** head, FILE * f);

/**
  @brief Recebe o output do comando df contendo as informa��es das parti��es de um HD, com o seu tamanho livre e seu ponto de montagem. Ser�o armazenadas
  essas duas informa��es no head.

  @param head Ponteiro para a estrutura onde ser� armazenado as informa��es
  @param f Arquivo com o output do comando df.
*/
void process_df_partition_info(tuple_t ** head, FILE * f);

/**
  @brief Recebe o output do comando smartctl contendo a temperatura do HD. Essa informa��o da temperatura ser� inserida no head.

  @param head Ponteiro para a estrutura onde ser� armazenado a temperatura
  @param f Arquivo com o output do comando smartctl.
*/
void process_smartctl_Temperature(tuple_t ** head, FILE * f);

/**
  @brief Recebe o output do comando smartctl contendo o resultado do teste overall-health self-assesment. Esse resultado ser� inserido no head.

  @param head Ponteiro para a estrutura onde ser� armazenado o resultado do teste
  @param f Arquivo com o output do comando smartctl.
*/
void process_smartctl_OverallTest(tuple_t ** head, FILE * f);

#endif /* DIAG_HARDDISK */

