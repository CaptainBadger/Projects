#String Reversal
#Code reverses an input string
def reverse(string):
	new_string = string
	reverse_string = ""
	while len(new_string) != 0:
		letter = new_string[:1]
		new_string = new_string[1:]
		reverse_string = reverse_string + letter
	print reverse_string
		
