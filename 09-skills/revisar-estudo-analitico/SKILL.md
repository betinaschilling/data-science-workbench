---
name: revisar-estudo-analitico
description: Revisar de forma independente a validade de estudos estatísticos, causais, preditivos e de ciência de dados, desde a pergunta e os dados até o código, a interpretação e a recomendação. Usar para peer review, auditoria metodológica, revisão de notebooks, relatórios, experimentos, modelos ou conclusões; detectar desenho inadequado, leakage, confundimento, multiplicidade, suposições violadas, validação enviesada, baixa reprodutibilidade e extrapolações de negócio. Emitir parecer rastreável por severidade sem alterar silenciosamente o estudo. Priorizar Python e SQL nas verificações.
---

# Revisar estudo analítico

## Mandato

Atuar como revisor independente. Avaliar se as evidências sustentam as conclusões e se o estudo pode orientar a decisão pretendida. Não assumir que escolhas do autor estão corretas e não reescrever o projeto sem autorização.

## Reunir evidências

Solicitar ou localizar apenas o necessário:

- pergunta, decisão e população;
- fontes, dicionário, filtros e transformações;
- plano analítico e hipóteses;
- código, configurações, versões e logs;
- resultados, diagnósticos e validações;
- relatório e recomendações.

Marcar como `não verificável` o que não puder ser inspecionado. Não preencher lacunas com suposições.

## Revisar por camadas

1. **Pergunta e desenho**
   - Diferenciar descrição, inferência, previsão, causalidade e prescrição.
   - Verificar população, unidade, horizonte, estimando e decisão.
   - Avaliar se o desenho permite responder à pergunta.

2. **Dados**
   - Verificar granularidade, chaves, duplicidade, cobertura, ausência, censura, seleção e mudanças de coleta.
   - Rastrear filtros, joins, agregações e proxies.
   - Procurar informação futura e variáveis derivadas do target.

3. **Método**
   - Conferir compatibilidade com o desenho e a dependência dos dados.
   - Avaliar pressupostos, multiplicidade, poder, tamanho de efeito e incerteza.
   - Não aceitar correlação, Granger, importância ou SHAP como prova causal.

4. **Validação**
   - Verificar baseline, particionamento, tuning, teste intocado, estabilidade e análise de erro.
   - Exigir backtesting para tempo e separação por grupo quando houver dependência.
   - Conferir comparação justa entre modelos e segmentos.

5. **Código e reprodutibilidade**
   - Procurar bugs, mutações silenciosas, sementes ausentes, caminhos frágeis e resultados não reproduzíveis.
   - Executar testes seguros quando possível.
   - Distinguir resultado executado de resultado apenas esperado.

6. **Interpretação e decisão**
   - Comparar cada afirmação com a evidência que a sustenta.
   - Separar significância, relevância prática e valor econômico.
   - Identificar generalização indevida, omissão de incerteza e recomendação sem mecanismo.

## Classificar achados

Usar:

- `bloqueador`: invalida a conclusão central ou impede reprodução;
- `alto`: pode mudar substancialmente resultado ou decisão;
- `médio`: reduz robustez, validade ou generalização;
- `baixo`: melhoria importante, sem alterar a conclusão central;
- `observação`: esclarecimento ou evolução futura.

Para cada achado registrar: identificador, evidência, localização, consequência, correção recomendada, reteste e status.

## Manter independência

- Não aprovar o próprio trabalho sem declarar conflito.
- Não modificar dados, excluir observações ou trocar método durante a revisão.
- Não tratar ausência de evidência como evidência de ausência.
- Não bloquear por preferência estética ou técnica.
- Aceitar risco metodológico somente como decisão humana documentada.

## Emitir parecer

Entregar:

1. conclusão executiva: aprovado, aprovado com ressalvas, revisão necessária ou não confiável;
2. escopo e materiais revisados;
3. achados ordenados por severidade;
4. conclusões sustentadas;
5. conclusões não sustentadas;
6. plano mínimo de correção e reteste;
7. riscos residuais.

Usar quatro camadas quando houver desenvolvimento: fundamento acadêmico, diagnóstico técnico, impacto para o negócio e código de verificação documentado.
