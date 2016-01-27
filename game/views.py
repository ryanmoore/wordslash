from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import itertools
import re

def old_game(request, num_hands, seed):
    hands = gen_triplets_from_seed(seed, int(num_hands))
    text = ''
    for hand in hands:
        text += '{}<br>'.format(''.join(hand))
    return HttpResponse('Hands in play:<br>{}'.format(text))

def game(request, num_hands, seed):
    hands = gen_triplets_from_seed(seed, int(num_hands))
    context = {'hands' : hands}
    return render(request, 'game/play.html', context)

def answer(request, num_hands, seed):
    hands = gen_triplets_from_seed(seed, int(num_hands))
    text = ''
    for hand in hands:
        text += '{}: {}<br>'.format(''.join(hand), find_shortest_words(hand, 10))
    return HttpResponse('{}'.format(text))

def gen_triplets_from_seed(seed, count):
    random.seed(seed)
    selected = random.sample(weighted_letter_set(), count*3)
    return list(grouper(selected, 3))

def weighted_letter_set():
    choices = string.ascii_uppercase
    singles = 'JKQVWXYZ'
    choices += ''.join(set(string.ascii_uppercase) - set(singles))
    return choices

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

def find_shortest_words(hand, limit):
    pattern = r'\b\w*{}\w*{}\w*{}\w*\s*$'.format(*''.join(hand).lower())
    with open('/usr/share/dict/words', 'r') as infile:
        matches = re.findall(pattern, infile.read(), flags=re.MULTILINE)
    matches = [elt for elt in matches if len(elt) > 3 and elt.islower()]
    matches.sort(key=lambda x: len(x))
    return list(itertools.islice(matches, 0, limit))
