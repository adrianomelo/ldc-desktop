#ifndef DIAG_SOUND
#define DIAG_SOUND

#include <ldc_core.h>

/**
  @brief Executa o teste de diagnóstico de som, que consiste em aumentar/diminuir o volume e habilitar/desabilitar a placa.

  @param log Indica se será gerado o log
  @param info Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.

  @return Ponteiro para a estrutura ldc_diag_t contendo os resultados do teste de diagnóstico
*/
ldc_diag_t * diag(int log, ldc_info_t * info);

/**
  @brief Muda o volume para 40% e 80% utilizando a função 'set_volume' e insere o resultado do final na estrutura current passada como parâmetro.

  @param current Ponteiro para a estrutura ldc_diag_t onde será inserido o resultado do teste.
  @param dev Indica a placa que será testada.
*/
void volume_test(ldc_diag_t * current, char *dev);

/**
  @brief Função auxiliar que muda o volume para o valor passado como parâmetro e retorna se o comando foi realizado com sucesso.

  @param dev Indica a placa que será testada.
  @param vol Indica o volume que será configurado na placa, como o volume é configurado em porcentagem, esse valor deve estar entre 0-100.

  @return Resultado indicando se conseguiu mudar o volume

  @retval 1 O volume foi modificado sem erro.
  @retval 0 Não foi possível modificar o volume.
*/
int set_volume (char *dev, int vol);

/**
  @brief Executa o teste de mute e unmute e insere o resultado do final na estrutura current passada como parâmetro.

  @param current Ponteiro para a estrutura ldc_diag_t onde será inserido o resultado do teste.
  @param dev Indica a placa que será testada.
*/
void mute_unmute_test(ldc_diag_t * current, char *dev);

/**
  @brief Chama a função 'exec_amixer' para desabilitar a placa e retorna o resultado do teste.

  @param dev Indica a placa que será testada.

  @return Resultado indicando se conseguiu colocar a placa em 'mute'

  @retval 1 A placa foi configurada para 'mute'.
  @retval 0 Não foi possível configurar a placa para 'mute'.
*/
int mute (char *dev);

/**
  @brief Chama a função 'exec_amixer' para habilitar a placa e retorna o resultado do teste.

  @param dev Indica a placa que será testada.

  @return Resultado indicando se conseguiu colocar a placa em 'unmute'

  @retval 1 A placa foi configurada para 'unmute'.
  @retval 0 Não foi possível configurar a placa para 'unmute'.
*/
int unmute (char *dev);

/**
  @brief Função auxiliar utilizada pelas funções 'mute' e 'unmute' para chamar o comando amixer para configurar a placa.

  @param dev Indica a placa que será testada.
  @param type_test O tipo de teste que será feito ('mute', 'unmute')
  @param strcmp Indica qual a palavra que será usada para comparar se o comando foi realizado corretamente (mute -> '[off]', unmute -> '[on]')
  @param type_dev O nome do tipo da placa que será configurado. Por exemplo, 'Master ou 'PCM'.

  @return Resultado indicando se foi possivel configurar a placa.

  @retval 1 A placa foi configurada corretamente.
  @retval 0 Não foi possível configurar a placa.
*/
int exec_amixer(char *dev, char *type_test, char *strcmp, char *type_dev);

#endif /* DIAG_SOUND */

