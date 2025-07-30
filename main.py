import csv

with open("dados.csv", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha["nome"]
        nota = float(linha["nota"])


        if nota>7:
          print(f"{nome} passou com {nota}")
          print ("Parabens!!!!!!!!!!!!!!!!!!!!!!!")


        media = sum(float(linha["nota"]) for linha in leitor) / len(linha["nota"])
        print("sua media é : " ,  media)