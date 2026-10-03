import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


dados = {
    "hora" : ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00","18:00"],
    "usuarios": [10, 12, 15, 25, 22, 18, 15, 20, 28, 30],
    "cpu":[20.0, 25.2, 30.0, 45.1, 42.7, 33.6, 31.5, 45.0, 53.1, 60.2],
}

media_cpu = np.mean(dados["cpu"])
mediana_cpu = np.median(dados["cpu"])
desv_padrao_cpu = np.std(dados["cpu"])

media_users = np.mean(dados["usuarios"])
mediana_user = np.median(dados["usuarios"])
desv_padrao_user = np.std(dados["usuarios"])

print(f"""
Média de consumo da CPU: {media_cpu:.2f}
Mediana de consumo da CPU: {mediana_cpu:.1f}
Desvio padrão de consumo da CPU: {desv_padrao_cpu:.1f}
Média de usuários no sistema: {media_users:.1f}
Mediana de usuários no sistema: {mediana_user:.1f}
Desvio padrão de usuários no sistema: {desv_padrao_user:.1f}
""")

x = np.array(dados["usuarios"])
y = np.array(dados["cpu"])

delta_x = x - media_users
delta_y = y - media_cpu
m = sum(delta_x * delta_y) / sum(pow(delta_x, 2))
b = media_cpu - (m * media_users)

teste_users = 50
exemplo_rl = (m * teste_users) + b
print(f"\nFazendo o teste com 50 usuarios, o consumo de CPU será de: {exemplo_rl:.2f}%")
teste_users = 0
exemplo_rl = (m * teste_users) + b
print(f"Fazendo o teste com {teste_users} usuarios, o consumo de CPU será de: {exemplo_rl:.2f}%")
print(f"Isso válida a hipotese possui uma correlação direta entre os números, já que a cada novo usuário o consumo da CPU cresce em {m:.2f}, partindo de {b:.2f}")

qtd_users = int(input("""
-------------------------------------------------------------------------
Teste de previsão do sistema.
-------------------------------------------------------------------------
\nInsira a quantidade de usuários que deseja para prever a uso da CPU: """))
modelo_prev = (m * qtd_users) + b
print(f"\nSe {qtd_users} usuarios estiverem ativos no sistema, o uso da CPU será de aproximadamente: {modelo_prev:.2f}%")

teste_users = 20
exemplo_rl = (m * teste_users) + b
print(f"\n\nSe às 19:00h possuir {teste_users} usuarios ativos no sistema, o uso da CPU será de aproximadamente: {exemplo_rl:.2f}%")

print("""
==============================================================================================
O modelo linear assume que cada usuário consome a mesma taxa fixa do processador,na prática
a taxa de processamento tende a variar, pois, com poucos usuários ativos o sistema tende a
melhor distribuir seus recursos, já sob alta demanda, os usuários disputam os mesmos núcleos
de processadores e memória, fazendo o consumo disparar de forma não linear. 
==============================================================================================
""")

plt.figure(figsize=(8, 4.5))
plt.scatter(x, y)
plt.title("Uso CPU vs Users")
plt.xlabel("Qtd usuários")
plt.ylabel("Porcentagem CPU")
plt.show()

dados_extra = {
    "cpu" : [10, 15, 30, 50, 70],
    "usuários" : [5, 10, 20, 30, 40]
}

x2 = np.array(dados_extra["usuários"])
y2 = np.array(dados_extra["cpu"])

def exponential_function(u, a, b):
    return a * np.exp(b * u)
params, covariance = curve_fit(exponential_function, x2, y2, maxfev = 7000)
a_fit, b_fit = params
predicted_cpu_usage = exponential_function(x2, a_fit, b_fit)
print("\nfitted parameters:")
print(f"Sem usuários o gasto da CPU é de: {a_fit}%")
print(f"Taxa de aceleração do consumo de CPU: {b_fit}")
plt.scatter(x2, y2, label='data')
plt.plot(x2, predicted_cpu_usage, label='fitted curve', color='red')
plt.xlabel('Usuários')
plt.ylabel('Uso da CPU (%)')
plt.legend()
plt.title('Uso da CPU vs. Usuários ativos (fitted curve)')
plt.grid()
plt.show()