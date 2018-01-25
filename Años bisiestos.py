# coding: utf-8
def esbisiesto(a):
	if (a % 4 == 0 and a % 100 !=0 or a % 400 == 0):
		print "Si es bisiesto"

	else:
		print "No es bisiesto"

esbisiesto(2100)
esbisiesto(2300)
esbisiesto(1955)

