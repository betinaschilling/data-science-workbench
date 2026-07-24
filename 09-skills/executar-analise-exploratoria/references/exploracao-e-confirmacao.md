# Exploração e confirmação

## Fronteira

Uma hipótese é exploratória quando foi inspirada, selecionada ou refinada após observar os mesmos dados usados para avaliá-la. Valor-p ou intervalo convencional calculado depois dessa seleção não recupera automaticamente validade confirmatória.

## Estratégias

- Separar amostra exploratória e confirmatória quando houver volume suficiente.
- Pré-especificar hipótese, métrica, população, modelo e regra de decisão antes da confirmação.
- Coletar novos dados ou usar período futuro.
- Aplicar correções de multiplicidade quando a família de testes for definida.
- Usar validação cruzada ou bootstrap para estabilidade, sem chamar isso de confirmação causal.
- Relatar resultados exploratórios como geradores de hipótese.

## Sinais de alerta

- testar muitas segmentações e reportar apenas a mais extrema;
- trocar métrica, janela ou transformação até obter um resultado desejado;
- formular a hipótese depois de ver o gráfico e narrá-la como anterior;
- atribuir mecanismo causal a uma associação;
- ignorar grupos sem efeito;
- escolher limites de categorias com base no desfecho;
- tratar baixa amostra como evidência de inexistência.

## Saída recomendada

Rotular achados como:

- descritivo robusto;
- padrão exploratório;
- hipótese candidata;
- resultado confirmatório;
- evidência causal.

Explicar quais etapas adicionais seriam necessárias para subir de nível.
