nums = list()
c = 0
num = int(input(f"Digite o 1º número: "))
nums.append(num)
while True:
    num = int(input(f"Digite o {c+2} número: "))
    if(num == 0):
        c -= 1
        break
    for f in range (0,len(nums)):
        if(num == nums[f]):
            continue
    c += 1
    nums.append(num)
nums.sort(reverse=True)
print(f"Foram inseridos {c} números, a ordem decrescente dos mesmos é {nums}")
