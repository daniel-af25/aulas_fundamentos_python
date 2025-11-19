nums = list()
for c in range(0,5):
    num = int(input(f"Insira o {c+1}/5 número: "))
    if (c == 0):
        nums.append(num)
    if (num < nums[-1]):
        nums.insert(0, num)
    else:
        nums.append(num)
nums.pop(0)
print (nums)


