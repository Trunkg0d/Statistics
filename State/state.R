df <- read.csv(file.choose())
df
mean(df[["Population"]])
mean(df[["Population"]], trim=0.1)
weighted.mean(df[["Murder.rate"]], w=df[["Population"]])

install.packages("matrixStats")
library("matrixStats")

weightedMedian(df[["Murder.rate"]], w=df[["Population"]])
sd(df[["Population"]])
IQR(df[["Population"]])
mad(df[["Population"]])
boxplot(df[["Population"]]/1000000, ylab="Population (millions)")

breaks <- seq(from=min(df[["Population"]]),
              to=max(df[["Population"]]), length=11)
pop_freq <- cut(df[["Population"]], breaks=breaks,
                right=TRUE, include.lowest = TRUE)
table(pop_freq)
hist(df[["Population"]], breaks=breaks)
hist(df[["Murder.rate"]], freq=FALSE)
lines(density(df[["Murder.rate"]]), lwd=3, col="blue")
