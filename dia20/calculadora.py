import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora"

    numero1 = ft.TextField(label="Primeiro número")
    numero2 = ft.TextField(label="Segundo número")

    resultado = ft.Text("Resultado:")

    operacoes = ft.Dropdown(
        label="Escolha a operação",
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/"),
        ],
    )

    def calcular(e):
        try:
            n1 = float(numero1.value)
            n2 = float(numero2.value)

            operacao = operacoes.value

            if operacao == "+":
                conta = n1 + n2
            elif operacao == "-":
                conta = n1 - n2
            elif operacao == "*":
                conta = n1 * n2
            elif operacao == "/":
                conta = n1 / n2
            else:
                resultado.value = "Escolha uma operação"
                page.update()
                return

            resultado.value = f"Resultado: {conta}"

        except ValueError:
            resultado.value = "Digite números válidos"

        except ZeroDivisionError:
            resultado.value = "Não é possível dividir por zero"

        page.update()

    botao = ft.ElevatedButton(
        "Calcular",
        on_click=calcular
    )

    page.add(
        numero1,
        numero2,
        operacoes,
        botao,
        resultado
    )


ft.app(target=main)