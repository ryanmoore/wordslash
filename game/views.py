from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import itertools

def game(request, num_hands, seed):
    hands = list(gen_triplets_from_seed(seed, int(num_hands)))
    return HttpResponse('Hands in play: {}'.format(hands))

def gen_triplets_from_seed(seed, count):
    random.seed(seed)
    selected = random.sample(weighted_letter_set(), count*3)
    return grouper(selected, 3)

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
