# Morse code translator

# Dictionary representing the morse code chart
MORSE_DICT = {
   'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

def get_key(val):
    for key,value in MORSE_DICT.items():
        if val == value:
            return key
    
    return "key doesnt exist"

l3 = []
query = input("Enter morse code separating letters by spaces and words by double spaces. \n")
l1 = query.split('  ')
for x in l1:
    l2 = x.split(' ')
    for y in l2:       
        l3.append(get_key(y))
        print(get_key(y))
    l3.append(' ')

print(*l3)


