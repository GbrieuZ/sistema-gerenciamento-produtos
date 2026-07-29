import streamlit as st

# Configuracao da pagina (titulo da aba do navegador e icone)
st.set_page_config(page_title="Controle de Estoque", page_icon="📦", layout="centered")

if "inventario" not in st.session_state:
    st.session_state.inventario = {}

# Atalho pra escrever menos daqui pra baixo
inventario = st.session_state.inventario

# Titulo principal
st.title("📦 Controle de Estoque")
st.caption("Sistema de gerenciamento de inventário de produtos — versão web")

# As abas substituem o menu de numeros do terminal
aba_add, aba_listar, aba_remover, aba_atualizar = st.tabs(
    ["➕ Adicionar", "📋 Listar", "🗑️ Remover", "✏️ Atualizar"]
)

# ------------------------------------------------------------------
#  ADICIONAR PRODUTO  (opcao 1 do terminal)
# ------------------------------------------------------------------
with aba_add:
    st.subheader("Adicionar produto ao estoque")

    nome = st.text_input("Nome do produto")
    quantidade = st.number_input("Quantidade", min_value=0, step=1, value=0)
    preco = st.number_input("Preço (R$)", min_value=0.0, step=0.01, value=0.0, format="%.2f")

    if st.button("Adicionar produto"):
        # Guardamos sempre em minusculas, igual voce fazia no terminal
        nome_tratado = nome.strip().lower()

        # As mesmas validacoes do terminal
        if not nome_tratado:
            st.error("Informe o nome do produto.")
        elif nome_tratado.isdigit():
            st.error("Informe apenas palavras no nome do produto.")
        elif nome_tratado in inventario:
            st.warning(f"O produto '{nome_tratado}' já está cadastrado. Use a aba Atualizar.")
        else:
            inventario[nome_tratado] = {
                "quantidade": int(quantidade),
                "preco": float(preco),
            }
            st.success(f"Produto '{nome_tratado}' adicionado com sucesso!")

# ------------------------------------------------------------------
#  LISTAR PRODUTOS  (opcao 2)
# ------------------------------------------------------------------
with aba_listar:
    st.subheader("Produtos no estoque")

    if not inventario:
        st.info("Nenhum produto cadastrado.")
    else:
        # Monta uma tabela ordenada por nome, ja com o valor total (qtd x preco)
        tabela = []
        valor_total_estoque = 0.0
        for nome_prod, dados in sorted(inventario.items()):
            total = dados["quantidade"] * dados["preco"]
            valor_total_estoque += total
            tabela.append({
                "Produto": nome_prod,
                "Quantidade": dados["quantidade"],
                "Preço (R$)": f"{dados['preco']:.2f}",
                "Total (R$)": f"{total:.2f}",
            })

        st.dataframe(tabela, use_container_width=True, hide_index=True)

        # Metricas resumidas — dao cara de sistema de verdade
        col1, col2 = st.columns(2)
        col1.metric("Produtos cadastrados", len(inventario))
        col2.metric("Valor total em estoque", f"R$ {valor_total_estoque:.2f}")

# ------------------------------------------------------------------
#  REMOVER PRODUTO  (opcao 3)
# ------------------------------------------------------------------
with aba_remover:
    st.subheader("Remover produto")

    if not inventario:
        st.info("Nenhum produto cadastrado.")
    else:
        # selectbox = lista suspensa; substitui o "digite o nome" do terminal
        escolha = st.selectbox("Escolha o produto para remover", sorted(inventario.keys()))
        if st.button("Remover produto"):
            del inventario[escolha]
            st.success(f"Produto '{escolha}' removido com sucesso!")
            st.rerun()  # recarrega a tela pra o item sumir da lista

# ------------------------------------------------------------------
#  ATUALIZAR PRODUTO  (opcao 4)
# ------------------------------------------------------------------
with aba_atualizar:
    st.subheader("Atualizar produto")

    if not inventario:
        st.info("Nenhum produto cadastrado.")
    else:
        escolha = st.selectbox(
            "Escolha o produto para atualizar", sorted(inventario.keys()), key="att_escolha"
        )
        dados_atuais = inventario[escolha]
        st.write(
            f"Quantidade atual: **{dados_atuais['quantidade']}**  |  "
            f"Preço atual: **R$ {dados_atuais['preco']:.2f}**"
        )

        nova_qtd = st.number_input(
            "Nova quantidade", min_value=0, step=1, value=dados_atuais["quantidade"]
        )
        novo_preco = st.number_input(
            "Novo preço (R$)", min_value=0.0, step=0.01,
            value=dados_atuais["preco"], format="%.2f"
        )

        if st.button("Salvar alterações"):
            inventario[escolha] = {
                "quantidade": int(nova_qtd),
                "preco": float(novo_preco),
            }
            st.success(f"Produto '{escolha}' atualizado com sucesso!")
            st.rerun()
