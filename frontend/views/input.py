import flet as ft

def create_input(state):
    """ Recebe o input de dados do usuário e exibe as métricas de resumo (contagem, média, mediana, valor máximo e mínimo) """
    return ft.Column(
        controls=[
            ft.Text("Conteúdo da aba entrada de dados", size=20), # Placeholder
            ft.Text("Nessa aba terá os botões de entrada de dados (manual, CSV ou Excel) e após inserido os dados, será exibido as métricas de resumo.", size=15)
            # Código da aba 
        ]

    )
