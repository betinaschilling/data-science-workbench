# Seleção de testes

## Mapa inicial

| Pergunta e desenho | Procedimentos candidatos | Observação |
|---|---|---|
| Uma média versus referência | t de uma amostra, teste de permutação, bootstrap | Avaliar estimando e caudas |
| Duas médias independentes | t de Welch, permutação, método robusto | Não presumir variâncias iguais |
| Duas medidas pareadas | t pareado, Wilcoxon, permutação de sinais | Analisar diferenças intrapar |
| Mais de dois grupos | ANOVA de Welch, regressão, Kruskal–Wallis | Planejar contrastes |
| Medidas repetidas | modelo misto, GEE, Friedman | Preservar dependência |
| Uma ou duas proporções | binomial exato, score, Fisher, qui-quadrado | Evitar Wald em amostras pequenas |
| Contingência | qui-quadrado, Fisher, modelos log-lineares | Examinar células esperadas |
| Associação contínua | Pearson, Spearman, Kendall, regressão | Distinguir forma e confundimento |
| Variâncias | Levene/Brown–Forsythe, Fligner | Teste F é frágil à não normalidade |
| Distribuições completas | KS, Anderson–Darling, energia, permutação | Não reduzir à média |
| Equivalência | TOST e intervalo | Definir margens previamente |
| Não inferioridade | teste unilateral e intervalo | Margem deve ser substantiva |

## Interpretação dos não paramétricos

Mann–Whitney não é automaticamente teste de medianas. Sob formas e dispersões diferentes, ele avalia dominância probabilística e pode responder a outra pergunta. Wilcoxon pareado exige atenção à simetria das diferenças para interpretações específicas.

## Quando usar modelos

Preferir regressão, modelos mistos, GEE ou GLM quando houver:

- covariáveis de ajuste;
- mais de um fator;
- interações;
- clusters ou repetição;
- desfechos não gaussianos;
- contrastes específicos;
- dados desbalanceados.

O teste deve emergir do contraste sobre o modelo adequado, não de uma sequência de testes isolados.
