#Importações necessárias
import matplotlib.pyplot

#Dados que colocaremos no grafico
meses2018 = ['jan', 'fev', 'mar']
dados2018 = [999, 5000, 500 ]
meses2019 = ['jan', 'fev', 'mar']
dados2019 = [1000, 11006, 0 ]
meses2020 = ['jan', 'fev', 'mar']
dados2020 = [500, 1500, 500 ]

#Plotando os dados no grafico
#Linha normal
matplotlib.pyplot.plot(meses2018, dados2018, color='red')
#k: Linha pontilhada
matplotlib.pyplot.plot(meses2019, dados2019,'k:', color='orange')
#k--: Linha tracejada
matplotlib.pyplot.plot(meses2020, dados2020,'k--', color='black')

#Lista que irá para a legenda
#Deve ser colocado na mesma ordem
anos = [2018, 2019, 2020]
#Criando a caixa de legenda externa(lista de nomes, titulo, localização)
matplotlib.pyplot.legend(anos, title="Anos", loc="center left")

#Definindo limites para a coluna y
#Ps: só valores positivos
matplotlib.pyplot.ylim(0, 12000)

#Titulo 
matplotlib.pyplot.title('Faturamento')

#Nome da x
matplotlib.pyplot.xlabel('Meses')
#Nome da y
matplotlib.pyplot.ylabel('Faturamento em R$')

matplotlib.pyplot.show()