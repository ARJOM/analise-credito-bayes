from dados import base as dados
from dados import bayes

def mostraDados(dados):
    for i in dados:
        print(i)
        for item in dados[i]:
            print(item, dados[i][item], end=" ")
        print("\n")


def infoUsuario(dados, id):
    print(id)
    for item in dados[id]:
        print(item, dados[id][item], end=" ")


def getQuantidade(dados, campo, id):
    quantidade = 0
    for item in dados:
        if dados[item][campo] == id:
            quantidade += 1
    return quantidade


def getQuantidade2(dados, campo, id, id2):
    quantidade = 0
    for item in dados:
        if dados[item][campo] == id and dados[item]["risco"] == id2:
            quantidade += 1
    return quantidade


def carregaDados(bayes, dados):
    for id in dados:
        tupla = dados[id]
        for campo in tupla:
            if campo == "risco":
                bayes[campo]["alto"] = getQuantidade(dados, campo, "alto") / len(dados)
                bayes[campo]["moderado"] = getQuantidade(dados, campo, "moderado") / len(dados)
                bayes[campo]["baixo"] = getQuantidade(dados, campo, "baixo") / len(dados)
                continue
            tupla2 = tupla[campo]

            qtalto = getQuantidade2(dados, campo, tupla2, "alto")
            qtmoderado = getQuantidade2(dados, campo, tupla2, "moderado")
            qtbaixo = getQuantidade2(dados, campo, tupla2, "baixo")

            bayes[campo][tupla2]["alto"] = qtalto / getQuantidade(dados, campo, tupla2)
            bayes[campo][tupla2]["moderado"] = qtmoderado / getQuantidade(dados, campo, tupla2)
            bayes[campo][tupla2]["baixo"] = qtbaixo / getQuantidade(dados, campo, tupla2)
    return bayes


def testa(bayes, tupla):
    riscoalto = bayes["risco"]["alto"]
    riscomoderado = bayes["risco"]["moderado"]
    riscobaixo = bayes["risco"]["baixo"]

    for item in tupla:
        dado = tupla[item]
        print("item", item, "\ndado", dado)
        riscoalto *= bayes[item][dado]["alto"]
        riscomoderado *= bayes[item][dado]["moderado"]
        riscobaixo *= bayes[item][dado]["baixo"]

    total = riscomoderado + riscobaixo + riscoalto
    riscoalto = (riscoalto, "alto")
    riscobaixo = (riscobaixo, "baixo")
    riscomoderado = (riscomoderado, "moderado")
    return max(riscoalto, riscomoderado, riscobaixo), total


bayes = carregaDados(bayes, dados)
maior, total = testa(bayes, {"historico": "bom", "divida": "baixa", "garantia": "nenhuma", "renda": "menor15"})
print(maior[1])
print(maior[0]/total*100, "%")
