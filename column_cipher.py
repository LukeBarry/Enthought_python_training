'''In this exercise you will encode the message This message is very secret with a column cipher with rows of length 3.
It is similar in spirit to the Caesar cipher exercise but of higher difficulty so allow some time or keep it for a second pass.'''

message = "This message is very secret"
def encode_message(message, rows):
    message = message.upper()
    message = message.replace(' ', '')
    remainder = len(message)%rows
    padded_message = message + (remainder * 'X')
    columns = [padded_message[i::rows] for i in range(rows)]
    encoded_message = ''.join(columns)
    return encoded_message

print encode_message(message, 3)
