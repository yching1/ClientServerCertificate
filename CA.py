MAX_KEY_SIZE = 26

def getKey(pubkey): #assign public key
    if pubkey == 'im a cert':
        key = 11
    return key

def getTranslatedMessage(mode, message, key):
    if mode == "d":
       key = -key
    translated = ""

    for symbol in message:
       if symbol.isalpha():
          num = ord(symbol)
          num += key
          
          if symbol.isupper():
             if num > ord('Z'):
                num -= 26
             elif num < ord('A'):
                num += 26
          elif symbol.islower():
             if num > ord('z'):
                num -= 26
             elif num < ord('a'):
                num += 26

          translated += chr(num)
       else:
          translated += symbol
    return translated