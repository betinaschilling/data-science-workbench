# ComuniDados — Apuração Eleições 2026

Projeto em incubação para construir um painel independente da evolução da apuração presidencial de 2026.

## V0

Escopo aprovado: Presidente, Brasil, snapshots planejados a cada 20 minutos e dashboard HTML estático com marca ComuniDados.

Fluxo proposto:

```text
TSE -> coleta única -> preservação raw -> normalização -> histórico -> build HTML
```

A automação periódica e a publicação ainda não são tratadas como validadas. O endpoint oficial deve ser confirmado por execução antes de habilitar agendamento.

## Estrutura

- `project.yaml`: manifesto e gates.
- `src/`: coleta, normalização, persistência e geração HTML.
- `tests/`: testes unitários sem dependência da API.
- `data/`: criada em runtime; dados brutos não devem ser alterados.
- `reports/`: saída HTML gerada em runtime.

## Execução planejada

```bash
python -m pip install -r requirements.txt
python src/collector.py --once
python src/build_dashboard.py
python -m pytest -q
```

## Estado

Incubating. Acesso real ao endpoint, esquema observado, execução do coletor e publicação: não verificados.

## Fonte e responsabilidade

Dados: Tribunal Superior Eleitoral (TSE). ComuniDados é um painel independente e não oficial.
