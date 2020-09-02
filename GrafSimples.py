#Importações necessárias
import matplotlib.pyplot

#Dados que colocaremos no grafico
meses2018 = ['jan', 'fev', 'mar']
dados2018 = [999, 5000, 500 ]

#Plotando os dados no grafico
matplotlib.pyplot.plot(meses2018, dados2018, color='red')

#Apresentando o gráfico
matplotlib.pyplot.show()