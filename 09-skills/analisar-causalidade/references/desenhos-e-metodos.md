# Desenhos e métodos

| Mecanismo | Desenho ou método | Suposição central |
|---|---|---|
| Randomização | A/B, cluster RCT | atribuição aleatória e execução |
| Confundidores medidos | g-computation, PS, IPW, AIPW, DML | exchangeability condicional |
| Política com adoção temporal | DiD, event study | tendências paralelas e ausência de antecipação |
| Regra por limiar | RDD | continuidade e não manipulação |
| Choque exógeno | IV | exclusão, independência, relevância |
| Uma unidade tratada | synthetic control | donor pool capaz de formar contrafactual |
| Intervenção em série | interrupted time series | tendência contrafactual estável |
| Tratamento no tempo | MSM, g-formula | confundimento temporal medido |
| Heterogeneidade | causal forest, meta-learners | identificação base + overlap |

## Escolha

- Preferir desenho que use conhecimento institucional sobre atribuição.
- Definir estimando antes do estimador.
- Comparar suposições, não apenas métricas.
- Usar doubly robust para proteção contra uma de duas especificações erradas, sem prometer robustez a confundimento não medido.
- Usar matching para construir comparabilidade, não para “provar” balanceamento.
- Usar ML para nuisance functions quando flexibilidade ajudar, com cross-fitting.
