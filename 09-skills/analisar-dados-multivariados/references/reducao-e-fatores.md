# Redução e fatores

| Objetivo | Método | Observação |
|---|---|---|
| Maximizar variância | PCA | componentes são combinações, não construtos |
| Robustez a outliers | robust PCA | validar implementação e decomposição |
| Construtos latentes | EFA/CFA | modelar variância comum |
| Categorias | CA/MCA | usar massas e perfis |
| Relacionar X e Y | PLS | validar componentes fora da amostra |
| Relacionar blocos | CCA | regularizar em alta dimensão |
| Visualizar vizinhança | UMAP/t-SNE | estrutura global pode distorcer |

## Seleção

- PCA: scree, parallel analysis, reconstrução e estabilidade.
- EFA: parallel analysis, MAP, resíduos e interpretabilidade.
- CFA: fit global, resíduos, cargas, validade convergente/discriminante e invariância.
- PLS/CCA: validação e permutação.

## Cuidados

- O sinal de um componente é arbitrário.
- Rotação muda interpretação, não o subespaço.
- Variância explicada alta não garante utilidade.
- Cronbach alpha alto pode refletir redundância.
- Comparar estruturas entre grupos exige invariância de mensuração.
