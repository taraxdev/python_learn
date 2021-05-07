def even_or_odd(num):
    if num%2==0:
        return f"the {num} is even"
    else:
        return f"the {num} is odd"

# print(even_or_odd(24))

nums = [1,2,3,4,55,23,6,23,78,234,768,234,43,657]

a = list(map(even_or_odd,nums))

print(a)
