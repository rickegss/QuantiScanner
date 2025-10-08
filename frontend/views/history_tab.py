import flet as ft

def criar_aba_historico(estado, pagina, abas_principais):
    """ Aba de histórico e integração com o database """
    return ft.Column(
        controls=[
            ft.Text("Conteúdo da aba histórico", size=20), # Placeholder
            ft.Text("Nessa aba exibirá as análises salvas, podendo o usuário renomear uma análise ou carregá-la.")
            # Código da aba 
        ]
    
    )