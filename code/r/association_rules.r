library(arules)
library(arulesViz)
library(lubridate)

l_movies = topmovies

# Convert dates to days of the year.
l_movies[, 4] = lapply(l_movies[, 4], as.Date, format="%B %d")
l_movies[, 4] = lapply(l_movies[, 4], yday)

# Remove dollar signs and convert to numeric types.
l_movies[, 3] = lapply(l_movies[, 3], substring, 2)
l_movies[, 3] = lapply(l_movies[, 3], as.numeric)

# Discretize column values.
l_movies[, 1] = discretize(as.matrix(l_movies[, 1]), categories = 5)
l_movies[, 3] = discretize(as.matrix(l_movies[, 3]), categories = 5)
l_movies[, 4] = discretize(as.matrix(l_movies[, 4]), categories = 4)
l_movies[, 5] = discretize(as.matrix(l_movies[, 5]), categories = 5)

col_names = names(l_movies)
l_movies[, col_names] = lapply(l_movies[, col_names], factor)

# Run the APRIORI algorithm.
rules.all <- apriori(l_movies, parameter = list(minlen=2, supp=0.2, conf=0.3))
rules.sorted <- sort(rules.all, by = "lift")

# Plot stuff.
plot(rules.all, method="grouped")