inventario = {}

def principal():

    while True:
        print("\n------ MENU ------")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Remover produto")
        print("4 - Atualizar quantidade de produto")
        print("5 - Sair do programa")
        print("-------------------")

        try:
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue
        
        if opcao < 1 or opcao > 5:
            print("Opção inválida. Tente novamente.")
            continue
    
        if opcao == 1:
            while True:
                nome_produto = (input("Digite o nome do produto ou pressione ENTER para sair: "))
                nome_produto = nome_produto.lower()
                if nome_produto == "":
                    break
                
                if nome_produto.isdigit():
                    print("Informe apenas palavras. Tente novamente.")
                    continue
                
                try:
                    quantidade_produto = int(input("Digite a quantidade do produto: "))
                    preco_produto = float(input("Digite o preco do produto: "))
                except ValueError:
                    print('A quantidade e o preco devem ser numeros. Tente novamente.')
                    continue
                inventario[nome_produto] = {
                    "quantidade": quantidade_produto,
                    "preco": preco_produto
                }
                print(f"Produto {nome_produto} adicionado com sucesso!")
                
        elif opcao == 2:
            if not inventario:
                print("Nenhum produto cadastrado.")
                input("Presione ENTER para voltar ao menu")
                continue
            else:
                for chave, valor in inventario.items():
                    print("\n------ CARRINHO ------")
                    print(f"Nome: {chave}, Quantidade: {valor['quantidade']}, Preço: R${valor['preco']:.2f}")
                    print("---------------------")
                    
                input("Presione ENTER para voltar ao menu")
        
        elif opcao == 3:
            if not inventario:
                print("Nenhum produto cadastrado.")
                input("Presione ENTER para voltar ao menu")
                continue
            
            print("\n------ CARRINHO ------")
            for nome_produto in inventario:
                print(f"{nome_produto}")
            print("---------------------")
            
            remover = input("Digite o nome do produto que deseja remover ou ENTER para sair: ")
            remover = remover.lower()            
            if remover == "":
                continue
            
            if remover.isdigit():
                print("Informe apenas palavras. Tente novamente.")
                continue
            
            if remover not in inventario:
                print(f"Produto {remover} nao encontrado.")
            else:
                del inventario[remover]
                print(f"Produto {remover} removido com sucesso!")
            
            input("Presione ENTER para voltar ao menu")
            continue
        
        elif opcao == 4:
            if not inventario:
                print("Nenhum produto cadastrado.")
                input("Presione ENTER para voltar ao menu")
                continue
            
            for chave, valor in inventario.items():
                print("\n------ CARRINHO ------")
                print(f"Nome: {chave}, Quantidade: {valor['quantidade']}, Preço: R${valor['preco']:.2f}")
                print('---------------------')
            
            att = input("Digite o nome do produto que deseja atualizar ou ENTER para sair: ")
            att = att.lower()
            if att == "":
                continue
            
            if att.isdigit():
                print("Informe apenas palavras. Tente novamente.")
                continue
                        
            if att not in inventario:
                print(f"O produto {att} não foi encontrado.")
            else:
                try:
                    quantidade_produto = int(input("Digite a quantidade do produto: "))
                    preco_produto = float(input("Digite o preco do produto: "))
                except ValueError:
                    print('A quantidade e o preco devem ser numeros. Tente novamente.')
                    continue
                inventario[att] = {
                    "quantidade": quantidade_produto,
                    "preco": preco_produto
                }
                print(f"Produto {att} atualizado com sucesso!")
            
            input("Presione ENTER para voltar ao menu")
            continue
        
        elif opcao == 5:
            print("PROGRAMA ENCERRADO")
            break
            
if __name__ == "__main__":            
    principal()