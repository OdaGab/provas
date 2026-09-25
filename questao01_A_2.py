a = 15
b = 4
c = 2

res_1 = a // b + c ** b % a
res_2 = not (a % c == 0) and (b * c > a or a - b != 11)
     #   not (false)  and  false or false
     #     True and False
     #       False

print(res_2)
