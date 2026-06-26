from services.cliente_service import ClienteService
from services.entrega_service import EntregaService
from services.pedido_service import PedidoService
from util.menu import exibir_menu_principal, limpar_tela
from util.formatador import formatar_moeda

def main():
    cliente_service = ClienteService()
    entrega_service = EntregaService()
    pedido_service = PedidoService()

    while True:
        limpar_tela()
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Módulo de Clientes
            print("\n--- CLIENTES ---")
            print("1. Cadastrar | 2. Listar | 3. Buscar")
            sub = input("Opção: ")
            if sub == "1":
                n = input("Nome: ")
                c = input("CPF: ")
                t = input("Telefone: ")
                e = input("Endereço: ")
                cliente_service.cadastrar_cliente(n, c, t, e)
                print("Cliente cadastrado!")
            elif sub == "2":
                for c in cliente_service.listar_clientes():
                    print(f"- {c.nome} (CPF: {c.cpf})")
            elif sub == "3":
                cpf = input("CPF para busca: ")
                cli = cliente_service.buscar_cliente_por_cpf(cpf)
                if cli: print(f"Encontrado: {cli.nome} - {cli.endereco}")
                else: print("Não encontrado.")
            input("\nPressione ENTER para voltar...")

        elif opcao == "2":
            # Módulo Entregador
            print("\n--- ENTREGADORES ---")
            print("1. Cadastrar | 2. Listar")
            sub = input("Opção: ")
            if sub == "1":
                n = input("Nome: ")
                v = input("Veículo: ")
                c = input("CNH: ")
                entrega_service.cadastrar_entregador(n, v, c)
                print("Entregador cadastrado!")
            elif sub == "2":
                for e in entrega_service.listar_entregadores():
                    print(f"- {e.nome} (Veículo: {e.veiculo})")
            input("\nPressione ENTER para voltar...")

        elif opcao == "3":
            # Módulo Pedidos
            print("\n--- PEDIDOS ---")
            print("1. Criar Pedido | 2. Listar | 3. Atualizar Status")
            sub = input("Opção: ")
            if sub == "1":
                cod = input("Código do pedido: ")
                cpf = input("CPF do cliente: ")
                cli = cliente_service.buscar_cliente_por_cpf(cpf)
                if not cli:
                    print("Cliente não encontrado! Cadastre primeiro.")
                else:
                    peso = float(input("Peso (kg): "))
                    dist = float(input("Distância (km): "))
                    print("Tipos: 1-Comum | 2-Expressa | 3-Premium")
                    tipo = int(input("Tipo: "))
                    pedido = pedido_service.criar_pedido(cod, cli, peso, dist, tipo)
                    print(f"Pedido criado! Frete: {formatar_moeda(pedido.valor_frete)}")
            elif sub == "2":
                for p in pedido_service.listar_pedidos():
                    print(f"Pedido {p.codigo} - Cliente: {p.cliente.nome} - Status: {p.status} - Frete: {formatar_moeda(p.valor_frete)}")
            elif sub == "3":
                cod = input("Código do pedido: ")
                print("Status: Em preparação | Saiu para entrega | Entregue | Cancelado")
                novo_stat = input("Digite exatamente o novo status: ")
                try:
                    if pedido_service.atualizar_status(cod, novo_stat):
                        print("Status atualizado!")
                    else:
                        print("Pedido não encontrado.")
                except ValueError as err:
                    print(f"Erro: {err}")
            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    main()