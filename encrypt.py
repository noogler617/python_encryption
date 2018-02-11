# python_encryption
code soe that you can encrypt a string (input). Also take the string and decrypt the string.





def encrypt(text,shift):
  '''
  INPUT: text as a string and an integer for the shift value.
  OUTPUT: The shifted text after being run through the Caeser cipher.
  '''
  
  
  decrypted_text = list(range(len(text)))
  alphabet = string.ascii_lowercase
  
  first_half = alphabet[:shift]
  second_half = alphabet[shift:]
  
  shifted_alphabet = second_half+first_half
  
  for i,letter in enumerate(text.lower()):
    if letter in alphabet:
      
      index = shifted_alphabet.index(letter)
      original_index = alphabet[index]
      decrypted_text[i] = original_letter
      
    
    else:
      decrypted_text[i] = letter
  
  
  return ''.join(encrypted_text)
