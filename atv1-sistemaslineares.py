import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd 

dados = {
    "vencimento" : [18, 5, 11, 9, 14, 6, 13, 8, 22, 15, 7, 20, 19, 16, 21, 10, 17, 12],
    "yield" : [2.9, 4.2, 3.2, 3.8, 4.0, 4.5, 3.4, 3.7, 2.1, 4.7, 4.3, 2.7, 2.5, 4.1, 2.3, 3.5, 3.2, 3.2],
    }
media_rendimento = np.mean(dados["yield"])
mediana_rendimento = np.median(dados["yield"])
desvio_padrao_rendimento = np.std(dados["yield"])
coeficiente_var = (desvio_padrao_rendimento / media_rendimento) * 100


x = np.array(dados["vencimento"])
y = np.array(dados["yield"])
x_quadrado = sum(pow(x, 2))
n = len(dados["vencimento"])


m = ((n * (sum(x*y))) - (sum(x))*(sum(y))) / ((n*(sum(pow (x, 2)))) - (pow(sum(x), 2))) # formula de m == a
a = (sum(y) - m * sum(x)) / (n) # formula de b

print("""\n 
======================
    Relatório
======================\n""")
print(f"- Yield médio: {media_rendimento:.3f}")
print(f" - P50 Yield: {mediana_rendimento}")
print(f"- Desvio padrão de Yield: {desvio_padrao_rendimento:.3f} -- Que equivale à {coeficiente_var:.2f}% do Yield Médio")
calculo_preditivo = m * 2 + a
print(f"\n\nAlocando o investimento durante 2 anos, teria um Yield aproximado de: {calculo_preditivo:.2f}%")
calculo_preditivo = m * 25 + a
print(f"Alocando o investimento durante 25 anos, teria um Yield aproximado de: {calculo_preditivo:.2f}%")
print("""\n
Recomendação: Com base na relação encontrada, compensa mais
investir em titulos com vencimentos no curto prazo já que
investir em IPCA+ longo prazo indica a perca de rendimento do
valor investido/rendimento total""")

parametro = ((n * (sum(x*y))) - (sum(x))*(sum(y)))
if parametro > 0:
    print("\n|Após análise, define-se que a reta é positiva, então, quanto mais anos deixar investido, maior rendimento terá|")
else:
    print("\n|Após análise, define-se que a reta é negativa, então, quanto mais anos deixar investido, menor rendimento terá|")


print(f"""\n
    coeficiente angular: {m}
    coeficiente linear: {a}\n""")


pergunta = input("""\n
====================================
Deseja fazer uma simulação? (S/N): """).lower()
if pergunta == 's':
    continuar = True
    while continuar:
        pergunta_anos = int(input("\n - Insira a quantidade de anos que deseja para prever Yield: "))
        calculo_preditivo = m * pergunta_anos + a
        print(f"\n\nAlocando o investimento durante {pergunta_anos} anos, teria um Yield aproximado de: {calculo_preditivo:.2f}%")
        pergunta = input("\n/Deseja fazer uma simulação? (S/N): ").lower()
        if pergunta == 'n':
            print("\nObrigado por fazer a simulação!!!\n")
            break
else:
    continuar = False

y_previsao = a + m * x
plt.scatter(x, y)
plt.plot(x, y_previsao, color="red", linewidth=2.5)
plt.xlabel('Anos')
plt.ylabel('Yield %')
plt.legend()
plt.title('Yield vs Anos')
plt.grid()
plt.show()

df = pd.DataFrame(dados)
df.to_csv("dados_pandas.csv", encoding="utf-8")
