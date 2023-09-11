n = int(input())

if n == 3 or n == 1:
    print(-1)

else:
    count = n // 5
    if (n - (count * 5)) % 2:
        count -= 1 
    count += ((n - (count * 5))//2)
    print(count)
    