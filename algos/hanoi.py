def move_disk(from_p, to_p):
	print('Moving disk from {} to {}'.format(from_p, to_p))

def move_tower(height, from_p, to_p, with_p):
	if height > 0:
		move_tower(height-1, from_p, with_p, to_p)
		move_disk(from_p, to_p)
		move_tower(height-1, with_p, to_p, from_p)


move_tower(3, 'A', 'B', 'C')