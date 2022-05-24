from tkinter import Tk,Button,Text,Entry,END,BOTH,X
MORSE_CODE_DICT = { 'A':'hH', 'B':'Hhhh',
					'C':'HhHh', 'D':'Hhh', 'E':'h',
					'F':'hhHh', 'G':'HHh', 'H':'hhhh',
					'I':'hh', 'J':'hHHH', 'K':'HhH',
					'L':'hHhh', 'M':'HH', 'N':'Hh',
					'O':'HHH', 'P':'hHHh', 'Q':'HHhH',
					'R':'hHh', 'S':'hhh', 'T':'H',
					'U':'hhH', 'V':'hhhH', 'W':'hHH',
					'X':'HhhH', 'Y':'HhHH', 'Z':'HHhh',
					'1':'hHHHH', '2':'hhHHH', '3':'hhhHH',
					'4':'hhhhH', '5':'hhhhh', '6':'Hhhhh',
					'7':'HHhhh', '8':'HHHhh', '9':'HHHHh',
					'0':'HHHHH', ',':'HHhhHH', '.':'hHhHhH',
					'?':'hhHHhh', '/':'HhhHh', '-':'HhhhhH',
					'(':'HhHHh', ')':'HhHHhH'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			# Looks up the dictionary and adds the
			# corresponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += ' '

	return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):

	# extra space added at the end to access the
	# last morse code
	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter

		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher

def digest(string):
    for l in string:
        if l not in MORSE_CODE_DICT:string=string.replace(l,'-')
    return string

def encr():
        outbox.delete("1.0", "end")
        outbox.insert(END,encrypt(digest(inbox.get().upper())))

def decr():
        outbox.delete("1.0", "end")
        outbox.insert(END,decrypt(inbox.get()))

root=Tk()
root.geometry("300x200")
root.title('H')
inbox=Entry(root)
inbox.pack(fill=X)
b1=Button(root,text='Encrypt',command=encr)
b1.pack()
b2=Button(root,text='Decrypt',command=decr)
b2.pack()
outbox=Text(root)
outbox.pack(fill=BOTH,expand=True)
root.mainloop()
