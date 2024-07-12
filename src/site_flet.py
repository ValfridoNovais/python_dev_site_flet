# Titulo: MMPG_Novais
# Botão: Iniciar Chat
    # popup/modal/alerta
        #Título: Bem Vindo ao MMPG_Zap
        # Campo de Texto: Escreva seu nome no chat
        # Botão: Entrar no chat
            #Sumir com o Titulo e o Botão Inicial
            #Fechar o poopup
            #Criar Chat (com a mensagem: Usucari entrou)

# Flet -> aplicativo/site/programa de computador

#importar o flet
import flet as ft

# criar a função principal do seu sistema
def main(pagina: ft.Page):
    titulo = ft.Text("MMPGzap")
    botao_iniciar = ft.ElevatedButton("Iniciar o Chat", on_click=lambda e: abrir_popup(e))

    titulo_janela = ft.Text("Bem vindo ao MMPGzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome pro chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat")

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(e):
        #popup = ft.AlertDialog(title=ft.Text("Popup aberto!"))
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    pagina.add(titulo)
    pagina.add(botao_iniciar)
    pagina.update()

# executar o seu sistema
ft.app(target=main, view=ft.WEB_BROWSER)
