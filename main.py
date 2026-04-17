from models import Session, Farmacia, Medicamento

session = Session()

def inserir_farmacias():
    with Session() as session:
        try:
            nome = input("Nome da farmácia: ")
            responsavel = input("Responsável: ")

            f = Farmacia(nome, responsavel, True)

            session.add(f)
            session.commit()

            print("Farmácia inserida com sucesso!")

        except Exception as erro:
            session.rollback()
            print(f"Erro: {erro}")

#inserir_farmacias()

def inserir_medicamentos():
    with Session() as session:
        try:
            nome = input("Nome: ")
            preco = float(input("Preço: "))

            farmacias = session.query(Farmacia).all()
            for f in farmacias:
                print(f"{f.id} - {f.responsavel}")

            farmacia_id = int(input("ID farmácia: "))

            m = Medicamento(nome, True, preco, farmacia_id)

            session.add(m)
            session.commit()

            print("Medicamento cadastrado!")

        except Exception as erro:
            session.rollback()
            print(f"Erro: {erro}")

#inserir_medicamentos()

def listar_filhos():
    with Session() as session:
        try:
            medicamentos = session.query(Medicamento).all()

            print("\n=== MEDICAMENTOS ===")
            for m in medicamentos:
                print(f"{m.nome} | preço: {m.preco} | farmacia: {m.farmacia_id}")

        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro: {erro}")
#listar_filhos()

def filtrar_filhos():
    with Session() as session:
        try:
            filtro = input("Digite o id: ")
            medicamentos = session.query(Medicamento).filter_by(farmacia_id=filtro).all()

            print("\n=== MEDICAMENTOS ===")
            for m in medicamentos:
                print(f"{m.nome} | preço: {m.preco} | farmacia: {m.farmacia_id}")

        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro: {erro}")

#filtrar_filhos()

def listar_pais_com_filhos():
    with Session() as session:
        try:
            input("Enter para listar farmácias com medicamentos")

            farmacias = session.query(Farmacia).all()

            print("\n=== FARMÁCIAS COM MEDICAMENTOS ===")

            for f in farmacias:
                medicamentos = session.query(Medicamento).filter_by(farmacia_id=f.id).all()

                if medicamentos:
                    print(f"ID: {f.id}")

        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro: {erro}")


def upd_pai():
    with Session() as session:
        try:
            id = input("Digite o id da Farmacia que deseja atualizar: ")
            farmacia = session.query(Farmacia).filter_by(id=id).first()

            print("\n === ATUALIZAR DADOS DA FARMÁCIA ===")

            if not farmacia:
                print("Não encontrada:")
                return 
            
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro: {erro}")
