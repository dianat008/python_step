# In the name of God

def sum_of_even_numbers(n):
    return sum([x for x in range(1, n+1) if x % 2 == 0])

n = int(input())
print(sum_of_even_numbers(n))