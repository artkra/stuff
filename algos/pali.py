from string import ascii_letters

def pali(s):
	s = ''.join([x.upper() for x in s if x in ascii_letters])
 	for i, ch in enumerate(s):
 	if s[i] == s[len(s)-1 - i]:
    	pass
  	else:
    	return False
	return True
