def list_to_string(s): 
    password = "" 
    for element in s: 
        password += element 
    return password
def select_special_character(special_characters_needed):
    special_characters = ['!','@','#','$','%','^','&','*',
    '(',')','_','?','<','>','~','[',']','/','+','=','-']
    result = []
    result = random.sample(special_characters,special_characters_needed)
    return result
def select_digits(digits_needed):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    result = []
    result = random.sample(digits,digits_needed)
    return result
def select_alphabet(alphabets_needed):
    alphabet_letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    result = []
    result = random.sample(alphabet_letters,alphabets_needed)
    return result


import random
acceptance=0
liked=0
password_list = []
special_characters_selected = []
alphabets_selected = []
digits_selected = []
password_length = int(input("Enter the password length: "))
special_characters_needed = int(input("no. of Special characters: "))
digits_needed = int(input("no. of Digits: "))
alphabets_needed = password_length - (special_characters_needed+digits_needed)
while liked==0:
    special_characters_selected = select_special_character(special_characters_needed)
    digits_selected = select_digits(digits_needed)
    alphabets_selected = select_alphabet(alphabets_needed)
    password_set = special_characters_selected+alphabets_selected+digits_selected
    print(f"The list of randomly generated characters is {password_set}")
    liked = int(input("""
0 -> Generate another set of characters.
1 -> Go to the next step.

"""))
while acceptance==0:
    random.shuffle(password_set)
    password = list_to_string(password_set)
    print(password)
    acceptance = int(input("""
0 -> To shuffle again.
1 -> Liked this password.

"""))
print(f"The password generated as per your choice is: {password}")
    