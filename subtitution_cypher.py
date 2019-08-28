def subtitution_encryption(key:int, message:str) -> str:
    """
    Encrypts a message using the subtitution cypher encryption. Spaces are omitted just to make it a little harder to crack the message.
    """
    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    
    enumerate_alphabet_letter_number = dict([(j,i) for i,j in enumerate(alphabet)])
    
    format_message = ''.join(message.split(' ')).lower()
    message_to_numbers = [enumerate_alphabet_letter_number[i] for i in format_message]
    
    multiply_key_with_message = [key * i for i in message_to_numbers]
    encrypt_message = [i%26 for i in multiply_key_with_message]
    enumerate_alphabet_number_letter = dict([(i,j) for i,j in enumerate(alphabet)])
    encrypt_message_to_letters = ''.join([enumerate_alphabet_number_letter[i] for i in encrypt_message])

    return encrypt_message_to_letters