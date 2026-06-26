# Atividade-Avaliativa-Programa-o-Orientada-a-Objetos-com-Python-
Atividade Avaliativa – Programação Orientada a Objetos com Python 
# FastDelivery Express - Sistema de Gerenciamento 🚚

## 1. Descrição do projeto
Sistema completo desenvolvido via terminal (console) para gerenciamento de entregas urbanas da empresa FastDelivery Express. O sistema controla clientes, entregadores, pedidos, status de entrega e faz cálculos dinâmicos de frete baseados no tipo de entrega selecionada.

## 2. Tecnologias utilizadas
* Python 3
* Git
* GitHub
* Codespaces (Ambiente de desenvolvimento)

## 3. Estrutura de pastas
* `fast_delivery/`: Pasta raiz do projeto.
* `interfaces/`: Contém contratos e classes abstratas do sistema.
* `modelos/`: Contém as classes base e entidades de negócio (Pessoa, Cliente, Entregador, Pedido, Entrega).
* `services/`: Contém as regras de negócio, lógica de cadastro, listagem e cálculos.
* `util/`: Contém funções utilitárias auxiliares, como limpa-tela, menus e formatações.

## 4. Explicação dos conceitos de POO utilizados
* **Herança:** Utilizada criando a superclasse `Pessoa`, a qual compartilha atributos básicos (nome) com as subclasses `Cliente` e `Entregador`.
* **Interface:** Criamos a `CalculoFreteInterface` usando a biblioteca `abc` para forçar o contrato do método `calcular_frete()`.
* **Polimorfismo:** O método `calcular_frete()` atua de formas totalmente diferentes nas classes `EntregaComum`, `EntregaExpressa` e `EntregaPremium`. O sistema não precisa saber qual é a classe exata no momento do Pedido, apenas invoca o método.
* **Encapsulamento:** Utilização de atributos privados (ex: `__nome`, `__cpf`) protegendo o estado dos objetos. O acesso se dá por métodos getters e setters através de `@property`.

## 5. Como executar o projeto
No terminal, navegue até a pasta do projeto e execute o arquivo `main.py`:
## 6. Exemplos de uso
<img width="393" height="283" alt="image" src="https://github.com/user-attachments/assets/888ad6da-f2c4-49b2-858f-d4cd3ed5f294" />
<img width="342" height="221" alt="image" src="https://github.com/user-attachments/assets/300cce8e-1fbd-4fb0-b179-c123a73f6bc1" />
<img width="396" height="244" alt="image" src="https://github.com/user-attachments/assets/3115a59f-a420-445e-9e0e-8ec5a5242182" />
<img width="488" height="166" alt="image" src="https://github.com/user-attachments/assets/ec84ed22-caa0-42d9-9d55-a21c4705d975" />


```bash

cd fast_delivery
python main.py


## 6. Exemplos de uso
<img width="393" height="283" alt="image" src="https://github.com/user-attachments/assets/888ad6da-f2c4-49b2-858f-d4cd3ed5f294" />
<img width="342" height="221" alt="image" src="https://github.com/user-attachments/assets/300cce8e-1fbd-4fb0-b179-c123a73f6bc1" />
<img width="396" height="244" alt="image" src="https://github.com/user-attachments/assets/3115a59f-a420-445e-9e0e-8ec5a5242182" />
<img width="488" height="166" alt="image" src="https://github.com/user-attachments/assets/ec84ed22-caa0-42d9-9d55-a21c4705d975" />

