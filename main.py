from models import Session, Farmacia, Medicamento

session = Session()

def inserir_farmacias():
    f1 = Farmacia("Raul","Yasmin",True)
    f2 = Farmacia("Henry","Breno",True)
    f3 = Farmacia("Alana", "Paulo", True)
    f4 = Farmacia("Brandom","Anderson", True)

    session.add_all([f1,f2,f3,f4])
    session.commit()

inserir_farmacias()

def inserir_medicamentos():
    md= Medicamento("Dipirona",True,9.99,1)
    md2= Medicamento("Neomicina",True,14.90,3)
    md3= Medicamento("Tadalafila",True,29.99,4)
    md4= Medicamento("Xarope",True,27.90,2)
    md5= Medicamento("DIAD",True,9.99,4)
    md6= Medicamento("Multigrip",True,14.99,2)
    md7= Medicamento("Vitamina-C",True,61.95,3)
    md8= Medicamento("Engov",True,10.33,1)
    md9= Medicamento("Neosaldina",True,7.29,4)
    md10= Medicamento("Vitamina-D",True,37.73,1)

    session.add_all([md,md2,md3,md4,md5,md6,md7,md8,md9,md10])
    session.commit()

inserir_medicamentos()
