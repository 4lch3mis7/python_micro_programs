import string
import random


def generate(num_lowers=4, num_uppers=4, num_digits=3, num_punctuations=3):
    
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    punctuations = string.punctuation

    password = []
    password.extend(random.sample(lowers, num_lowers))
    password.extend(random.sample(uppers, num_uppers))
    password.extend(random.sample(digits, num_digits))
    password.extend(random.sample(punctuations, num_punctuations))

    random.shuffle(password)
    password = ''.join(password)

    return password


if __name__=='__main__':
    print('Testing password generator')
    print(generate())