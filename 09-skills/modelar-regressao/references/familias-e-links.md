# Famílias e links

| Desfecho | Modelos candidatos | Escala de interpretação |
|---|---|---|
| Contínuo | OLS, GLS, robusta, Student-t | diferença média condicional |
| Contínuo positivo | Gamma, lognormal, inverse Gaussian | razão ou diferença esperada |
| Binário | logit, probit, cloglog | odds, probabilidade, efeito marginal |
| Ordinal | proportional odds/probit ordinal | odds cumulativas ou probabilidades |
| Nominal | multinomial | probabilidades ou odds por categoria |
| Contagem | Poisson, quasi-Poisson, binomial negativa | razão de taxas |
| Taxa | Poisson/NB com offset | taxa por unidade de exposição |
| Proporção | binomial, beta, fractional logit | proporção esperada |
| Quantil | regressão quantílica | diferença condicional no quantil |
| Sobrevivência | Cox, AFT, paramétricos flexíveis | hazard, tempo ou sobrevivência |
| Muitos zeros | hurdle, zero-inflated, two-part | ocorrência e magnitude |
| Repetido/agrupado | mixed models, GEE | efeito condicional ou populacional |

## Escolha

- Usar link que respeite o suporte do desfecho e ofereça interpretação adequada.
- Verificar se a distribuição condicional, não apenas a marginal, está coerente.
- Usar offset com coeficiente fixado em 1 para exposição conhecida.
- Distinguir modelo zero-inflated de hurdle pelo mecanismo substantivo.
- Verificar proportional odds antes de adotar modelo ordinal proporcional.
- Distinguir efeitos condicionais de modelos mistos e efeitos marginais de GEE.
