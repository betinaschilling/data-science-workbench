# Clusterização

| Estrutura esperada | Métodos candidatos |
|---|---|
| Grupos aproximadamente esféricos | k-means |
| Robustez e distância arbitrária | k-medoids |
| Hierarquia | aglomerativo |
| Densidades e ruído | DBSCAN/HDBSCAN |
| Elipses probabilísticas | Gaussian mixture |
| Fronteiras não convexas | spectral |
| Classes latentes | latent class/profile |
| Formas temporais | k-shape, DTW, features + clustering |

## Número de clusters

Combinar:

- silhouette;
- Calinski–Harabasz;
- Davies–Bouldin;
- gap statistic;
- BIC/AIC para mixtures;
- estabilidade;
- tamanho mínimo;
- interpretabilidade;
- ação possível.

## Validação

- repetir seeds;
- usar bootstrap/subsampling;
- calcular ARI ou Jaccard entre soluções;
- testar distâncias e escalas;
- validar em período ou amostra externa;
- comparar distribuição de resultados externos;
- verificar overfitting de perfis.

Clusters podem ser um contínuo cortado artificialmente. Reportar sobreposição e probabilidades quando apropriado.
