contador = 0
with open("auth.log", "r")as arquivo:
for linha in arquivo:
    if "FAILED_PASSWORD" in linha:
     partes:linha.split(" "):
     ip = partes[5]
     print("⚠️ BLOQUEIO RECOMENDADO: O IP " + ip + " falhou novamente.")
       contador = contador + 1
           print("ALERTA: TENTATIVA DE INVASÃO DETECTADA ->" + linha.strip())
print("Total de falhas encontradas: ", contador)