# хм, он и "лепспел", и "лепсспел" считает палиндромом
def check_word(s):
    if s[::-1] == s:
        print('True')
    if s[::-1] != s:
        print('False')


check_word('лепсспел')
