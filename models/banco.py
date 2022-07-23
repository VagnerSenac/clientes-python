# Model - O que vem do banco de dados (BD)
def model_usuario():
    arquivo = open("models\\usuarios.txt","r+")  #abre o arquivo dados em formato de leitura
    conteudo = arquivo.readlines() #retorna uma LISTA DE STRINGS
    for linha in conteudo:
        usuario_senha = linha.split(";") #quebra a linha indicando no ;
    usuario_BD = usuario_senha[0]     #indica que o primeiro item é o usuário
    return usuario_BD

def model_senha():
    arquivo = open("models\\usuarios.txt","r+")  #abre o arquivo dados em formato de leitura
    conteudo = arquivo.readlines() #retorna uma LISTA DE STRINGS
    for linha in conteudo:
        usuario_senha = linha.split(";")  #quebra a linha indicando no ;
    senha_BD = usuario_senha[1]     #indica que o segundo item é a senha
    return senha_BD

print(model_senha())
