# Desenhos de validação

| Cenário | Desenho recomendado | Risco principal |
|---|---|---|
| Observações intercambiáveis | K-fold estratificado | duplicatas e dependência oculta |
| Nova entidade | GroupKFold ou holdout por grupo | mesma entidade em treino e teste |
| Futuro | holdout temporal ou rolling origin | look-ahead |
| Novo local/domínio | holdout externo | domain shift |
| Poucos dados e tuning | nested CV | otimismo da seleção |
| Séries hierárquicas | corte temporal comum e avaliação por nível | incoerência e pesos |
| Dados espaciais | blocos espaciais | autocorrelação próxima |
| Rótulo atrasado | gap/embargo | sobreposição de janelas |

## Princípios

- Dividir primeiro; ajustar transformações depois.
- Repetir folds quando a variância de particionamento for importante.
- Usar conjuntos idênticos para comparar modelos.
- Preservar um teste final após seleção extensiva.
- Preferir validação externa quando a implantação envolver população diferente.
- Declarar quais unidades podem aparecer em mais de um fold.
- Não usar nested CV mecanicamente quando um holdout temporal externo representar melhor o uso.
