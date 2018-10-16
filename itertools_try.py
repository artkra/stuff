# chain
# from_iterable
# combinations
# combination_wtih_replacement
# compress
# count
# cycle
# dropwhile
# groupby
# ifilter 
# ifilterfalse
# imap
# islice 
# izip 
# izip_longest
# permutations
# product
# repeat
# starmap
# takewhile
# tee 
from itertools import *

print list(chain('ABC', 'DEF'))

print list(chain.from_iterable(['ABC', 'DEF']))

print list(combinations(range(4), 2))

print list(combinations_with_replacement(range(4), 2))

print list(compress(range(4), [0, 1, 0, 1]))

for x in count(2.5, 0.5):
	if x < 20:
		print x
	else:
		break

for i, x in enumerate(cycle('ABC')):
	if i < 20:
		print str(i) + '  ' + str(x)
	else:
		break

print list(dropwhile(lambda x: x <= 10, range(20)))

for u, g in groupby('AAAABBBBCCCCBBBBAAAASDDDDSSSSSSHHHHH'):
	print u
	print list(g)

print list(ifilter(lambda x: x%2, range(10)))
print list(ifilterfalse(lambda x: x%2, range(10)))
print list(imap(pow, (2,3,10), (5,2,3)))
print list(islice('ABCD', 2 , 4))
print list(izip('ABCD', 'xy'))
print list(izip_longest('ABCD', 'xy', fillvalue='-'))
print list(permutations('ABCD', 2))
print list(product('ABCD', 'xy'))
print list(repeat('ABCD', 2))
print list(starmap(pow, [(2,5), (3,2), (10,3)]))
print list(takewhile(lambda x: x <= 10, range(20)))
for i in tee('ABCD', 4):
	print list(i)

