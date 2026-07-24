# Escolha de visualizações

| Pergunta | Visualizações candidatas |
|---|---|
| Como uma variável se distribui? | histograma, ECDF, densidade, boxplot, violin com pontos |
| Como grupos diferem? | box/violin, intervalos, ridgeline, small multiples |
| Duas variáveis se relacionam? | dispersão, hexbin, contorno, curva suave |
| Como uma métrica evolui? | linha, pontos, bandas, small multiples |
| Qual a composição? | barras empilhadas, barras de 100%, área quando houver tempo |
| Há concentração? | Pareto, Lorenz, ECDF, treemap apenas quando hierarquia importar |
| Como muitas variáveis se relacionam? | matriz de correlação filtrada, pairplot amostrado, parallel coordinates com cautela |
| Há padrão espacial? | mapa coroplético com denominadores adequados, pontos ou hexágonos |
| Há valores ausentes? | matriz de ausência, barras por grupo, padrão temporal |

## Regras

- Usar barras a partir de zero quando o comprimento codificar magnitude.
- Mostrar pontos ou distribuição quando médias esconderem heterogeneidade.
- Exibir incerteza quando o gráfico sugerir comparação inferencial.
- Usar escalas logarítmicas somente com indicação explícita.
- Ordenar categorias por significado ou valor.
- Limitar cores e reservar cor forte para informação prioritária.
- Preferir small multiples a sobrepor séries demais.
- Adaptar gráficos à densidade: dispersão para poucos pontos, hexbin ou agregação para milhões.
