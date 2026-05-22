import flet as ft

def main(page: ft.Page):
    def clicar(e):
        texto.value="App Flet"
        page.update()


    texto= ft.Text("Usando o flet")
    botao= ft.ElevatedButton("Clique aqui", on_click=clicar)

    page.add(texto, botao)

ft.app(target=main)
