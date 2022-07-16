#View - o que vai pro usuário do sistema
#Função
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha: ")
    import validacao
    validacao.validar_login()
    validar_login(usuario_digitado, senha_digitado)
