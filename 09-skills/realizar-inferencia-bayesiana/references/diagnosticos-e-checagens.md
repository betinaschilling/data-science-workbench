# Diagnósticos e checagens

## Computação

| Diagnóstico | Sinal | Ação |
|---|---|---|
| R-hat | próximo de 1 | investigar valores elevados |
| ESS bulk/tail | precisão de média/caudas | aumentar eficiência ou draws |
| Divergências | geometria problemática | reparametrizar, revisar priors/modelo |
| Tree depth | trajetórias truncadas | revisar geometria e configuração |
| BFMI | exploração de energia | reparametrizar escalas |
| Trace/rank | mixing e modos | revisar inicialização e multimodalidade |

Não usar um limiar isolado. Avaliar todos os parâmetros e quantidades derivadas importantes.

## Simulation-based calibration

Para modelos ou implementações complexas:

1. amostrar parâmetros do prior;
2. simular dados;
3. ajustar o modelo;
4. verificar ranks da verdade;
5. repetir.

Usar também parameter recovery em cenários substantivamente relevantes.

## Predictive checks

Escolher estatísticas que revelem falhas importantes: média, variância, zeros, extremos, dependência, grupos, sazonalidade e função de perda. Não depender apenas de sobreposição visual global.
