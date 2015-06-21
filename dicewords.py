#!/usr/bin/python

'''
Script to generate passphrases according to the vocabular in:
http://world.std.com/~reinhold/diceware.wordlist.asc

To see why this might be a better algorithm for choosing a password:
https://blog.agilebits.com/2011/06/21/toward-better-master-passwords/

And see how long your passwords need to be:
https://blog.agilebits.com/2013/04/16/1password-hashcat-strong-master-passwords/

Two dictionaries are supported.  English (vocab size 7776) or multi language  (vocab size 537566)
'''

import re
import random
import argparse

expr = re.compile(r'^([1-6]{5})\W(.+)')


LANGUAGE_DICTS = [
  'words/Afrikaans-dice.txt',
  'words/Croatian-dice.txt',
  'words/Czech-dice.txt',
  'words/English-dice.txt',
  'words/Finnish-dice.txt',
  'words/French-dice.txt',
  'words/Hungarian-dice.txt',
  'words/Italian-dice.txt',
  'words/Japanese-dice.txt',
  'words/Latin-dice.txt',
  'words/Norwegian-dice.txt',
  'words/Polish-dice.txt',
  'words/Spanish-dice.txt',
  'words/Swahili-dice.txt',
  'words/Swedish-dice.txt',
  'words/Turkish-dice.txt',
]

def get_vocab(filename):
  with open(filename) as fh:
    matches = [expr.match(line) for line in fh.readlines()]
    vocab = [match.group(2) for match in matches if match]
    return vocab

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('words', type=int, help='number of words per phrase')
  parser.add_argument('phrases', type=int, help='number of phrases to generate')
  parser.add_argument('-m', '--multilang', help='use dictionaries of multiple languages', action='store_true')
  args = parser.parse_args()

  if args.multilang:
    vocab = list({ word for language in LANGUAGE_DICTS
                   for words in get_vocab(language)
                   for word in words.split(' ') })
  else:
    vocab = get_vocab('words/diceware-wordlist.txt')
    assert(len(vocab) == 6 ** 5)

  for _ in xrange(args.phrases):
    print ' '.join([random.choice(vocab) for _ in xrange(args.words)])
