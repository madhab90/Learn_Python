alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(user_Text, shift_amount,direction):
  converted_Text = ""
  if direction == "decode":
    shift_amount *= -1
  for letter in user_Text:
    position = alphabet.index(letter)
    
   
    
    new_position = position + shift_amount
    converted_Text += alphabet[new_position]
  print (f"The {direction}d text is {converted_Text}.")






#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)