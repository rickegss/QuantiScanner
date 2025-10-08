import flet as ft

def criar_aba_resultados(estado, pagina):
    """ Exibe o gráfico boxplot e quartis, decis, percentis """
    return ft.Column(
        controls=[
            ft.Text("Conteúdo da aba resultados", size=20), # Placeholder
            ft.Text("Nessa aba será exibido o gráfico de boxplot, quartis, decis e percentis, além de um botão para salvar a análise no banco de dados.")
            # Código da aba 
        ]

    )