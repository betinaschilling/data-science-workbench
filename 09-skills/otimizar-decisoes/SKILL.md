---
name: otimizar-decisoes
description: Formular, resolver, diagnosticar e comunicar problemas de decisão ótima sob objetivos, restrições e incerteza. Usar para alocação, pricing, orçamento, mix, capacidade, calendário, metas, roteamento ou planejamento; definir variáveis de decisão, função objetivo, restrições, cenários e trade-offs, aplicar programação linear, inteira, não linear, robusta, estocástica ou multiobjetivo e validar a solução operacionalmente. Priorizar Python e SQL; não otimizar previsões sem representar custos, restrições e incerteza.
---

# Otimizar decisões

## Formular

Definir:

- decisão controlável;
- unidade, horizonte e frequência;
- função objetivo em unidades de negócio;
- restrições duras e flexíveis;
- parâmetros estimados;
- incerteza;
- alternativas atuais e baseline;
- critérios de viabilidade e aceitação.

Não converter correlação em alavanca controlável.

## Escolher abordagem

- programação linear para relações lineares contínuas;
- inteira ou mista para escolhas discretas;
- não linear para respostas curvas;
- restrições para escalas e combinações;
- robusta para conjuntos de incerteza;
- estocástica para cenários probabilísticos;
- multiobjetivo para trade-offs;
- heurísticas somente quando métodos exatos forem inviáveis.

Explicar aproximações e garantias.

## Integrar previsões

Usar distribuições ou cenários quando a decisão depender do futuro. Propagar erro e comparar solução determinística, robusta e estocástica. Não tratar previsão pontual como verdade.

## Resolver e diagnosticar

Verificar:

- unidades e sinais;
- viabilidade;
- restrições ativas;
- folgas;
- custos reduzidos ou preços sombra;
- gap de otimalidade;
- sensibilidade;
- estabilidade a parâmetros;
- tempo e escalabilidade.

Investigar inviabilidade antes de relaxar restrições. Relaxamento exige justificativa de negócio.

## Validar

Comparar com baseline, regras atuais e cenários adversos. Fazer backtest quando possível e verificar impacto por segmento, risco de concentração e consequências não intencionais.

Uma solução matematicamente ótima pode ser operacionalmente inválida.

## Implementar

Priorizar SQL para parâmetros e reconciliação; Python com SciPy, PuLP, OR-Tools, Pyomo, CVXPY ou solver adequado. Fixar versões, tolerâncias e sementes quando houver heurística.

Separar dados, modelo, solver e relatório. Criar testes para balanços, limites e invariantes.

## Comunicar

Apresentar ação recomendada, ganho sobre baseline, restrições determinantes, trade-offs, sensibilidade, cenários, risco e condições de reotimização.

Não relatar apenas valor objetivo. Mostrar o que muda na operação.

## Guardrails

- Não otimizar métrica proxy sem validar alinhamento.
- Não ocultar inequidade em uma média global.
- Não relaxar restrição legal, ética ou física.
- Não afirmar causalidade a partir do otimizador.
- Não recomendar solução frágil a pequenas mudanças.

Entregar formulação matemática legível, dados e hipóteses, solução, diagnóstico, validação, interpretação de negócio e código documentado.
