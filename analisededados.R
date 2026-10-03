library(ggplot2)

df_grupo <- captura_dados_lowlatency
df_grupo

summary(df_grupo)

media <- mean(df_grupo$cpuPorcentagemUso)
cat(media)

maiorconsumo <- df_grupo[which.max(df_grupo$cpuPorcentagemUso),]
maiorconsumo


menorconsumo <- df_grupo[which.min(df_grupo$cpuPorcentagemUso),]
menorconsumo

hist(df_grupo$cpuPorcentagemUso,
     main= "Histograma Componentes",
     xlab = "Uso da Cpu(%)",
     ylab = "Frequência",
     col = "red")

plot(df_grupo$cpuPorcentagemUso, df_grupo$ramPercentualUso,
     xlab = "Uso da CPU (%)",
     ylab = "Uso da RAM (%)",
     col="red")

summary(lm(df_grupo$cpuPorcentagemUso~df_grupo$ramPercentualUso))

df_grupo[1,]

modelo <-lm(df_grupo$cpuPorcentagemUso ~ df_grupo$dtRegistro) 
modelo
plot(modelo)
abline(modelo, col="red", lwd = 5)

plot(df_grupo$ramPercentualUso, df_grupo$downloadRede)


ggplot(mapping = aes(df_grupo$downloadRede, df_grupo$cpuPorcentagemUso)) +
  geom_point() + 
  geom_smooth(method = "lm") +

retas <- ggplot(mapping = aes(df_grupo$cpuPorcentagemUso, df_grupo$statusCpu)) +
  geom_point() +
  geom_smooth(se = FALSE, method = "lm") +
  geom_hline(yintercept = mean(df_grupo$cpuPorcentagemUso))


x <- df_grupo$dtRegistro
y <- df_grupo$cpuPorcentagemUso
plot(df_grupo$dtRegistro, df_grupo$cpuPorcentagemUso)
abline(lm(y ~ x), col = "red", lwd = 2)

summary(lm(y ~ x))

plot(df_grupo$cpuPorcentagemUso ~ df_grupo$cpuTemperatura)


