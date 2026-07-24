# Famílias de modelos

## Seleção orientada pelo problema

| Contexto | Famílias candidatas | Observações |
|---|---|---|
| Poucas séries e necessidade inferencial | ARIMA/SARIMAX, ETS, espaço de estados, regressão dinâmica | Favorecer diagnóstico e interpretação |
| Sazonalidade múltipla | MSTL + modelo residual, TBATS, regressão harmônica | Validar estabilidade das sazonalidades |
| Muitas séries relacionadas | modelos globais de ML, deep learning ou fundacionais | Usar identificação de série e validação por grupos |
| Covariáveis complexas e não linearidade | CatBoost, LightGBM, XGBoost | Criar lags e janelas sem leakage |
| Horizonte longo | modelos diretos, multioutput, N-HiTS, Transformers, fundacionais | Avaliar degradação por horizonte |
| Poucos dados | modelos clássicos, pooling hierárquico, modelos pré-treinados | Evitar ajuste excessivo |
| Intermitência | Croston, SBA, TSB, modelos de ocorrência e tamanho | Usar métricas adequadas a zeros |
| Hierarquia | base forecast + reconciliação, modelos coerentes | Comparar acurácia e coerência |
| Previsão probabilística | espaço de estados, quantis, likelihoods, conformal | Medir calibração e sharpness |

## Estratégias multi-horizonte

- Recursiva: simples, mas acumula erro.
- Direta: reduz propagação, mas exige um modelo por horizonte.
- DirRec: combina dependência e especialização.
- Multioutput: aprende horizontes conjuntamente.
- MIMO/seq2seq: útil quando a trajetória futura conjunta importa.

Escolher a estratégia de acordo com o horizonte operacional, o volume de dados e o custo de manutenção.

## Modelos fundacionais

Tratar modelos como Chronos e TimesFM como candidatos, não como vencedores prévios. Confirmar:

- frequência e comprimento aceitos;
- suporte a covariáveis e quantis;
- tratamento de múltiplas séries;
- custo e latência;
- zero-shot versus fine-tuning;
- estabilidade em mudança de domínio;
- comparação justa com baselines locais e globais.

## Ensemble e seleção

Construir ensembles somente quando houver diversidade real de erros. Estimar pesos dentro do backtesting, sem usar o período final. Avaliar seleção por origem, horizonte ou série apenas quando houver dados suficientes para evitar instabilidade.
