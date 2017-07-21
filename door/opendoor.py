from changeDoorState import change_state

door_state = False #door is closed
# True => door is opened
# False => door is closed


while True: 
	if door_state == True:
		print("Door state: Opened")
	else:
		print("Door state: Closed")

	command = input().split()
	print(command)	
	#if len(command) == 0:
		#break
	#door_state = change_state(door_state, command)
	
	




#from stemmers import porter2


'''
door_state = 0  # door is closed


command = input().split()
stem_cmd = [porter2.stem(i) for i in command]
#command = command.split()
open_key = ['open','door']


count = 0
for w in open_key:
	if w in stem_cmd:
		count = count + 1		
if count == len(open_key):
	door_state = 1

if door_state == 1:
	print("Door Opened")


# door state is 1 now, which means it is open. It needs to be closed.
close_key = ['close','door']
command = input().split()
stem_cmd = [porter2.stem(i) for i in command]
count = 0
for w in close_key:
	if w in command:
		count = count + 1		
if count == len(close_key):
	door_state = 0 

if door_state == 0:
	print("Door Closed")
'''
'''
for w in close_key:
	if w in command:
		door_state = 0
if door_state == 0:
	print("Door closed")
'''


'''
Eg cases:
open door
open the door
please open the door
can you please open the door
i want you to open the door right now
'''



'''
if command == open_key:
	door_state = 1
	print("Door Opened.")
'''


