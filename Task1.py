'''
Некоторый алгоритм из одной цепочки символов получает новую цепочку следующим образом. Если последняя буква в цепочке — гласная,
то эта буква дописывается в начало цепочки, а если буква — согласная, то в конец цепочки. После чего последовательность символов в цепочке переворачивается в обратном порядке.
Дана цепочка символов “…” в файле word.txt. Какая цепочка символов получится, если к данной цепочке применить описанный алгоритм трижды?
'''

def chain(file):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    try:
        f = open(file, 'r+')
        content = f.read()
        if (content[-1] in vowels):
            content = content[1] + content
        else:
            content = content + content[-1]

        f.seek(0)
        f.write(content[::-1])
        f.truncate()
        f.close()
        
        return content[::-1]
    
    except IOError: # файл не существует
        return 'File not found'
    
 
print(chain("word.txt"))