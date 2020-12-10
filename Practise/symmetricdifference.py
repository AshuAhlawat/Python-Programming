q_a = int(input())
a = input()

l_a = a.split()

my_set_a = set(l_a)

q_b = int(input())
b = input()

l_b = b.split()

my_set_b = set(l_b)

res_set = my_set_a^my_set_b
print(res_set)
res_list = list(res_set)
res_list_int=list(map(int,res_list))

res_list_int.sort()

for i in res_list_int:
    print(i)