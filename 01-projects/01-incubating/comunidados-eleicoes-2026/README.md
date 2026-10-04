# ComuniDados — Apuração Eleições 2026

Projeto em incubação para acompanhar a evolução da apuração presidencial de 2026.

## V0

Presidente da República, abrangência Brasil, snapshots a cada 20 minutos e saída HTML estática com marca ComuniDados.

Fonte oficial documentada pelo TSE:
- ambiente: `oficial`;
- eleição federal do 1º turno: `6257`;
- cargo Presidente: `0001`;
- arquivo: EA20 de abrangência Brasil;
- URL construída: `https://resultados.tse.jus.br/oficial/ele2026/6257/dados/br/br-c0001-e006257-u.json`.

O TSE informa limite de 100 requisições por segundo por IP. Esta V0 faz no máximo uma consulta por execução agendada.

## Fluxo

```text
GitHub Actions (20 min)
        |
        v
EA20/TSE -> validação mínima -> raw JSON imutável
        |                         |
        +---- hash/deduplicação --+
        |
        v
dashboard HTML (etapa seguinte após schema observado)
```

## Execução

```bash
python -m pip install -r requirements.txt
python src/collector.py --once
python -m pytest -q
```

## Estado

`incubating`. Os parâmetros e o padrão de URL estão confirmados na documentação oficial. O payload de produção e a execução do workflow permanecem `não verificados` até a primeira execução bem-sucedida registrada no GitHub.

## Fonte e responsabilidade

Dados: Tribunal Superior Eleitoral (TSE). ComuniDados é um painel independente e não oficial.
