---
name: explicar-modelos-e-resultados
description: Explicar modelos estatísticos e de machine learning em níveis global, local e segmentado, escolhendo técnicas compatíveis com o modelo e a pergunta. Usar para interpretar coeficientes, efeitos marginais, importância por permutação, PDP, ICE, ALE, SHAP, contrafactuais, decomposição de forecast e análise de sensibilidade; distinguir funcionamento do modelo, associação observada, efeito causal e recomendação. Verificar estabilidade, dependência entre features e incerteza, evitando tratar explicabilidade como prova causal.
---

# Explicar modelos e resultados

## Definir o objeto da explicação

Esclarecer:

- quem precisa da explicação;
- qual decisão ela apoia;
- se o foco é previsão individual, comportamento global, mecanismo, erro ou auditoria;
- qual conclusão é permitida pelo desenho;
- qual nível de detalhe e risco.

Separar explicação do modelo, dos dados e do fenômeno real.

## Escolher técnicas

- coeficientes e intervalos para modelos paramétricos;
- efeitos marginais para modelos com links ou interações;
- permutation importance para dependência preditiva;
- PDP e ICE para perfis condicionais, com cautela em extrapolação;
- ALE para features correlacionadas;
- SHAP para atribuições locais e agregadas;
- contrafactuais para alternativas factíveis;
- resíduos, erros e ablation para compreender falhas;
- decomposição específica para forecast.

Não aplicar uma técnica apenas por popularidade.

## Verificar validade

Avaliar:

- correlação e dependência entre features;
- regiões sem suporte;
- instabilidade por amostra, tempo e segmento;
- sensibilidade ao modelo de referência;
- incerteza da explicação;
- coerência com sinais e restrições conhecidas;
- efeito do preprocessing;
- disponibilidade temporal das features.

Comparar técnicas quando a conclusão material depender delas.

## Interpretar corretamente

Distinguir:

- associação nos dados;
- regra aprendida pelo modelo;
- contribuição para uma previsão;
- efeito marginal modelado;
- efeito causal identificado.

SHAP positivo não significa que intervir na feature aumentará o target. Importância alta não implica controlabilidade. PDP pode combinar regiões irreais.

## Explicar incerteza e heterogeneidade

Mostrar distribuição, intervalos e variação por grupo, tempo e faixa. Evitar narrativa baseada apenas em média global. Identificar casos em que explicações locais contradizem padrão agregado.

## Produzir comunicação

Entregar em camadas:

1. fundamento do método de explicação;
2. procedimento e limitações técnicas;
3. significado prático e decisão permitida;
4. código Python documentado e visualizações proporcionais.

Apresentar fatos, inferências e hipóteses separadamente. Incluir o que o modelo não permite concluir e quais evidências adicionais seriam necessárias.

## Guardrails

- Não ocultar desempenho fraco com visualizações explicativas.
- Não explicar previsões fora do suporte como se fossem confiáveis.
- Não confundir probabilidade com certeza individual.
- Não produzir contrafactual impossível ou não acionável.
- Não usar explicabilidade para justificar variável sensível ou proxy sem avaliação ética.

Encerrar com principais drivers, direção condicionada, heterogeneidade, estabilidade, limitações e consequência para a decisão.
