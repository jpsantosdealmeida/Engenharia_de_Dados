from collections import Counter

c = Counter()


l1 = [1,1,2,3,3,5]
l2 = [1,1,2,6,2,5]

print(f'Contador {c}')
c.update(l1)
print(f'Contador depois do update {c}')
print(f'Contador total {c.total()}')
print(f'Contador transformando em lista e len {len(list(c))}')
