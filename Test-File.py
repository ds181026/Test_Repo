import random
import string
import re

def random_spell_mistake(sentence, p = 0.1): #p is for the probability that the word gets misspelled
    letters = string.ascii_lowercase
    words = sentence.split()
    new_sent = []
    for w in words:
        wlist = list(w)
        if random.uniform(0,1) < p:
            wlist[random.randint(0,len(wlist)-1)] = letters[random.randint(0,len(letters)-1)]
        changed_word = ''.join(wlist)
        new_sent.append(changed_word)
        final_sent = ' '.join(new_sent)
    print(final_sent)

neighbours = {
    'q': ['a', 'w'],
    'w': ['q', 'a', 's', 'e'],
    'e': ['w', 's', 'd', 'r'],
    'r': ['e', 'd', 'f', 't'],
    't': ['r', 'f', 'g', 'z'],
    'z': ['t', 'g', 'h', 'u'],
    'u': ['z', 'h', 'j', 'i'],
    'i': ['u', 'j', 'k', 'o'],
    'o': ['i', 'k', 'l', 'p'],
    'p': ['o', 'l'],
    'a': ['q', 'w', 's', 'y'],
    's': ['w', 'e', 'd', 'x', 'y', 'a'],
    'd': ['e', 'r', 'f', 'c', 'x', 's'],
    'f': ['r', 't', 'g', 'v', 'c', 'd'],
    'g': ['t', 'z', 'h', 'b', 'v', 'f'],
    'h': ['z', 'u', 'j', 'n', 'b', 'g'],
    'j': ['u', 'i', 'k', 'm', 'n', 'h'],
    'k': ['i', 'o', 'l', 'm', 'j'],
    'l': ['o', 'p', 'k'],
    'y': ['a', 's', 'x'],
    'x': ['y', 's', 'd', 'c'],
    'c': ['x', 'd', 'f', 'v'],
    'v': ['c', 'f', 'g', 'b'],
    'b': ['v', 'g', 'h', 'n'],
    'n': ['b', 'h', 'j', 'm'],
    'm': ['n', 'j', 'k'],
    ' ': ['c', 'v', 'b', 'n', 'm']
    }

def realistic_spell_mistake(sentence, p = 0.1):
    letters = list(sentence)
    for l in enumerate(letters):
        idx = l[0]
        letter = l[1]
        if random.uniform(0,1) < p:
            if letter.isupper() == True:
                letter = letter.lower()
                neighbour_letters = neighbours[letter]
                letters[idx] = neighbour_letters[random.randint(0,len(neighbour_letters)-1)].upper()
            else:
                neighbour_letters = neighbours[letter]
                letters[idx] = neighbour_letters[random.randint(0,len(neighbour_letters)-1)]
        final_sent = ''.join(letters)
    print(final_sent)

def change_word_order(text):
    sents = text.split('. ')
    new_sent_list = []
    for sent in sents:
        sent_list = sent.split()
        sent_list[-1] = sent_list[-1].strip('.')
        random.shuffle(sent_list)
        sent_list[-1] += '.'
        new_sent = ' '.join(sent_list)
        new_sent_list.append(new_sent)
    final_text = ' '.join(new_sent_list)
    print(final_text)






test_text = 'This is now a text with a few sentences. I am extremely curious to find out what my function does.'
change_word_order(test_text)
#Problem: It is hard to determine whether the first word of a sentence should stay capitalized or not when it's not at the beginning of the sentence anymore
#It is also difficult to say what would be the best thing to do with hyphens or commas
random_spell_mistake(str(input('Type words: ')), p = 0.02)
realistic_spell_mistake(str(input('Type words: ')), p = 0.02)



def ocr_mistake(text):
    pass

#benjis functions
def remove_letter(text):
    pass

















number_text = '''
this are the pills i need
50mg of this
20g of that
30 ml of this
I am 20 years old and i weigh 62 kilogram
'''






def calculate_grams(expression):
    match = re.match(r'(([0-9])+)\s?([a-zA-Z]+)', expression)
    number = float(match.group(1))
    unit = match.group(3)
    kilos = ['kilogram', 'kg']
    milis = ['miligram', 'mg']
    if unit.lower() in kilos:
        weight = 1000*number
    elif unit.lower() in milis:
        weight = 0.001*number
    else:
        weight = number
    final_value = str(weight) + 'g'
    return final_value

gram_text = '501 mg' 
print(calculate_grams(gram_text))

def change_units(text):
    gram_re = r'[0-9]+\s?(g|gram|mg|miligram|kg|kilogram)'
    liter_re = r'[0-9]+\s?(l|liter|ml|mililiter|dl|deciliter|cl|centiliter)'
    new_text = re.sub(gram_re, calculate_grams(gram_re), text)
    return(new_text)
        
change_units(number_text)

#https://linuxhint.com/python_string_replacement/