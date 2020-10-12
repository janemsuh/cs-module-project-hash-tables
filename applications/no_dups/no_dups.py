def no_dups(s):
    if len(s) < 1:
        return ''
    
    dictionary = dict()

    words = s.split(' ')

    output = words[0]
    dictionary[output] = True

    for word in words[1:]:
        if dictionary.get(word):
            continue
        else:
            output += ' ' + word
            dictionary[word] = True
    
    return output


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))