# Calibração, estabilidade e drift

## Calibração

Para classificação, avaliar reliability curve, calibration intercept, slope, Brier e calibração por grupos. Para regressão probabilística, avaliar cobertura por faixa, quantis e intervalos. Para risco temporal, avaliar calibração no horizonte relevante.

Métodos:

- Platt scaling;
- isotonic regression;
- beta calibration;
- temperature scaling;
- recalibração de intercepto e slope;
- conformal prediction.

Separar dados de calibração e teste.

## Estabilidade

Examinar variação por:

- fold;
- semente;
- período;
- entidade;
- região;
- faixa do alvo;
- prevalência;
- qualidade de dados;
- regime operacional.

Reportar distribuição, não apenas média.

## Drift

Distinguir:

- covariate shift: muda P(X);
- label shift: muda P(Y);
- concept drift: muda P(Y|X);
- schema ou data-quality drift;
- policy drift causado pelo próprio uso do modelo.

PSI, KS, divergências e detectores são sinais. Relacionar drift à degradação e à decisão antes de agir.

## Respostas

Escolher entre investigar fonte, corrigir dados, recalibrar, ajustar limiar, atualizar features, retreinar, usar janela móvel, segmentar modelos ou suspender uso. Documentar o gatilho e o teste de recuperação.
