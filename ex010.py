# Create a program that reads all money in a wallet, print that value and how much dollar can be bought. R$5.17 = US$1.00

reais = float(input('Enter amount reais you have: '))
print('You have R${:.2f} or US${:.2f}'.format(reais, (reais/5.17)))
