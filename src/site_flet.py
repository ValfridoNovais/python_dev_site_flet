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
import os
import flet as ft

# Diretório onde os arquivos serão armazenados
UPLOAD_DIR = "uploads"

# Cria o diretório de uploads se não existir
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def main(page: ft.Page):
    page.title = "MMPGzap"

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

    upload_picker = ft.FilePicker(on_result=lambda e: enviar_arquivo(e))
    botao_upload_pdf = ft.ElevatedButton("Upload PDF", on_click=lambda _: upload_picker.pick_files())
    botao_upload_imagem = ft.ElevatedButton("Upload Imagem", on_click=lambda _: upload_picker.pick_files())
    botao_upload_audio = ft.ElevatedButton("Upload Áudio", on_click=lambda _: upload_picker.pick_files())
    botao_upload_video = ft.ElevatedButton("Upload Vídeo", on_click=lambda _: upload_picker.pick_files())

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    linha_upload = ft.Row([botao_upload_pdf, botao_upload_imagem, botao_upload_audio, botao_upload_video])
    chat = ft.Column()

    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        page.pubsub.send_all(texto)
        texto_mensagem.value = ""
        page.update()

    def enviar_arquivo(evento):
        if evento.files:
            for f in evento.files:
                # Verifique se o arquivo foi carregado corretamente
                if not f.path:
                    chat.controls.append(ft.Text(f"Erro ao carregar o arquivo: {f.name}"))
                    page.update()
                    return
                
                # Salva o arquivo no diretório de uploads
                file_path = os.path.join(UPLOAD_DIR, f.name)
                with open(file_path, "wb") as file:
                    with open(f.path, "rb") as source_file:
                        file.write(source_file.read())

                # Gera a URL do arquivo
                file_url = f"http://192.168.1.106:8000/{UPLOAD_DIR}/{f.name}"

                texto = f"{campo_nome_usuario.value} enviou um arquivo: {f.name}"
                chat.controls.append(ft.Text(texto))
                if f.name.lower().endswith(".pdf"):
                    chat.controls.append(ft.Text(f"Arquivo PDF: {f.name} (não suportado para visualização)"))
                elif any(f.name.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".gif"]):
                    chat.controls.append(ft.Image(src=file_url))
                elif any(f.name.lower().endswith(ext) for ext in [".mp3", ".wav", ".ogg"]):
                    chat.controls.append(ft.Text(f"Arquivo de áudio: {f.name} (não suportado para visualização)"))
                elif any(f.name.lower().endswith(ext) for ext in [".mp4", ".avi", ".mov"]):
                    chat.controls.append(ft.Text(f"Arquivo de vídeo: {f.name} (não suportado para visualização)"))
                
                # Adiciona link para download
                chat.controls.append(ft.Text(f"Baixar {f.name}", url=file_url, color="blue"))
                
                page.update()

    def entrar_chat(evento):
        page.remove(titulo)
        page.remove(botao_iniciar)
        janela.open = False
        page.add(chat)
        page.add(linha_mensagem)
        page.add(linha_upload)
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        page.pubsub.send_all(texto_entrou_chat)
        page.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(e):
        if janela not in page.overlay:
            page.overlay.append(janela)
        janela.open = True
        page.update()

    page.add(titulo)
    page.add(botao_iniciar)
    page.overlay.append(upload_picker)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, host="192.168.1.106", port=8080)

#ft.app(target=main, view=ft.WEB_BROWSER, server=FastAPIServer(app), host="0.0.0.0", port=8080)


#ft.app(target=main, view=ft.WEB_BROWSER, host="192.168.1.106", port=8080) #Casa
#ft.app(target=main, view=ft.WEB_BROWSER, host="10.14.56.243", port=8080) #Quartel
