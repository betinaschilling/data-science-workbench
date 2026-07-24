# Efeitos, poder e amostra

## Tamanhos de efeito

| Contexto | Medidas possíveis |
|---|---|
| Diferença contínua | diferença de médias/medianas/quantis, Cohen's d, Hedges' g |
| Pareado | diferença média, d das diferenças, razão de resposta |
| Binário | diferença de risco, risco relativo, odds ratio, NNT |
| Contagem ou taxa | diferença e razão de taxas |
| Associação | correlação, R² parcial, inclinação |
| ANOVA/modelo | contrastes, eta², omega², R² parcial |
| Não paramétrico | rank-biserial, Cliff's delta, probabilidade de superioridade |

Priorizar a escala original. Usar medida padronizada para comparação, não como substituto automático da magnitude prática.

## Intervalos

Alinhar o intervalo ao estimador e ao desenho. Evitar intervalos Wald frágeis para proporções extremas, odds ou pequenas amostras. Considerar score, perfil de verossimilhança, exato ou bootstrap adequado.

## Poder

Poder depende do efeito verdadeiro, variabilidade, amostra, alfa, desenho e método. Incorporar:

- desbalanceamento;
- correlação pareada;
- efeito de desenho em clusters;
- medidas repetidas;
- perdas e não resposta;
- multiplicidade;
- adesão e contaminação.

## Simulação

Usar simulação quando houver modelo misto, regra sequencial, múltiplos desfechos, distribuição complexa ou análise robusta. Simular o processo gerador, aplicar exatamente o pipeline planejado e estimar frequência de decisão correta.
