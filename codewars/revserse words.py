def reverse_words(text):
    str1 = ''
    for i in text.split(' '):
        i = i[::-1] + ' '

        str1 += i
    return str1.rstrip()


#or



def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))