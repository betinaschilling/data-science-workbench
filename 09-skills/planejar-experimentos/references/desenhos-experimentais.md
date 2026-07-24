# Desenhos experimentais

| Contexto | Desenho | Cuidado |
|---|---|---|
| Usuários independentes | A/B individual | cross-device e contaminação |
| Lojas, cidades ou equipes | cluster RCT | ICC e poucos clusters |
| Tratamentos combináveis | fatorial | interação e multiplicidade |
| Mesma unidade recebe variantes | crossover | carryover e período |
| Mercado muda no tempo | switchback | autocorrelação e washout |
| Rollout obrigatório | stepped-wedge | tendência temporal |
| Muitos braços | A/B/n ou adaptativo | multiplicidade e seleção |
| Efeito de rede | cluster/rede | interferência |

## Princípios

- Randomizar na menor unidade que preserve independência suficiente.
- Usar estratificação para covariáveis prognósticas importantes.
- Planejar análise conforme a atribuição.
- Definir washout em crossover ou switchback.
- Evitar desenho adaptativo quando inferência confirmatória não estiver corretamente ajustada.
- Distinguir bandit, que otimiza regret, de experimento voltado à estimação precisa.
