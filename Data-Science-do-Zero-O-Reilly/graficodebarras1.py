from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

#i+0.1 for i está adicionando um pequeno deslocamento em x para melhorar a visualização das barras
xs= [i+0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars, 0.5, color ='pink') # define o que fica em cada eixo e estiliza s barras
plt.xlabel("Movies")
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")
plt.xticks([i+0.1 for i, _ in enumerate(movies)], movies)
plt.show()  