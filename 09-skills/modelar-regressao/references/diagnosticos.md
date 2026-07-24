# Diagnósticos de regressão

## Mapa

| Problema | Evidências | Respostas possíveis |
|---|---|---|
| Não linearidade | resíduos vs ajustados, partial residuals | splines, transformação, interação |
| Heterocedasticidade | scale-location, Breusch–Pagan | modelar variância, SE robusto, família adequada |
| Autocorrelação | ACF residual, Ljung–Box | estrutura temporal, GLS, lags |
| Multicolinearidade | condição, VIF, instabilidade | reparametrizar, regularizar, combinar |
| Influência | leverage, Cook, DFBETAs | investigar, robustez, corrigir fonte |
| Overdispersion | deviance/df, resíduos | binomial negativa, quasi-likelihood |
| Zero inflation | frequência e resíduos de zeros | hurdle/ZI se houver mecanismo |
| Separação | coeficientes divergentes | penalização, Firth quando disponível |
| Má calibração | curva, intercepto e slope | recalibrar, revisar especificação |
| Mixed singular | variâncias ~0, correlações extremas | simplificar estrutura aleatória |
| PH violado | Schoenfeld, efeitos no tempo | estratificar ou variar coeficiente |

## Princípios

- Diagnosticar na escala adequada ao modelo.
- Examinar resíduos por grupos e tempo.
- Não excluir ponto influente sem investigar.
- Diferenciar falha de média, variância, link e dependência.
- Reajustar e repetir diagnósticos após mudanças.
- Registrar especificações alternativas relevantes.
