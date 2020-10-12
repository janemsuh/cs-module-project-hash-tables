import re

def word_count(s):
    output = {}
    words = s.split()

    if words == ['']:
        return {}
    
    for word in words:
        word = re.sub(r"[\"\&\.\:\;\,\-\+\=\/\\\[\]\{\}\(\)\*\^\&\|\s]", '', word.lower())
        if word == '':
            continue
        else:
            if word in output:
                output[word] += 1
            else:
                output[word] = 1
    return output



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))