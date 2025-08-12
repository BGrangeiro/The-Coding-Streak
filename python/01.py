"""
Write a Python program that generates or receives a text, converts it to lowercase, iterates through each letter using .count() to count how many times 
each has appeared so far, and displays the result in the console. At the end, show which letter appeared the most, ignoring spaces, punctuation, and 
case differences.
"""
import lorem

#texto = lorem.sentence().lower() #gera uma frase toda em minuscula
texto = 'bananabaxa'
i = 0
maior_letra = 0
while i < len(texto):

    indicie = texto[i] # Pega letra por letra do TEXTO
    letra_por_letra = texto[:i+1] # Junta as letras uma por uma para ir analisando quando uma letra nova aparece
    contagem = letra_por_letra.count(indicie) # Conta quanto de cada letra tem
    i+=1

    if contagem > maior_letra:  # Verifica qual a letra que mais apareceu
        maior_letra = contagem

    print(indicie,contagem)

print(maior_letra)


