import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import statistics as st


dados ={
    "velocidade" : [1/2,1/4,1/8,1/15,1/30,1/60,1/125,1/250,1/500,1/1000],
    "brilho" : [200,190,175,171,168,150,148,140,131,127]
}

x = np.array(dados["velocidade"])
y = np.array(dados["brilho"])

media = np.mean(dados["brilho"])
mediana = np.median(dados["brilho"])
moda = st.mode(dados["brilho"])
desvio_padrao = np.std(dados["brilho"])
decil = np.percentile(dados["brilho"], [10, 20, 30, 40, 50, 60, 70, 80, 90])
variancia_amostral_brilho = np.var(y, ddof=1)
variancia_amostral_velocidade = np.var(x, ddof=1)

print(f"""
\nmedia: {media}
\nmediana: {mediana}
\nmoda: {moda}
\ndesvio padrão: {desvio_padrao}
\nvariância amostral brilho: {variancia_amostral_brilho}
\nvariância amostral velocidade: {variancia_amostral_velocidade}""")

contador = 1
for i in range(9):
    print(f"{contador}° decil: {decil[i]}")
    contador+=1


a, b = np.polyfit(x, y, deg=1)
regressao_linear = a * x + b

print(f"Coeficiente angular {a}, Coeficiente linear: {b}")
print(f"\nRegressão linear: {regressao_linear}\n")


print(f"""
\n
    Principal Insight:
Após análise dos dados, comprova-se a existência de uma tendência de relação direta e proporcional da velocidade de abturação e aumento do brilho da imagem
\n""")

plt.scatter(x, y)
plt.title("Velocidade de abturação X Brilho da imagem")
plt.xlabel("Velocidade de abturação")
plt.ylabel("Brilho da imagem")
plt.grid()
plt.show()