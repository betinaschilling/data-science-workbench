# Ausência e cobertura

## Classificar a ausência

| Situação | Interpretação possível | Ação inicial |
|---|---|---|
| Campo vazio em linha existente | Não coletado, erro, não aplicável ou desconhecido | Investigar regra e padrão por grupo |
| Data ou entidade sem linha | Falha de cobertura, ausência operacional ou evento não ocorrido | Construir grade esperada antes de medir |
| Valor zero | Medição real, censura, placeholder ou ausência codificada | Validar semântica do zero |
| Grupo sem qualquer observação | Falha estrutural de cobertura | Restringir população ou buscar nova fonte |
| Ausência após determinado período | Mudança de sistema ou definição | Investigar quebra de processo |

## Mecanismos estatísticos

- MCAR: a ausência não depende de variáveis observadas ou não observadas relevantes.
- MAR: a ausência pode ser explicada por variáveis observadas incluídas no tratamento.
- MNAR: a probabilidade de ausência depende do próprio valor ausente ou de fatores não observados.
- Estrutural: o campo não se aplica ou a unidade não deveria gerar observação.

Não concluir MCAR apenas porque um teste não rejeitou a hipótese. Usar conhecimento do processo e análises de sensibilidade.

## Medidas mínimas

- percentual ausente geral e por grupo;
- padrão temporal;
- blocos de colunas ausentes conjuntamente;
- comparação de variáveis observadas entre linhas completas e incompletas;
- cobertura da população e do período;
- comprimento e localização das lacunas;
- diferença entre grade esperada e observada.

## Tratamentos

Escolher entre correção na fonte, indicador de ausência, imputação simples, múltipla, modelagem conjunta, ponderação, restrição de escopo ou análise de sensibilidade. Ajustar qualquer imputador apenas no conjunto de treinamento ou na informação historicamente disponível.
