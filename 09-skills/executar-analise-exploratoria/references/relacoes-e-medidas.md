# Relações e medidas

## Selecionar por tipo e estrutura

| Relação | Medidas e técnicas | Cuidados |
|---|---|---|
| Numérica × numérica | Pearson, Spearman, Kendall, biweight, regressão suave | Examinar forma, outliers, grupos e dependência |
| Numérica × binária | diferença padronizada, point-biserial, distribuições | Considerar desbalanceamento e variância |
| Numérica × multicategoria | eta² descritivo, distribuições por grupo | Comparar composição e tamanhos |
| Categórica × categórica | proporções, odds, Cramér's V, resíduos | Evitar células esparsas e confundir composição |
| Não linear geral | informação mútua, distance correlation | Interpretabilidade menor e risco de sobreajuste |
| Condicional | estratificação, correlação parcial, modelos auxiliares | Não presumir ajuste causal |

## Princípios

- Mostrar o gráfico antes ou junto da medida resumida.
- Distinguir monotonicidade de linearidade.
- Reportar quantidade de observações válidas usada em cada cálculo.
- Avaliar estabilidade por subamostras e períodos.
- Reconhecer correlação ecológica quando dados estiverem agregados.
- Considerar erro de mensuração e restrição de amplitude.
- Não usar correlação de Pearson para variáveis categóricas codificadas arbitrariamente.

## Muitas variáveis

Ordenar relações por pergunta substantiva, não apenas magnitude. Se explorar matrizes extensas, controlar redundância, registrar quantas relações foram examinadas e reservar validação independente para padrões selecionados.
