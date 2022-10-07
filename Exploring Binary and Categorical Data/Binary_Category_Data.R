df = read.csv(file.choose(), header = T)
df
barplot(as.matrix(df)/6, cex.axis=.5)

