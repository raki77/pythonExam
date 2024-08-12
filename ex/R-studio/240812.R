
# install.packages("prob")

version
# R 버젼 4.4.1


install.packages("devtools")
library(devtools)
remotes::install_github("cran/fOptions")
remotes::install_github("cran/fAsianOptions")
remotes::install_github("cran/prob")

install.packages("BiocManager")
BiocManager::install("fasianOptions")


install.packages("prob")
prob::tosscoin(1)

library(prob)
tosscoin(2)

rolldie(1)
rolldie(2)

# 반복
rep("Red", 7)
rep("Blue", 5)

# combine
?c

beads <- c(rep("Red", 7), rep("Blue", 5))

# sample(x, size, replace = FALSE, prob = NULL)
?sample

sample(beads, 1, replace = TRUE)

(5/12) * (5/12)


