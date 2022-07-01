alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import day8.art as art
print(art.logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
        end_text += char
    else:        
        position = alphabet.index(char)
        new_position = position + shift_amount
        new_position %= 26
        end_text += alphabet[new_position]
   
    
  print(f"Here's the {cipher_direction}d result: {end_text}\n\n\n\n")



def question_with_caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


while True:
    question_with_caesar()
    
    loop = input("Do you want to play again? 'yes' for again and 'no' for leave\n").lower()

    if loop == "yes":
        pass
    elif loop == "no":
        break
        
print("Goodbye!")