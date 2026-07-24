# Validação e métricas temporais

## Desenhos de validação

- Holdout temporal: usar para uma avaliação final simples, preservando um período futuro.
- Expanding window: usar quando toda a história permanecer relevante.
- Sliding window: usar quando regimes antigos perderem validade.
- Rolling origin: usar para simular diversas datas reais de previsão.
- Gap ou embargo: usar quando features próximas à fronteira puderem contaminar o teste.
- Nested temporal validation: usar quando seleção de modelo e avaliação final precisarem ser separadas.

## Métricas pontuais

| Métrica | Uso | Limitação |
|---|---|---|
| MAE | erro absoluto interpretável | depende da escala |
| RMSE | penalizar erros grandes | sensível a outliers |
| WAPE/WMAPE | agregação comercial ponderada | instável quando o denominador é pequeno |
| MAPE | comunicação percentual | problemática com zeros e valores pequenos |
| sMAPE | alternativa percentual simétrica | ainda apresenta comportamentos não intuitivos |
| MASE | comparação entre séries | depende de baseline de escala adequado |
| RMSSE | penalização quadrática escalada | sensível a extremos |
| Bias/ME | direção sistemática do erro | cancelamentos podem ocultar problemas |

Não depender de uma única métrica. Combinar magnitude, viés e adequação à decisão.

## Métricas probabilísticas

- Pinball loss para quantis.
- CRPS para distribuições preditivas.
- Coverage para verificar frequência de cobertura.
- Interval score ou Winkler score para cobertura e largura.
- Calibration plots por quantil e horizonte.

Avaliar calibração e sharpness conjuntamente: intervalos excessivamente largos podem cobrir bem e ainda ser pouco úteis.

## Agregação

Reportar resultados por:

- horizonte;
- origem de previsão;
- série e nível hierárquico;
- volume ou relevância comercial;
- calendário e eventos críticos;
- regime ou janela temporal.

Apresentar média, mediana, dispersão e caudas quando houver heterogeneidade. Evitar rankings baseados em diferenças pequenas e instáveis; quando necessário, usar testes ou intervalos para diferenças de desempenho, respeitando a dependência temporal.
