# Portabilidade entre modelos

## Contrato comum

Todo agente deve ler primeiro `AGENTS.md`, localizar a habilidade em `09-skills/manifest.yaml` e carregar integralmente apenas os `SKILL.md` necessários. As instruções do repositório prevalecem sobre sugestões genéricas do modelo.

## Claude

O arquivo `CLAUDE.md` encaminha para as regras canônicas. Em uma sessão, peça: “Leia AGENTS.md e use 09-skills/<nome>/SKILL.md para esta tarefa”.

## Gemini

O arquivo `GEMINI.md` aplica o mesmo encaminhamento. Carregue o skill desejado como contexto do workspace.

## GitHub Copilot

`.github/copilot-instructions.md` encaminha para `AGENTS.md` e para a coleção. Em prompts, cite explicitamente o caminho da habilidade.

## Outros modelos

Inclua no contexto, nesta ordem:

1. `AGENTS.md`;
2. o pedido atual;
3. o `SKILL.md` selecionado;
4. referências requeridas pela habilidade;
5. arquivos do projeto relevantes.

Não concatene todas as habilidades. Isso aumenta conflito de instruções e reduz a qualidade do raciocínio.
