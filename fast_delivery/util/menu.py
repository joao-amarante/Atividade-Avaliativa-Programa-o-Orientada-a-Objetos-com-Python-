import os

def limpar_tela():
    """Limpa o console de acordo com o sistema operacional"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu_principal():
    print("=" * 40)
    print(" FAST DELIVERY EXPRESS - GERENCIAMENTO")
    print("=" * 40)
    print("1. Módulo de Clientes")
    print("2. Módulo de Entregadores")
    print("3. Módulo de Pedidos")
    print("0. Sair")
    print("=" * 40)