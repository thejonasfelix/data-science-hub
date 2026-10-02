corretora_agora = {"ITSA4", "ECOR3", "TAEE11", "B3SA3", "VALE3"}
corretora_ativa = {"B3SA3", "BBDC4", "BBSE3", "BRDT3", "TAEE11", "TRPL4", "VALE3", "VIVT3"}
corretora_genial = {"CPFE3", "BEEF3", "CYRE3", "SAPT4", "TRPL4"}
corretora_easynvest = {"B3SA3", "AGRO3", "COCA34", "TAEE11", "VALE3", "CPLE11", "ITSA4", "ABEV3"}
corretora_elite = {"BBDC4", "BBSE3", "BRSR6", "EGIE3", "ITSA4", "SAPR11", "TAEE11", "TRPL4", "VIVT3", "VALE3"}
corretora_guide = {"ALUP11", "BBAS3", "CYRE3", "CPFE3", "KLBN11", "PSSA3", "TIMS3", "VALE3"}
corretora_nova_futura = {"B3SA3", "CYRE3", "GGBR4", "VIVT3", "TRPL4"}
corretora_orama = {"ABCB4", "BBDC4", "BEEF3", "CESP6", "EGIE3"}

acao_comum = corretora_agora.intersection(corretora_ativa, corretora_genial, corretora_easynvest, corretora_elite, corretora_guide, corretora_nova_futura, corretora_orama)
if acao_comum == True:
    print(acao_comum)
else:
    print("\nNão existe ação em comum comparando todas as corretoras \n")

acao_comum_espec = corretora_genial.intersection(corretora_easynvest, corretora_elite, corretora_guide)
if acao_comum_espec == True:
    print(acao_comum_espec)
else:
    print("Não existe ação em comum entre essas 4 corretoras \n")

print("Ações Únicas de cada corretora")
acao_unica_01 = corretora_genial.difference(corretora_easynvest, corretora_elite, corretora_guide)
print(f"Genial: {acao_unica_01}")
acao_unica_02 = corretora_easynvest.difference(corretora_genial, corretora_elite, corretora_guide)
print(f"Easynvest: {acao_unica_02}")
acao_unica_03 = corretora_elite.difference(corretora_genial, corretora_easynvest, corretora_guide)
print(f"Elite: {acao_unica_03}")
acao_unica_04 = corretora_guide.difference(corretora_genial, corretora_easynvest, corretora_elite)
print(f"Guide: {acao_unica_04}")

if corretora_genial.issubset(corretora_easynvest):
    print("Genial é subconjunto da Easynvest")
elif corretora_genial.issuperset(corretora_easynvest):
    print("Genial é superconjunto da Easynvest")
elif corretora_genial.issubset(corretora_elite):
    print("Genial é subconjunto da Elite")
elif corretora_genial.issuperset(corretora_elite):
    print("Genial é superconjunto da Elite")
elif corretora_genial.issubset(corretora_guide):
    print("Genial é subconjunto da Guide")
elif corretora_genial.issuperset(corretora_guide):
    print("Genial é superconjunto da Guide")
else:
    print("\nGenial Não é subconjunto e nem superconjunto\n")


if corretora_easynvest.issubset(corretora_genial):
    print("Easynvest é subconjunto Genial")
elif corretora_easynvest.issuperset(corretora_genial):
    print("Easynvest é superconjunto Genial")
elif corretora_easynvest.issubset(corretora_elite):
    print("Easynvest é subconjunto Elite")
elif corretora_easynvest.issuperset(corretora_elite):
    print("Easynvest é superconjunto Elite")
elif corretora_easynvest.issubset(corretora_guide):
    print("Easynvest é subconjunto Guide")
elif corretora_easynvest.issuperset(corretora_guide):
    print("Easynvest é superconjunto Guide")
else:
    print("Easynvest Não é subconjunto e nem superconjunto\n")
        

if corretora_elite.issubset(corretora_genial):
    print("Elite é subconjunto Genial")
elif corretora_elite.issuperset(corretora_genial):
    print("Elite é superconjunto Genial")
elif corretora_elite.issubset(corretora_easynvest):
    print("Elite é subconjunto Easynvest")
elif corretora_elite.issuperset(corretora_easynvest):
    print("Elite é superconjunto Easynvest")
elif corretora_elite.issubset(corretora_guide):
    print("Elite é subconjunto Guide")
elif corretora_elite.issuperset(corretora_guide):
    print("Elite é superconjunto Guide")
else:
    print("Elite Não é subconjunto e nem superconjunto\n")


if corretora_guide.issubset(corretora_genial):
    print("Guide é subconjunto Genial")
elif corretora_guide.issuperset(corretora_genial):
    print("Guide é superconjunto Genial")
elif corretora_guide.issubset(corretora_easynvest):
    print("Guide é subconjunto Easynvest")
elif corretora_guide.issuperset(corretora_easynvest):
    print("Guide é superconjunto Easynvest")
elif corretora_guide.issubset(corretora_elite):
    print("Guide é subconjunto Elite")
elif corretora_guide.issuperset(corretora_elite):
    print("Guide é superconjunto Elite")
else:
    print("Guide Não é subconjunto e nem superconjunto\n")

combinacao_acoes = acao_unica_01.union(acao_unica_02,acao_unica_03, acao_unica_04)
print(f"Conjunto de ações únicas de cada corretora: \n{combinacao_acoes}")
