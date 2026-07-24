# Priors e modelo generativo

## Construção de priors

1. Definir escala do parâmetro.
2. Identificar valores plausíveis e extremos.
3. Traduzir conhecimento para quantis ou probabilidades.
4. Simular prior predictive.
5. Revisar implicações.
6. Documentar fonte e sensibilidade.

## Padrões

| Parâmetro | Priors candidatos | Cuidado |
|---|---|---|
| Coeficiente padronizado | Normal centrada em zero | escala deve ser conhecida |
| Escala positiva | half-normal, half-t, exponential | massa excessiva perto de zero |
| Probabilidade | Beta | interpretar concentração |
| Correlação | LKJ | eta controla identidade |
| Efeito de grupo | Normal hierárquica | hiperprior da escala |
| Alta dimensão | horseshoe, regularized horseshoe | parametrização e identificação |

## Sensibilidade

Comparar priors plausíveis, especialmente para parâmetros fracamente identificados. Mostrar quando a conclusão é dirigida pelo prior. Priors fortes exigem justificativa; priors vagos podem causar geometria ruim e previsões absurdas.
