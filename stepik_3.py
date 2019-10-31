def even_indeces(l):
    ans = []
    for i, num in enumerate(l):
        if i % 2 == 0:
            ans.append(num)
    return ans

print(even_indeces([1, 1, 2, 3, 5, 8, 13, 21, 34]))