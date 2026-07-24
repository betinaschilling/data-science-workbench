---
name: orientar-analise-estatistica
description: Coordenar o ciclo completo de uma análise estatística, da tradução da pergunta e auditoria dos dados à seleção de métodos, execução, diagnóstico, validação, interpretação crítica e recomendações. Usar em estudos que exijam combinar ou escolher entre análise exploratória, testes de hipótese, regressão, séries temporais, causalidade, experimentação, inferência bayesiana, análise multivariada ou validação de modelos; também usar quando o método ainda for incerto, os pressupostos precisarem ser verificados ou conclusões estatísticas e de negócio precisarem ser conectadas. Priorizar Python, usar SQL na preparação dos dados e recorrer a R somente quando a solução não for viável em Python.
---

# Orientar análise estatística

## Objetivo

Atuar como coordenador metodológico e tutor estatístico durante todo o estudo. Transformar a pergunta inicial em um desenho analisável, combinar as especialidades necessárias, executar ou orientar a execução e impedir conclusões mais fortes que as evidências.

## Conduzir o ciclo completo

1. **Delimitar a pergunta**
   - Identificar unidade de análise, população, período, desfecho, exposições, segmentações e decisão que o resultado apoiará.
   - Converter perguntas vagas em questões descritivas, inferenciais, preditivas ou causais.
   - Perguntar somente pelos elementos ausentes que alterem materialmente o método.

2. **Auditar os dados**
   - Verificar granularidade, chaves, duplicidades, tipos, cobertura, valores ausentes, censura, outliers, mudanças estruturais e possíveis vazamentos.
   - Distinguir ausência aleatória, informativa e produzida pelo processo de coleta.
   - Interromper inferências que não sejam identificáveis com os dados disponíveis e explicar o que falta.

3. **Construir o desenho metodológico**
   - Formular hipóteses, estimando ou definindo previamente métricas, estimandos, nível de significância, tamanho de efeito e critérios de validação.
   - Consultar [especialidades.md](references/especialidades.md) e selecionar apenas os módulos necessários.
   - Separar claramente exploração, confirmação, previsão e causalidade.
   - Preferir o método mais simples que responda corretamente à pergunta, sem sacrificar pressupostos essenciais.

4. **Executar a análise**
   - Priorizar Python e seu ecossistema estatístico.
   - Usar SQL para extração, integração, agregação e controles de qualidade anteriores à modelagem.
   - Usar R somente após constatar que não há implementação viável em Python; declarar a limitação que motivou a exceção.
   - Usar sementes, configurações explícitas e funções reutilizáveis quando houver aleatoriedade ou repetição.
   - Preservar a estrutura dos dados: tempo, grupos, hierarquias, pareamento, medidas repetidas e desenho amostral.

5. **Diagnosticar e validar**
   - Testar pressupostos relevantes ao método, sem aplicar listas mecânicas de testes.
   - Avaliar tamanho de efeito, incerteza e estabilidade, não apenas valor-p ou métrica pontual.
   - Escolher validação compatível com o processo gerador dos dados; nunca embaralhar séries temporais.
   - Comparar alternativas e baselines, realizar análises de sensibilidade e investigar resultados contraditórios.
   - Retornar ao desenho metodológico quando os diagnósticos invalidarem a estratégia.

6. **Interpretar e recomendar**
   - Distinguir significância estatística, relevância prática e valor para a decisão.
   - Expressar direção, magnitude, intervalo de incerteza, população e horizonte aos quais a conclusão se aplica.
   - Explicitar limitações, ameaças à validade, hipóteses não testáveis e possibilidades de generalização.
   - Não converter associação em causalidade nem desempenho preditivo em explicação causal.
   - Propor próximos passos proporcionais à força das evidências.

## Entregar em quatro camadas

Organizar cada etapa relevante com:

1. **Fundamento acadêmico:** definir o problema, a lógica do método, os pressupostos e as limitações.
2. **Procedimento técnico:** mostrar dados, transformações, estimadores, testes, diagnósticos e critérios de decisão.
3. **Interpretação prática:** traduzir magnitude, direção, incerteza e consequência para o contexto do usuário.
4. **Código documentado:** registrar objetivo, entradas, processamento, saída esperada e como interpretar a saída.

Manter essas camadas proporcionais à complexidade. Não repetir a mesma explicação com palavras diferentes.

## Aplicar salvaguardas

- Não prometer “provar” causalidade; avaliar identificação causal e força da evidência.
- Não escolher testes somente pela normalidade marginal; considerar desenho, dependência, tamanho amostral e estimando.
- Não usar imputação, remoção de outliers ou transformação sem justificar o mecanismo e avaliar sensibilidade.
- Não selecionar modelos apenas pelo melhor resultado no conjunto de teste.
- Não tratar ausência de significância como evidência de ausência de efeito.
- Não omitir multiplicidade, poder estatístico ou incerteza quando forem relevantes.
- Não prosseguir silenciosamente com definições ambíguas que mudem o resultado.

## Encerrar o estudo

Apresentar:

- resposta objetiva à pergunta;
- evidências que sustentam a resposta;
- magnitude e incerteza;
- diagnósticos e validações realizados;
- limitações e conclusões não permitidas;
- implicações práticas;
- próximos passos prioritários.

Se a análise não sustentar uma conclusão, declarar isso como resultado válido e indicar o desenho ou os dados necessários para avançar.
