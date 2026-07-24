---
name: formular-problema-analitico
description: Traduzir demandas de negócio, pesquisa ou produto em problemas analíticos claros, identificáveis e verificáveis. Usar no início de análises, modelos, experimentos, forecasts ou estudos causais para definir decisão, pergunta, população, unidade de análise, desfecho, horizonte, estimando, restrições, métricas e critérios de sucesso; distinguir descrição, diagnóstico, inferência, previsão, causalidade, simulação e otimização. Detectar perguntas não respondíveis com os dados e evitar começar pela técnica.
---

# Formular problema analítico

## Objetivo

Converter uma demanda vaga em uma especificação que conecte decisão, evidência necessária, dados, método e critério de conclusão. Não sugerir modelo antes de entender qual decisão será apoiada.

## Compreender a decisão

Identificar:

- quem decide e qual ação está disponível;
- resultado desejado e restrições;
- prazo, horizonte e frequência da decisão;
- custo de agir, não agir e errar;
- nível mínimo de efeito ou ganho relevante;
- como o resultado será utilizado.

Se não houver decisão imediata, registrar o objetivo de conhecimento ou aprendizagem.

## Classificar a pergunta

Escolher uma ou mais classes, mantendo-as separadas:

- descritiva: o que ocorreu;
- diagnóstica: onde, quando e com quem ocorreu;
- associativa ou inferencial: quais relações existem;
- preditiva: o que ocorrerá para novas observações;
- causal: o que mudaria sob intervenção;
- experimental: como medir uma intervenção controlada;
- simulatória: o que pode ocorrer sob cenários;
- prescritiva: qual ação otimiza um objetivo.

Não usar “impacto”, “influência” ou “causa” como sinônimos de correlação.

## Especificar o problema

Definir:

1. pergunta principal e perguntas secundárias;
2. população-alvo e população observada;
3. unidade de análise e granularidade;
4. período histórico e horizonte;
5. desfecho ou target;
6. exposições, tratamentos, features e controles;
7. segmentações e hierarquias;
8. momento em que cada informação fica disponível;
9. estimando, quando houver inferência causal;
10. saída esperada: estimativa, probabilidade, ranking, previsão, cenário ou decisão.

Explicitar exclusões de escopo e conclusões que os dados não permitem.

## Mapear dados e riscos

Criar inventário preliminar de fontes, cobertura, chaves, frequência, latência e qualidade conhecida. Antecipar:

- viés de seleção;
- ausência informativa;
- censura;
- confundimento;
- leakage;
- mudança de definição;
- quebra estrutural;
- interferência;
- baixa potência;
- desalinhamento entre proxy e conceito.

Encaminhar auditoria detalhada para `auditar-dados-estatisticos`.

## Definir sucesso

Separar:

- critério estatístico: incerteza, tamanho de efeito, calibração ou desempenho;
- critério técnico: reprodutibilidade, estabilidade e latência;
- critério de negócio: valor, risco, custo ou capacidade operacional;
- critério de aprendizagem: conhecimento novo e decisão futura habilitada.

Definir baseline e regra de decisão antes de observar o resultado final.

## Selecionar rota metodológica

Indicar famílias de métodos e skills candidatas, sem fechar prematuramente:

- exploração;
- teste de hipótese;
- regressão;
- séries temporais;
- causalidade;
- experimento;
- análise multivariada;
- inferência bayesiana;
- aprendizado supervisionado ou não supervisionado;
- simulação ou otimização.

Justificar a rota pelo desenho dos dados e pela pergunta, não pela popularidade da técnica.

## Controlar ambiguidades

Perguntar somente por informações ausentes que mudem materialmente desenho ou conclusão. Para pontos não bloqueadores, declarar suposição provisória e seu efeito.

Pausar quando houver escolha humana sobre target, população, imputação, exclusões, efeito mínimo, função de custo ou decisão final.

## Entregar a especificação

Produzir:

- contexto e decisão;
- pergunta analítica;
- classificação;
- hipótese ou estimando;
- população, unidade, período e horizonte;
- variáveis e disponibilidade temporal;
- dados necessários;
- riscos;
- critérios de sucesso;
- plano metodológico inicial;
- entregáveis;
- decisões pendentes.

Usar linguagem acadêmica, técnica e de negócio sem repetir conteúdo. Incluir código apenas quando necessário para verificar viabilidade ou estrutura dos dados.
