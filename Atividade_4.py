import pandas as pd

def ler_dados_excel(caminho_ficheiro):
# Ler dados do ficheiro Excel e carregar num DataFrame
    return pd.read_excel(caminho_ficheiro)

def calcular_media_notas(dataframe, coluna_notas):
# Calcular a média das notas de cada aluno
    return dataframe[coluna_notas].mean()

def encontrar_aluno_nota_mais_alta(dataframe, coluna_prova):
# Encontrar o aluno com a nota mais alta em uma prova específica
    return dataframe.loc[dataframe[coluna_prova].idxmax()]

def calcular_media_por_prova(dataframe, colunas_provas):
# Calcular a média de notas para cada prova
    return dataframe[colunas_provas].mean()

dados = ler_dados_excel("AtividadePedagogica4_10793_02.xlsx")

for i in range(len(dados.index)):
    notas = dados.loc[i][1:4]
    teste = {"Notas": notas}
    teste_df = pd.DataFrame(teste)
    media_notas = calcular_media_notas(teste_df, "Notas")
    print("Média das Notas:", media_notas)

aluno_nota_mais_alta = encontrar_aluno_nota_mais_alta(dados,"Prova 1")
print("Aluno com a Nota Mais Alta em Prova 1:", aluno_nota_mais_alta[0])
aluno_nota_mais_alta = encontrar_aluno_nota_mais_alta(dados,"Prova 2")
print("Aluno com a Nota Mais Alta em Prova 2:", aluno_nota_mais_alta[0])
aluno_nota_mais_alta = encontrar_aluno_nota_mais_alta(dados,"Prova 3")
print("Aluno com a Nota Mais Alta em Prova 3:", aluno_nota_mais_alta[0])

#Media do Rogério 
media_por_prova = calcular_media_notas(dados, ["Prova 1", "Prova 2", "Prova 3"])
print("Média de Notas por Prova:\n", media_por_prova)