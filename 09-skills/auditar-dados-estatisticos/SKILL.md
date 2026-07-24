---
name: auditar-dados-estatisticos
description: Auditar dados antes de análises estatísticas, ciência de dados, machine learning ou estudos causais, avaliando qualidade técnica, semântica, estatística e científica. Usar para verificar esquema, granularidade, chaves, duplicidades, cobertura, completude, valores ausentes, zeros, outliers, consistência, representatividade, viés de seleção, mudanças de coleta, qualidade de mensuração, leakage, disponibilidade temporal e adequação dos dados à pergunta. Produzir diagnóstico, severidade, evidências, impacto analítico e plano de tratamento; priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Auditar dados estatísticos

## Objetivo

Determinar se os dados representam adequadamente o fenômeno, a população e o período necessários para responder à pergunta. Separar defeitos técnicos, comportamentos legítimos e limitações científicas; não “limpar” automaticamente observações apenas por parecerem incomuns.

Se a auditoria fizer parte de um estudo maior, usar também `orientar-analise-estatistica`. Para dependências temporais específicas, combinar com `analisar-series-temporais`.

## Delimitar o contrato analítico

Registrar antes dos testes:

- pergunta, decisão e tipo de conclusão pretendida;
- população-alvo, população observada e unidade de análise;
- granularidade esperada e chaves candidatas;
- período, cobertura geográfica e segmentações;
- desfechos, exposições, features e metadados;
- momento em que cada campo se torna disponível;
- regras de geração, atualização, correção e exclusão;
- fontes, joins e transformações anteriores.

Não declarar um dado “bom” de forma abstrata. Avaliar sua adequação ao uso: descrição, inferência, previsão ou causalidade exigem salvaguardas diferentes.

## Executar a auditoria em camadas

### 1. Estrutura e esquema

Verificar:

- arquivos, tabelas, partições, formatos e codificação;
- nomes, tipos, domínios, unidades e escalas;
- colunas obrigatórias e inesperadas;
- chaves primárias, compostas e estrangeiras;
- granularidade declarada versus observada;
- duplicidades exatas, de chave e semanticamente equivalentes;
- cardinalidades e integridade dos relacionamentos;
- consistência entre fontes e versões.

Não remover duplicidades sem identificar qual registro é válido e qual processo as produziu.

### 2. Cobertura e completude

Medir:

- linhas, entidades, datas e categorias cobertas;
- início e fim da cobertura por segmento;
- densidade esperada versus observada;
- valores ausentes por coluna, linha, grupo e período;
- padrões conjuntos de ausência;
- categorias ou populações completamente não observadas;
- interrupções, atrasos de carga e mudanças abruptas.

Distinguir dado ausente, zero, não aplicável, desconhecido, não coletado e ausência de operação.

Consultar [ausencia-e-cobertura.md](references/ausencia-e-cobertura.md) para classificar mecanismos e tratamentos.

### 3. Validade e consistência

Testar:

- faixas possíveis e plausíveis;
- regras lógicas entre campos;
- sinais, moedas, unidades, escalas e arredondamentos;
- datas impossíveis ou fora de ordem;
- totais e componentes reconciliáveis;
- estabilidade de categorias e códigos;
- mudanças de distribuição associadas a alteração de sistema;
- consistência longitudinal de entidades.

Separar regras universais, regras de negócio e padrões apenas improváveis.

### 4. Distribuições e observações influentes

Examinar:

- posição, dispersão, assimetria, caudas e multimodalidade;
- frequência de zeros e valores-limite;
- outliers univariados, condicionais, multivariados e temporais;
- pontos de alta influência;
- distribuições por grupos relevantes;
- alterações de regime e drift.

Tratar outlier como hipótese investigativa. Não excluir observações usando somente IQR, z-score ou isolamento sem considerar contexto, grupo e processo gerador.

Consultar [outliers-e-mudancas.md](references/outliers-e-mudancas.md).

### 5. Representatividade e mensuração

Avaliar:

- cobertura da população-alvo;
- critérios de inclusão e exclusão;
- amostragem, não resposta e sobrevivência seletiva;
- sobrerrepresentação de grupos, locais ou períodos;
- proxies e validade de construto;
- erro de medição, precisão, resolução e censura;
- mudanças de instrumento, definição ou incentivo;
- variáveis derivadas do próprio resultado.

Declarar quando os dados permitem descrever apenas a população observada, não a população-alvo.

### 6. Leakage e disponibilidade

Construir uma linha do tempo de disponibilidade para alvo e features. Procurar:

- dados criados após o evento previsto;
- agregações que incluam o futuro;
- joins com tabelas revisadas retroativamente;
- imputação, escalonamento ou seleção ajustados antes da divisão;
- atributos que codifiquem diretamente o desfecho;
- duplicatas ou entidades correlatas distribuídas entre treino e teste;
- informação de teste usada em engenharia ou seleção.

Consultar [leakage-e-particionamento.md](references/leakage-e-particionamento.md).

## Quantificar e priorizar achados

Para cada achado, registrar:

| Campo | Conteúdo |
|---|---|
| Evidência | Métrica, regra, amostra ou visual que demonstra o problema |
| Escopo | Colunas, entidades, períodos, grupos e volume afetados |
| Causa provável | Coleta, integração, definição, operação ou fenômeno real |
| Impacto | Descrição, inferência, previsão, causalidade ou uso operacional |
| Severidade | Bloqueador, alta, média, baixa ou informativa |
| Tratamento | Correção na fonte, exclusão, imputação, modelagem, sensibilidade ou documentação |
| Validação | Teste que confirmará se o tratamento funcionou |

Classificar como bloqueador quando o problema inviabilizar a unidade de análise, o desfecho, a identificação causal, a separação treino-teste ou a interpretação central.

## Definir tratamentos

Preferir, nesta ordem:

1. corrigir a fonte ou regra de geração;
2. recuperar informação de fonte confiável;
3. reconstruir joins ou agregações;
4. modelar explicitamente o mecanismo;
5. aplicar tratamento estatístico com análise de sensibilidade;
6. restringir o escopo da conclusão;
7. excluir apenas com justificativa e rastreabilidade.

Comparar resultados antes e depois de imputação, winsorização, transformação ou exclusão quando essas decisões puderem alterar conclusões.

Não imputar o desfecho automaticamente. Não imputar séries temporais usando informação futura fora do cenário real. Não preencher ausência estrutural como se fosse ausência aleatória.

## Implementar

Priorizar:

- SQL para contagens, chaves, integridade, cobertura, reconciliação e testes próximos à fonte;
- Pandas, Polars ou PySpark para perfis reproduzíveis e regras condicionais;
- NumPy e SciPy para métricas e diagnósticos;
- visualizações em Matplotlib, Seaborn ou Plotly;
- Great Expectations, Pandera ou testes equivalentes quando contratos automatizados forem úteis.

Transformar achados confirmados e estáveis em testes de dados automatizados. Manter separadas as regras determinísticas e as anomalias probabilísticas.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico sobre validade, mensuração, ausência, viés e representatividade;
2. procedimento técnico com métricas, regras, segmentações e evidências;
3. interpretação prática do impacto de cada problema;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- parecer de adequação por uso pretendido;
- inventário priorizado de achados;
- problemas bloqueadores;
- tratamentos recomendados e responsáveis quando conhecidos;
- análises de sensibilidade necessárias;
- testes automatizáveis;
- limitações que permanecerão mesmo após a limpeza.
