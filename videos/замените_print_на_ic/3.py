from icecream import ic

def func(value):
	ic.disable()
	if value == 1:
		ic()
	else:
		ic()

ic(1)
func(1)