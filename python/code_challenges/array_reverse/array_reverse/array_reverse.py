test_list = [1,2,3,4,5]

def reverse_list(list):
  half_leng = len(list)//2

  for num in range(half_leng):
    temp = list[num]
    list[num] = list[len(list) - 1 - num]
    list[len(list) - 1 - num] = temp
  return list

print(reverse_list(test_list))
