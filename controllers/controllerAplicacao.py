import models.banco as banco
import views.formulario as view

# Controller - a validação
def validar_login(usuario_completo):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()
    if usuario_completo[0] == usuario_BD and usuario_completo[1] == senha_BD:
        view.exibir_mensagem("                        Bem vindo !!!!")
        opcoes_menu()
    else:
        view.exibir_mensagem("                    Usuário ou Senha Inválido")
        iniciar()

def iniciar():
    #usuario_completo = view.formulario_login()
    #validar_login(usuario_completo)
    validar_login(view.formulario_login())
    
def opcoes_menu():
    opcao = view.menu()
    if opcao == '1':
        cadastrar_cliente()
        
    elif opcao == '2':
        print("Listagem de clientes")
    else:
        view.exibir_mensagem("                        Sistema finalizado")
        exit()

def cadastrar_cliente():
    cliente = view.cadastro_cliente()

