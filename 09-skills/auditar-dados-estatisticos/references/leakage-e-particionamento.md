# Leakage e particionamento

## Tipos de leakage

- Target leakage: feature contém ou deriva do resultado.
- Look-ahead: usa informação posterior ao instante da decisão.
- Train-test contamination: a preparação aprende com o conjunto de avaliação.
- Entity leakage: mesma entidade ou cópias correlatas aparecem nos dois lados.
- Temporal overlap: janelas compartilham períodos ou alvos.
- Revision leakage: usa dado histórico revisado que não existia na época.
- Selection leakage: o conjunto final influencia features, hiperparâmetros ou escolha do modelo.

## Auditoria de disponibilidade

Para cada variável, registrar:

- instante do evento representado;
- instante de captura;
- instante de processamento;
- instante de disponibilidade confiável;
- revisões posteriores;
- disponibilidade futura em produção.

Usar o último desses instantes relevante para decidir se a feature pode entrar na origem da previsão.

## Particionamento

- Usar divisão aleatória somente quando observações forem intercambiáveis.
- Separar por grupo quando novas entidades forem o objetivo.
- Separar temporalmente quando o futuro for o objetivo.
- Aplicar gap quando janelas, rótulos atrasados ou dependência próxima causarem contaminação.
- Ajustar transformações, imputadores e seletores dentro de cada fold.
- Reservar avaliação final quando houver seleção extensa.

## Evidência

Comparar desempenho com e sem features suspeitas e verificar se a variável poderia ser calculada em um replay histórico fiel. Desempenho excepcionalmente alto é sinal de investigação, não prova de leakage.
