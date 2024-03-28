key = {'.-': 'а',
       '-...': 'б',
       '.--':'в',
       '--.':'г',
       '-..':'д',
       '.':'е',
       '...-':'ж',
       '--..':'з',
       '..':'и',
       '.---':'й',
       '-.-':'к',
       '.-..':'л',
       '--':'м',
       '-.':'н',
       '---':'о',
       '.--.':'п',
       '.-.':'р',
       '...':'с',
       '-':'т',
       '..-':'у',
       '..-.':'ф',
       '....':'х',
       '-.-.':'ц',
       '---.':'ч',
       '----':'ш',
       '--.-':'щ',
       '--.--':'ъ',
       '-.--':'ы',
       '-..-':'ь',
       '..-..':'э',
       '..--':'ю',
       '.-.-':'я'}

file = open('out.txt', 'w')

def decode(code, plain):
       if code == '':
              file.write(plain + '\n')
       else:
              for i in reversed(range(min(6, len(code) + 1))):
                     if (code[:i] in key):
                            decode(code[i:], plain + key[code[:i]])


print('Введите зашифрованное сообщение: ')
code = input()
decode(code, '')

file.close()
