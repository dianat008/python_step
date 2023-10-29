my_data = int(input())
moghayes = 0
for i in range(1,my_data-1) :
    if my_data%i == 0 :
        moghayes += i
    else:
        continue
    
if moghayes == my_data :
    print("YES")
else:
    print("NO")