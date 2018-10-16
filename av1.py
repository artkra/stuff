def not_(value): return not value
result = not_(0), all(any([not_(x) for x in range(b)]) for b in range(10))
print(result)