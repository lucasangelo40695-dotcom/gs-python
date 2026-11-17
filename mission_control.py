# Nome da missão: Keys-1
# Nome da equipe: Equipe Keys
# Integrantes:
# Gustavo Guedes Pereira – RM: 569779
# Lucas Angelo Colesanti – RM: 569530
# Gabriel Rodrigues – RM: 569322
# RM dos integrantes: 569779, 569530, 569322
# Link do vídeo pitch no YouTube:
# https://www.youtube.com/watch?v=cygPftukCl4


NOME_MISSAO = "Keys-1"
NOME_EQUIPE = "Equipe Keys"

dados_missao = [
    [22, 95, 97, 98, 94],
    [25, 88, 85, 97, 90],
    [33, 58, 70, 95, 72],
    [37, 45, 41, 92, 61],
    [41, 24, 16, 84, 33],
    [35, 38, 27, 79, 46],
    [29, 66, 44, 88, 68],
]

descricao_ciclos = [
    "Lançamento e início da missão",
    "Inserção em órbita e estabilização",
    "Tempestade solar afeta o sinal",
    "Falha parcial no painel solar",
    "Pane múltipla nos sistemas",
    "Manobra de emergência",
    "Tentativa de recuperação",
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]

rotulos = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]
unidades = [" °C", "%", "%", "%", "%"]

recomendacoes_criticas = [
    "Verificar controle térmico da missão.",
    "Tentar restabelecer contato com a base.",
    "Ativar modo de economia de energia.",
    "Acionar protocolo de suporte à vida.",
    "Reduzir operações não essenciais.",
]

PONTOS = {"NORMAL": 0, "ATENÇÃO": 1, "CRÍTICO": 2}

LARGURA = 60


def analisar_temperatura(temperatura):
    if temperatura < 18:
        return "ATENÇÃO", "Temperatura abaixo do ideal"
    elif temperatura <= 30:
        return "NORMAL", "Temperatura estável"
    elif temperatura <= 35:
        return "ATENÇÃO", "Temperatura elevada"
    else:
        return "CRÍTICO", "Risco de superaquecimento"


def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "CRÍTICO", "Comunicação com a base em nível crítico"
    elif comunicacao < 60:
        return "ATENÇÃO", "Comunicação instável"
    else:
        return "NORMAL", "Comunicação estável"


def analisar_bateria(bateria):
    if bateria < 20:
        return "CRÍTICO", "Bateria em nível crítico"
    elif bateria < 50:
        return "ATENÇÃO", "Bateria abaixo do recomendado"
    else:
        return "NORMAL", "Energia estável"


def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return "CRÍTICO", "Oxigênio em nível crítico"
    elif oxigenio < 90:
        return "ATENÇÃO", "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", "Oxigênio adequado"


def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return "CRÍTICO", "Estabilidade operacional crítica"
    elif estabilidade < 70:
        return "ATENÇÃO", "Estabilidade operacional reduzida"
    else:
        return "NORMAL", "Estabilidade operacional adequada"


funcoes_analise = [
    analisar_temperatura,
    analisar_comunicacao,
    analisar_bateria,
    analisar_oxigenio,
    analisar_estabilidade,
]


def analisar_ciclo(ciclo):
    resultados = []
    for posicao in range(len(ciclo)):
        classificacao, mensagem = funcoes_analise[posicao](ciclo[posicao])
        resultados.append((classificacao, mensagem, PONTOS[classificacao]))
    return resultados


def calcular_risco_ciclo(resultados):
    total = 0
    for resultado in resultados:
        total += resultado[2]
    return total


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados, pontuacao):
    areas_criticas = []
    areas_atencao = []
    for posicao in range(len(resultados)):
        if resultados[posicao][0] == "CRÍTICO":
            areas_criticas.append(posicao)
        elif resultados[posicao][0] == "ATENÇÃO":
            areas_atencao.append(posicao)

    if len(areas_criticas) >= 3:
        return ("Ativar modo de segurança e priorizar suporte à vida, "
                "energia e comunicação.")

    if len(areas_criticas) > 0:
        textos = []
        for posicao in areas_criticas:
            textos.append(recomendacoes_criticas[posicao])
        return " ".join(textos)

    if classificar_ciclo(pontuacao) == "MISSÃO EM ATENÇÃO":
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    if len(areas_atencao) > 0:
        nomes = []
        for posicao in areas_atencao:
            nomes.append(areas_monitoradas[posicao])
        return "Ação preventiva em: " + ", ".join(nomes) + "."

    return "Manter operação normal e continuar monitoramento."


def analisar_tendencia(riscos):
    primeiro = riscos[0]
    ultimo = riscos[-1]
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def calcular_pontos_por_area(todos_resultados):
    pontos_area = [0] * len(areas_monitoradas)
    for resultados in todos_resultados:
        for posicao in range(len(resultados)):
            pontos_area[posicao] += resultados[posicao][2]
    return pontos_area


def identificar_area_mais_afetada(pontos_area):
    indice_maior = 0
    for posicao in range(1, len(pontos_area)):
        if pontos_area[posicao] > pontos_area[indice_maior]:
            indice_maior = posicao
    return areas_monitoradas[indice_maior]


def calcular_medias(matriz):
    medias = []
    for coluna in range(len(matriz[0])):
        soma = 0
        for linha in matriz:
            soma += linha[coluna]
        medias.append(soma / len(matriz))
    return medias


def gerar_conclusao(classificacao_final, tendencia, ciclos_criticos):
    if classificacao_final == "MISSÃO CRÍTICA":
        return ("A missão está em estado crítico. É necessário manter o modo de "
                "segurança ativo e avaliar o retorno ou abortar a operação.")
    if ciclos_criticos > 0 and "melhora" in tendencia:
        return ("A missão enfrentou momentos críticos, mas os sistemas se "
                "recuperaram. Recomenda-se manter o monitoramento reforçado.")
    if ciclos_criticos > 0:
        return ("A missão apresentou instabilidade relevante durante a operação. "
                "Apesar da tentativa de recuperação, ainda existem sistemas em "
                "atenção e a equipe deve manter o plano de contingência ativo.")
    if classificacao_final == "MISSÃO EM ATENÇÃO":
        return ("A missão operou com alertas moderados. A equipe deve acompanhar "
                "de perto as áreas em atenção.")
    return "A missão operou dentro dos parâmetros esperados durante todo o período."


def exibir_cabecalho():
    print("=" * LARGURA)
    print("MISSION CONTROL AI")
    print("=" * LARGURA)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * LARGURA)


def exibir_ciclo(numero, ciclo, resultados, pontuacao, classificacao, recomendacao):
    print()
    print(f"CICLO {numero} — {descricao_ciclos[numero - 1]}")
    print("-" * LARGURA)
    for posicao in range(len(ciclo)):
        status, mensagem, _ = resultados[posicao]
        print(f"{rotulos[posicao]}: {ciclo[posicao]}{unidades[posicao]} | "
              f"{status} | {mensagem}")
    print()
    print(f"Pontuação de risco do ciclo: {pontuacao}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}")


def gerar_relatorio_final(riscos, classificacoes, todos_resultados):
    medias = calcular_medias(dados_missao)
    maior_risco = max(riscos)
    ciclo_mais_critico = riscos.index(maior_risco) + 1
    risco_medio = sum(riscos) / len(riscos)
    ciclos_criticos = classificacoes.count("MISSÃO CRÍTICA")
    tendencia = analisar_tendencia(riscos)
    pontos_area = calcular_pontos_por_area(todos_resultados)
    area_mais_afetada = identificar_area_mais_afetada(pontos_area)
    classificacao_final = classificar_ciclo(round(risco_medio))

    print()
    print("=" * LARGURA)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * LARGURA)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print()
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print()
    print(f"Média de temperatura: {medias[0]:.2f} °C")
    print(f"Média de comunicação: {medias[1]:.2f}%")
    print(f"Média de bateria: {medias[2]:.2f}%")
    print(f"Média de oxigênio: {medias[3]:.2f}%")
    print(f"Média de estabilidade: {medias[4]:.2f}%")
    print()
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {ciclos_criticos}")
    print()
    print("Tendência da missão:")
    print(tendencia)
    print()
    print("Pontuação acumulada por área:")
    for posicao in range(len(areas_monitoradas)):
        print(f"{areas_monitoradas[posicao]}: {pontos_area[posicao]} pontos")
    print()
    print("Área mais afetada:")
    print(area_mais_afetada)
    print()
    print("Classificação final da missão:")
    print(classificacao_final)
    print()
    print("Conclusão:")
    print(gerar_conclusao(classificacao_final, tendencia, ciclos_criticos))
    print("=" * LARGURA)


def main():
    exibir_cabecalho()

    riscos = []
    classificacoes = []
    todos_resultados = []

    for indice in range(len(dados_missao)):
        ciclo = dados_missao[indice]
        resultados = analisar_ciclo(ciclo)
        pontuacao = calcular_risco_ciclo(resultados)
        classificacao = classificar_ciclo(pontuacao)
        recomendacao = gerar_recomendacao(resultados, pontuacao)

        exibir_ciclo(indice + 1, ciclo, resultados, pontuacao,
                     classificacao, recomendacao)

        riscos.append(pontuacao)
        classificacoes.append(classificacao)
        todos_resultados.append(resultados)

    gerar_relatorio_final(riscos, classificacoes, todos_resultados)


if __name__ == "__main__":
    main()
