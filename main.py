import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"


#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

def caesar(text,shift,direction):
  if direction=="encode":
    enc=[]
    for letter in text:
      if shift > 26:
        shift=shift%26
      if letter not in alphabet:
        enc.append(letter)
      elif alphabet.index(letter)+shift>len(alphabet)-1:
        k=(alphabet.index(letter)+shift)-len(alphabet)
        enc.append(alphabet[k])
      else:
        k=alphabet.index(letter)+shift
        enc.append(alphabet[k])
    print("The encoded text is")
    print("".join(enc))
  
  elif direction=="decode":
    decr=[]
    for letter in text:
      if shift > 26:
        shift=shift%26
      if letter not in alphabet:
        decr.append(letter)
      elif alphabet.index(letter)-shift<0:
        position=len(alphabet)+(alphabet.index(letter)-shift)
        decr.append(alphabet[position])
      else:
        position=alphabet.index(letter)-shift
        decr.append(alphabet[position])
    print("The decoded text is :")
    print("".join(decr))
  else:
    print("Wrong Operation Try Again")
caesar(text,shift,direction)
while(1):
  data=input("Do you want to restart the cipher program?.Type 'Yes' if you want to go again or else type 'No'\n").lower()
  if data=="yes":
    direction1=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text1=input("Type your message:\n").lower()
    shift1=int(input("Type the shift number\n"))
    caesar(text1,shift1,direction1)
  else:
    print("Cipher Operation Ended")
    break
