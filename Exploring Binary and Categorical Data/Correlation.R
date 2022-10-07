df = read.csv(file.choose(), header = T)
df
plot(df$T, df$VZ, xlab="T", ylab="VZ")
