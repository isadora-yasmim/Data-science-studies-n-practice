from matplotlib import pyplot as plt

variance=[1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x+y for x,y in zip(variance,bias_squared)]
xs = [i for i,_ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance')#linha verde contínua
plt.plot(xs, bias_squared, 'r-.', label='bias^2')#linha vermelha tracejada-pontilhada
plt.plot(xs, total_error, 'b:', label='total error')#linha azul pontilhada

plt.legend(loc=9)#significa que ficará na parte superior central do gráfico
plt.ylabel("error")
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()