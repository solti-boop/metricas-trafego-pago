def dividir(a, b):
    return a / b if b else 0


def ctr(cliques, impressoes):
    return dividir(cliques, impressoes) * 100


def cpc(investimento, cliques):
    return dividir(investimento, cliques)


def cpa(investimento, conversoes):
    return dividir(investimento, conversoes)


def roas(receita, investimento):
    return dividir(receita, investimento)


if __name__ == "__main__":
    investimento = float(input("Investimento (R$): "))
    impressoes = int(input("Impressões: "))
    cliques = int(input("Cliques: "))
    conversoes = int(input("Conversões: "))
    receita = float(input("Receita (R$): "))

    print(f"CTR: {ctr(cliques, impressoes):.2f}%")
    print(f"CPC: R$ {cpc(investimento, cliques):.2f}")
    print(f"CPA: R$ {cpa(investimento, conversoes):.2f}")
    print(f"ROAS: {roas(receita, investimento):.2f}")
