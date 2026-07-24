# Multiplicidade e flexibilidade analítica

## Fontes de multiplicidade

- vários desfechos;
- vários tratamentos ou grupos;
- muitas janelas temporais;
- subgrupos;
- transformações;
- múltiplas definições de métrica;
- análises intermediárias;
- seleção de modelos;
- hipóteses sugeridas pelos próprios dados.

## Objetivos de controle

| Objetivo | Procedimentos comuns | Uso |
|---|---|---|
| FWER forte | Holm, Bonferroni, Hochberg | Poucas decisões críticas |
| FDR | Benjamini–Hochberg, BY | Descoberta em muitas hipóteses |
| Contrastes | Tukey, Dunnett, intervalos simultâneos | Comparações planejadas entre grupos |
| Hierarquia | gatekeeping, closed testing | Hipóteses com prioridade lógica |
| Sequencial | alpha spending, group sequential | Múltiplas análises no tempo |

## Práticas

- Definir hipótese primária e família antes da análise confirmatória.
- Reportar valores-p brutos e ajustados quando útil.
- Manter estimativas e intervalos; ajuste não substitui magnitude.
- Não criar famílias separadas apenas para evitar correção.
- Não aplicar FDR quando cada falso positivo tiver alto custo individual sem justificar.
- Tratar análise de subgrupo pós-hoc como exploratória.

## Degrees of freedom

Registrar decisões sobre exclusões, transformações, covariáveis, métricas e janelas. Quando escolhas plausíveis forem numerosas, considerar multiverse analysis ou specification curve para avaliar robustez.
