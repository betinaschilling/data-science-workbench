# Diagnóstico e transformações

## Sequência recomendada

1. Confirmar frequência, cobertura e semântica das ausências.
2. Visualizar série bruta e agregações coerentes.
3. Investigar calendário, tendência, sazonalidades e mudanças estruturais.
4. Examinar dependência temporal.
5. Testar propriedades exigidas pela família de modelos candidata.
6. Aplicar transformações dentro do desenho de validação.

## Ferramentas e limites

| Objetivo | Ferramentas possíveis | Cuidado principal |
|---|---|---|
| Tendência e sazonalidade | STL, MSTL, médias móveis, espaço de estados | A decomposição pode vazar informação quando ajustada em toda a amostra |
| Estacionaridade | ADF, KPSS, Phillips–Perron | Resultado depende de termos determinísticos, lags e tamanho amostral |
| Autocorrelação | ACF, PACF, Ljung–Box | Sazonalidade e tendência podem produzir dependência espúria |
| Frequências dominantes | periodograma, espectro | Calendário irregular e tendência distorcem picos |
| Quebras | CUSUM, Bai–Perron, ruptures | Distinguir quebra real de evento pontual ou mudança de coleta |
| Relações defasadas | CCF, prewhitening, regressão dinâmica | Correlação cruzada bruta pode refletir sazonalidade compartilhada |
| Volatilidade | resíduos ao quadrado, ARCH tests | Não confundir heterocedasticidade com sazonalidade da variância |

## Transformações

- Usar log ou Box–Cox quando a variância crescer com o nível e a semântica permitir.
- Usar Yeo–Johnson quando houver zeros ou valores negativos e fizer sentido.
- Diferenciar para remover integração estocástica, não apenas para “passar” em teste.
- Usar diferenças sazonais quando houver raiz unitária sazonal, distinguindo-a de sazonalidade determinística.
- Preservar uma forma de reconstruir previsões na escala original e corrigir viés de retransformação quando necessário.
- Avaliar efeitos das transformações sobre interpretação, intervalos e métricas.

## Dados intermitentes

Identificar séries com muitos zeros e intervalos irregulares de demanda. Comparar métodos como Croston, SBA ou TSB com baselines apropriados e métricas robustas. Distinguir zero de demanda, ausência de observação e indisponibilidade operacional.
