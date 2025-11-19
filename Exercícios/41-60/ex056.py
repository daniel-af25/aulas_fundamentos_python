nums = list()
for c in range(0,5):
    num = int(input(f"Insira o {c+1}º número: "))
    nums.append(num)
maior = nums[0]
menor = nums [0]
indmaior = 0
indmenor = 0
for c in range(1,len(nums)):
    if(nums[c] > maior):
        maior = nums[c]
        indmaior = c
    if(nums[c] < menor):
        menor = nums[c]
        indmenor = c
print()
print(f"Maior nunero: {maior}, indice da lista: {indmaior}.")
print(f"Menor nunero: {menor}, indice da lista: {indmenor}.")


'''
Podia se ter usado tambem o max(nums) e o min(nums) para calcular o maximo e o minimo e o nums.index(maior/menor) para descobrir o index dos maior e menor mais rapido.
'''