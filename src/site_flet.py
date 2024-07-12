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
def main(page: ft.Page):
    page.title = "MMPGzap"
    #page.favicon = "path/to/your/favicon.ico"  # Atualize com o caminho para o seu favicon

    titulo = ft.Text("MMPGzap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        page.update()

    page.pubsub.subscribe(enviar_mensagem_tunel)

    botao_iniciar = ft.ElevatedButton("Iniciar o Chat", on_click=lambda e: abrir_popup(e))

    titulo_janela = ft.Text("Bem vindo ao MMPGzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome pro chat", on_submit=lambda e: entrar_chat(e))

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=lambda e: enviar_mensagem(e))
    botao_enviar = ft.ElevatedButton("Enviar", on_click=lambda e: enviar_mensagem(e))

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    chat = ft.Column()

    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        # Enviar mensagem no chat
        page.pubsub.send_all(texto)
        texto_mensagem.value = ""
        page.update()

    def entrar_chat(evento):
        # Tirar Título da página
        page.remove(titulo)
        # Tirar o botão iniciar
        page.remove(botao_iniciar)
        # Fechar o popup/janela
        janela.open = False
        # Criar o chat
        page.add(chat)
        # Criar o campo de texto para enviar mensagem
        page.add(linha_mensagem)
        # Escrever a mensagem: novais entrou no chat
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        page.pubsub.send_all(texto_entrou_chat)
        #chat.controls.append(ft.Text(texto_entrou_chat))
        page.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(e):
        page.dialog = janela
        janela.open = True
        page.update()

    page.add(titulo)
    page.add(botao_iniciar)
    page.update()

# executar o seu sistema
#ft.app(target=main, view=ft.WEB_BROWSER, host="0.0.0.0", port=8080)


ft.app(target=main, view=ft.WEB_BROWSER, host="192.168.1.102", port=8080)
