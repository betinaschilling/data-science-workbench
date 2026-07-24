# Execução e análise

## Integridade

- SRM: comparar alocação observada e esperada.
- Covariáveis: verificar diferenças pré-tratamento como diagnóstico.
- Exposição: medir assignment, eligibility e actual exposure separadamente.
- Attrition: comparar perda e atraso entre braços.
- Contaminação: medir troca ou contato entre variantes.
- Clusters: confirmar que nenhuma unidade mudou de cluster.

## Análise

- Usar ITT como análise principal.
- Ajustar covariáveis pré-tratamento para precisão, não para reparar randomização.
- Clusterizar erros na unidade de atribuição.
- Usar randomization inference quando especialmente compatível.
- Reportar diferença absoluta e relativa.
- Mostrar intervalo, p-valor quando previsto e efeito mínimo relevante.
- Avaliar guardrails com multiplicidade proporcional ao risco.

## Problemas

| Problema | Conduta |
|---|---|
| SRM | interromper interpretação e investigar pipeline |
| Baixa adesão | manter ITT; estimar CACE com cuidado |
| Exposição desigual | investigar mecanismo e estimando |
| Resultado imaturo | aguardar janela pré-definida |
| Evento externo | documentar; usar desenho temporal ou sensibilidade |
| Peeking | aplicar método sequencial ou reconhecer inflação |
| Subgrupo pós-hoc | rotular como exploratório |

## Relatório

Apresentar fluxo de elegibilidade, atribuição, exposição, maturação e análise. Documentar desvios do protocolo antes de revelar resultados quando possível.
