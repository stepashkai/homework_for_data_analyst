#anova
df <- data.frame(cbind(c(7,8,8,5,7,10,5,3,8,10), 
                 c("men","men","men","men","men",
                  "women","women","women","women","women")))
colnames(df) <- c("value","gender")
df
fit <- aov(value ~ gender, df)
summary(fit)

#Mann-Whitney test
men <- c(7, 8, 8, 5, 7)
women <- c(10, 5, 3, 8, 10)
wilcox.test(men, women, exact = F)
?wilcox.test
