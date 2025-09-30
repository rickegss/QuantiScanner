import flet as ft

from backend.analysis import MotorAnalise
from backend.database import GerenciadorBancoDados

from frontend.views.input import create_input
from frontend.views.history_tab import create_history
from frontend.views.results_tab import create_results

class AppState:
    """ Classe que guarda os dados da aplicação"""
    def __init__(self):
        self.motor_analise = MotorAnalise()
        self.db_manager = GerenciadorBancoDados()
        self.metricas_atuais = None
        self.boxplot_atual = None


def main(page: ft.Page):
    page.title = "QuantiScanner - Análise de Boxplot"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 800
    page.window_height = 600

    app_state = AppState()

    input_content = create_input(app_state)
    history_content = create_history(app_state)
    results_content = create_results(app_state)   

    main_tabs = ft.Tabs(
        selected_index=0,
        animation_duration=350,
        tabs=[
            ft.Tab(text="Entrada de Dados", content=input_content),
            ft.Tab(text="Resultados", content=results_content),
            ft.Tab(text="Histórico", content=history_content)
        ],
        expand=1
    )

    page.add(main_tabs)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
