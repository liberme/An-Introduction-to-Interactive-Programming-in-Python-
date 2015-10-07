def Some(n):
    number = range(2, n)
    results = []
    while len(number) > 0:
        results.append(number[0])
        target = number[0]
        for i in number:
            if i % target == 0:
                number.remove(i)     
    return len(results)

print Some(100)
print Some(1000)