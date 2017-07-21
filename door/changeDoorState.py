from stemmers import porter2


def change_state(door_state, text):
	
	if isValid(text) == False:
		return

	open_key = ['open','door']
	close_key = ['close','door']
	
	
	stem_cmd = [porter2.stem(i) for i in text]

	
	if door_state == False:
		key = open_key
	elif door_state == True:
		key = close_key
	
	for w in key:
		if w not in stem_cmd:
			print("invalid command")
			return
	
	
	door_state = not door_state	

	
	if door_state == True:
		print("Door Opened")
	else:
		print("Door Closed")
	
	return door_state
 	
	


# Checks whether the natural language input is valid or not.
def isValid(text):
	stemmed = [porter2.stem(i) for i in text]

	if (len(text) == 1) or ('open' in stemmed and 'close' in stemmed):
		print("Invalid command.")
		return False

	return True
