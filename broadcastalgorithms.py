from collections import defaultdict
def one_to_all(d, my_id, X):
	mask = 2**d - 1
	print "mask initial", mask
	for k,i in enumerate(range(0,d)[::-1]): 
		print "time ",k+1
		mask = mask ^ 2**i
		#print "mask ", mask
		#print "myid and mask", my_id & mask
		if my_id & mask == 0: 
			if my_id & 2**i == 0:
				msg_destination = my_id ^ 2**i
				print "message destination", msg_destination
			else:
				msg_source = my_id ^ 2**i
				print "recieving from", msg_source

result = defaultdict(int)
my_msg = range(8)

def all_to_all_bc_hcude(my_id, my_msg, d, result):
	result = my_msg
	for i in range(0,d): 
		partner = my_id ^ 2**i
		print "send ",result, " to ", partner
		result = result + my_msg
		print result


def prefix_sum(my_id, my_number, d, result):
	result = my_number
	msg = result
	stored = defaultdict(int)
	recieved = defaultdict(int)
	for i in range(0,d): 
		partner = my_id ^ 2**i
		print "send msg",result, " to ", partner
		stored[i] = msg
		msg = msg + my_number
		if partner < my_id: 
			result += my_number
		print result
	print stored

def all_to_allmesh(my_id, my_msg, p, result ):
	left = my_id - (my_id % math.sqrt(p)) + ((my_id-1)% math.sqrt(p))
	right = my_id - (my_id % math.sqrt(p)) + ((my_id+1)% math.sqrt(p))
	result = set(my_msg)
	msg = result
	print "along rows"
	for i in range(1, int(math.sqrt(p))): 
		print "send from ",right, " recieved from ", left
		result = result.union(my_msg)
	up = (my_id - math.sqrt(p))%p
	down = (my_id + math.sqrt(p))%p
	print "along collumns"
	for i in range(1, int(math.sqrt(p))):
		print "send from ",down, " recieved from ", up
		result = result.union(my_msg)

def all_to_all_personal(d, my_id):
	for i in range(1,2**d): 
		partner = my_id^i; 
		print "send to ", my_id,partner," to ",partner
		print "recieve ",partner, my_id from partner


