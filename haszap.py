import flet as ft 


def main(pagina):

    titulo= ft.Text("Guizap")
    pagina.add(titulo)

    def msg_websocket(mensagem):
        texto=ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(msg_websocket)

    def enviar_mensagem(evento):
        nome_usuario= caixa_nm.value
        txt_campo_mensagem= cp_enviar_mensagem.value
        mensagem=f"{nome_usuario}:{txt_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        cp_enviar_mensagem.value = ""

        pagina.update()
        
    cp_enviar_mensagem=ft.TextField("Digite aqui sua mensagem", on_submit=enviar_mensagem)
    bt_enviar=ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar=ft.Row([cp_enviar_mensagem, bt_enviar])
    chat= ft.Column()


    def entrar_chat(evento):
        popup.open=False
        pagina.remove(titulo)
        pagina.add(chat)
        pagina.remove(botao)
        pagina.add(linha_enviar)
       
        nome_usuario=caixa_nm.value
        mensagem= f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    titulo_popup=ft.Text("Bem vindo ao chat")
    caixa_nm=ft.TextField(label="Digite seu nome")
    bt_popup=ft.ElevatedButon("Entrar no chat", on_click=entrar_chat)
    popup=ft.AlertDialog(title=titulo_popup, content=caixa_nm, actions=[bt_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        

    botao=ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    pagina.add(botao)

