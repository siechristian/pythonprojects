#global keyword
total = 0
def count():
	global total 
	total += 1
	return total
count()
count()
print(count())