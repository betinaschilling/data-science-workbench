---
name: simular-sistemas-e-cenarios
description: Formular, implementar, verificar, validar e interpretar simulações para explorar sistemas, políticas e cenários sob incerteza. Usar para Monte Carlo, propagação de incerteza, eventos discretos, filas, dinâmica de sistemas, microsimulação, modelos baseados em agentes, stress tests e análise de sensibilidade; representar mecanismos, estados, eventos, dependências e intervenções, comparar distribuições de resultados e evitar apresentar cenário como previsão. Priorizar Python e SQL; recorrer a R apenas sem alternativa viável.
---

# Simular sistemas e cenários

## Definir finalidade

Classificar a simulação:

- quantificar incerteza;
- comparar políticas;
- testar capacidade ou filas;
- explorar dinâmica e feedback;
- representar agentes heterogêneos;
- executar stress test;
- avaliar sensibilidade;
- gerar dados sintéticos.

Definir decisão, horizonte, população, estados, métricas e condições de comparação.

## Construir modelo conceitual

Explicitar:

- entidades e agentes;
- estados e transições;
- eventos e relógio;
- regras comportamentais;
- recursos e restrições;
- feedbacks;
- parâmetros e distribuições;
- intervenções e cenários;
- fronteiras do sistema.

Distinguir mecanismo conhecido, hipótese e convenção de modelagem.

## Escolher paradigma

- Monte Carlo para propagação de incerteza;
- eventos discretos para filas, recursos e processos;
- dinâmica de sistemas para estoques, fluxos e feedback;
- microsimulação para trajetórias individuais;
- agentes para interação e emergência;
- bootstrapping ou simulação estatística para distribuição amostral;
- cenários determinísticos para stress tests transparentes.

Usar o paradigma mais simples que represente o mecanismo necessário.

## Parametrizar

Estimar parâmetros com dados quando possível e separar calibração de validação. Para parâmetros incertos, usar distribuições justificadas e dependências plausíveis.

Não usar distribuições independentes por conveniência quando correlações alterarem resultados.

## Verificar e validar

Verificação pergunta se o código implementa o modelo. Validação pergunta se o modelo é adequado ao uso.

Realizar:

- testes unitários e invariantes;
- casos extremos e degenerados;
- balanços;
- comparação com solução analítica simples;
- replicações e erro Monte Carlo;
- validação histórica ou externa;
- análise de sensibilidade;
- calibração;
- revisão substantiva das regras.

Não validar apenas porque a simulação reproduz a média histórica.

## Experimentar

Definir cenários antes de observar resultados. Usar sementes controladas, common random numbers quando útil e replicações suficientes. Comparar distribuições, quantis, probabilidades de risco e trajetórias, não apenas médias.

Para modelos com muitos fatores, considerar desenho de experimentos e análise de sensibilidade global.

## Interpretar

Separar:

- cenário;
- previsão;
- contrafactual;
- stress test;
- resultado condicionado às regras.

Uma simulação mostra consequências do modelo sob premissas, não prova que o mundo seguirá a trajetória.

## Implementar

Priorizar Python com NumPy, SciPy, Pandas, SimPy, SALib e bibliotecas adequadas; SQL para parâmetros e reconciliação. Modularizar estado, eventos, política, métricas e experimentos. Registrar versões, sementes e configurações.

## Entregar

Apresentar modelo conceitual, premissas, dados, parâmetros, verificação, validação, cenários, distribuições de resultados, sensibilidade, limitações, implicações e código documentado.

Indicar quais conclusões são robustas e quais dependem fortemente de premissas.
