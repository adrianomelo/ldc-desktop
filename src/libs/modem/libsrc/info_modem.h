#ifndef INFO_MODEM
#define INFO_MODEM

#include <ldc_core.h>

/*
 * @brief Captura as informações do modem, utilizando as informações disponíveis no hwinfo.
 *
 * @param log Indica se será gerado o log.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info (int log);

/*
 * @brief Função auxiliar que recebe uma estrutura do tipo hd_t fornecida pela libhd contendo as informações de um modem.
 * Então, salva na estrutura de retorno todas a infomações do dispositivo.
 *
 * @param log
 * @param hd Ponteiro para a estrutura da libhd que contém as informações do modem.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * info_libhd_modem (ldc_info_t * log, hd_t * hd);

/*
 * @brief Funcao auxiliar que procura por um modem, utilizando de uma comparacao entre o output do lspci e a tabela PCIIDs.
 *
 * @param f Ponteiro para o arquivo com o output da filtragem/comparacao.
 *
 * @return Ponteiro para a estrutura ldc_info_t contendo os resultados da parte informativa.
 */
ldc_info_t * process_lspci_modem(FILE * f);

/*
 * @brief Funcao auxiliar que escreve em dev_file o alvo do link /dev/modem.
 *
 * @param dev_file Buffer de saida.
 *
 * @return 1 se o link existe, 0 caso contrario.
 */
int get_dev_modem_link(char * dev_file);

/*
 * @brief Se o dispositivo de modem for outro que não /dev/ttyS0, esta função cria um link para este dispositivo em /dev/ttyS0, escrevendo o endereço
 * original do dispositivo em dev_file. O dispositivo em /dev/ttyS0, se não é o modem, é movido para uma localização temporária. Para reverter
 * estas modificações, revert_prepare_for_hwinfo_call deve ser utilizado.
 *
 * @param dev_file Caminho original para o dispositivo.
 */
void prepare_for_hwinfo_call(char * dev_file);

/*
 * @brief Desfaz as alterações possivelmente feitas por prepare_for_hwinfo_call
 *
 * @param dev_file Caminho original para o dispositivo.
 */
void revert_prepare_for_hwinfo_call(char * dev_file);

#endif /* INFO_MODEM */
