# Métricas por tarefa

| Tarefa | Métrica principal possível | Complementares |
|---|---|---|
| Regressão | MAE ou RMSE | bias, MASE, RMSSE, quantis do erro |
| Classificação binária | log loss, PR-AUC ou utilidade | ROC-AUC, Brier, calibração, confusion matrix |
| Multiclasse | log loss macro/ponderada | F1, top-k, calibração |
| Ranking | NDCG, MAP | precision@k, recall@k |
| Sobrevivência | time-dependent Brier | C-index, calibração temporal |
| Forecast | WAPE/MASE/RMSSE | bias, RMSE, erro por horizonte |
| Quantis | pinball loss | cobertura, crossing, interval score |
| Distribuição | CRPS ou log score | calibração, sharpness |

## Cuidados

- MAPE falha com zeros e valores pequenos.
- ROC-AUC pode parecer alta com baixa utilidade em eventos raros.
- F1 ignora verdadeiros negativos e não incorpora custo diretamente.
- WAPE pode esconder séries pequenas e ser instável em denominadores baixos.
- R² não mede calibração nem utilidade.
- Métricas macro dão igual peso a grupos; ponderadas refletem volume.
- Proper scoring rules devem orientar previsões probabilísticas.

Sempre mostrar a unidade e o sentido de melhora.
