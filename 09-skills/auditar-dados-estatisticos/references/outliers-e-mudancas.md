# Outliers, influência e mudanças

## Distinguir fenômenos

- Erro impossível: viola regra física, lógica ou de sistema confirmada.
- Evento raro válido: extremo, mas pertencente ao processo.
- Outlier condicional: incomum apenas dentro de grupo, calendário ou covariáveis.
- Ponto influente: altera substancialmente estimativa ou decisão.
- Mudança de regime: várias observações passam a seguir outro processo.
- Drift de coleta: alteração do instrumento, definição ou cobertura.

## Métodos possíveis

| Contexto | Métodos |
|---|---|
| Univariado | IQR, MAD, quantis robustos, caudas paramétricas |
| Multivariado | distância robusta, Isolation Forest, LOF |
| Regressão | leverage, resíduos studentizados, distância de Cook, DFBETAs |
| Temporal | resíduos de modelo, STL robusta, change-point detection |
| Grupos | regras condicionais, modelos hierárquicos, comparação intragrupo |

Usar métodos como triagem, não como decisão automática.

## Avaliar tratamento

Comparar resultados com:

- dado original;
- correção confirmada;
- exclusão justificada;
- winsorização ou transformação;
- estimador robusto;
- variável indicadora;
- modelagem do regime.

Relatar quando a conclusão depender de poucas observações influentes.
