import sys

#enter your map structure using '*' in order to ouput it in your desired word.
bitmap = """ 
    ****************
        ************************
    ****************
        ************************
  """
print('Enter the message to display with the bitmap.')
message = input('>  ')
if message == '':
    sys.exit()


    # loop over each line in the bitmap:


for line in bitmap.splitlines():
    # loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            print('', end='')
        else:
            print(message[i % len(message)], end='')
    print()
