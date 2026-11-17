# Mission Control AI — Keys-1

Global Solution 2026.1 — Pensamento Computacional e Automação com Python (FIAP).

Sistema em Python que simula o monitoramento inteligente de uma missão espacial experimental.
A "inteligência" é baseada em regras lógicas (sem bibliotecas externas e sem machine learning).

## Como executar

```bash
python mission_control.py
```

Requer apenas Python 3.

## Estrutura dos dados

- `dados_missao`: matriz (lista de listas) com **7 ciclos**; cada linha segue a ordem
  `[temperatura, comunicacao, bateria, oxigenio, estabilidade]`.
- `areas_monitoradas`: nomes das áreas, na mesma ordem das colunas da matriz.

| Ciclo | Evento simulado |
|---|---|
| 1 | Lançamento e início da missão |
| 2 | Inserção em órbita e estabilização |
| 3 | Tempestade solar afeta o sinal |
| 4 | Falha parcial no painel solar |
| 5 | Pane múltipla nos sistemas |
| 6 | Manobra de emergência |
| 7 | Tentativa de recuperação |

## Regras de alerta

Foram mantidos os limites sugeridos no enunciado.

| Área | NORMAL | ATENÇÃO | CRÍTICO |
|---|---|---|---|
| Temperatura (°C) | 18 a 30 | < 18 ou > 30 até 35 | > 35 |
| Comunicação (%) | ≥ 60 | 30 a 59 | < 30 |
| Bateria (%) | ≥ 50 | 20 a 49 | < 20 |
| Oxigênio (%) | ≥ 90 | 80 a 89 | < 80 |
| Estabilidade (%) | ≥ 70 | 40 a 69 | < 40 |

**Pontuação:** NORMAL = 0, ATENÇÃO = 1, CRÍTICO = 2 (máximo 10 por ciclo).

**Classificação do ciclo:** 0–2 MISSÃO ESTÁVEL · 3–5 MISSÃO EM ATENÇÃO · 6–10 MISSÃO CRÍTICA.

**Tendência:** compara o risco do primeiro e do último ciclo (piora / melhora / estável).

**Área mais afetada:** área com maior soma de pontos ao longo de todos os ciclos
(em caso de empate, vale a primeira na ordem da lista).

**Classificação final da missão:** risco médio dos ciclos, arredondado, aplicado nas mesmas faixas do ciclo.

## Recomendações automáticas (por ciclo)

1. 3 ou mais áreas críticas → ativar modo de segurança e priorizar suporte à vida, energia e comunicação.
2. 1 ou 2 áreas críticas → recomendação específica de cada área crítica
   (controle térmico, restabelecer contato, economia de energia, suporte à vida, reduzir operações).
3. Ciclo em atenção sem áreas críticas → monitorar e preparar plano de contingência.
4. Ciclo estável com alguma área em atenção → ação preventiva nas áreas em atenção.
5. Tudo normal → manter operação normal.

## Funções

`analisar_temperatura`, `analisar_comunicacao`, `analisar_bateria`, `analisar_oxigenio`,
`analisar_estabilidade`, `analisar_ciclo`, `calcular_risco_ciclo`, `classificar_ciclo`,
`gerar_recomendacao`, `analisar_tendencia`, `calcular_pontos_por_area`,
`identificar_area_mais_afetada`, `calcular_medias`, `gerar_conclusao`,
`exibir_cabecalho`, `exibir_ciclo`, `gerar_relatorio_final`, `main`.

## Equipe

- Gustavo Guedes Pereira — RM 569779
- Lucas Angelo Colesanti — RM 569530
- Gabriel Rodrigues — RM 569322

Vídeo pitch: https://www.youtube.com/watch?v=cygPftukCl4
