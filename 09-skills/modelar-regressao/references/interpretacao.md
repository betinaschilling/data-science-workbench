# Interpretação de regressão

## Regras

- Declarar “mantidas constantes as variáveis do modelo” para associação condicional.
- Explicar a unidade de mudança do preditor.
- Converter logs, odds e links para escalas compreensíveis.
- Mostrar intervalos e distribuição das covariáveis onde o efeito foi estimado.
- Evitar extrapolar além do suporte observado.
- Para não linearidades, mostrar curva predita e derivadas ou contrastes.
- Para interações, mostrar efeitos condicionais em valores relevantes.
- Distinguir efeito individual, específico de cluster e populacional.

## Exemplos de escala

| Modelo | Coeficiente bruto | Tradução útil |
|---|---|---|
| OLS | mudança em Y por unidade de X | diferença na unidade de Y |
| Log(Y) | mudança em log Y | variação percentual aproximada ou exata |
| Logit | mudança em log-odds | probabilidades preditas e efeito marginal |
| Poisson log | mudança em log taxa | razão de taxas |
| Cox | mudança em log hazard | hazard ratio e curvas de sobrevivência |
| Quantílica | mudança no quantil | diferença no quantil condicional |

## Cuidado causal

Um coeficiente ajustado não é automaticamente causal. Exigir uma estratégia de identificação, conjunto de ajuste defensável, temporalidade correta, consistência, positividade e ausência de confundimento não medido ou análise de sensibilidade.
