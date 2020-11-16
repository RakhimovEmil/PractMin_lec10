def binary_s(value, d):
	l = 0
	r = len(d) - 1
	while l <= r:
		m = (l + r) / 2
		if value < d[m]:
			r = m - 1
		elif value > d[m]:
			l = m + 1
		else:
			return m
	return -1
