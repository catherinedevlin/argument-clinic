#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:  #kludge because import confuses me
    from argumentclinic.regexdict import RegExDict
except ImportError:
    from regexdict import RegExDict
from itertools import cycle

responses = RegExDict()
responses[r"\byou\b"] = cycle(["No I didn't.", "Did not.", "Didn't."])
responses[r"\bdid not\b"] = responses[r"\bdidn't\b"] = cycle(
    ["Yes you did.", "You did.", "You did.", "You did.", "Oh you did!"])
responses[r"\bdid\b"] = cycle(
    ["No you didn't.", "You didn't.", "You didn't!", "You did not!"])
responses[r"\bis not\b"] = responses[r"\bisn't\b"] = cycle(
    ["Yes it is.", "It is!", "It can be.", ])
responses[r"\bit's\b"] = responses[r"\bis\b"] = cycle(
    [r"No it isn't.", "It is not.", "Isn't.", "It most certainly is not."])
fallback = cycle(["I told you once.", "Nonsense.", 
     "Look, if I argue with you, I must take up a contrary position."])

def argue(statement):
    """
    Provides an argument.

    >>> argue("Oh look, this isn't an argument.")
    'Yes it is.'
    >>> argue("It's just contradiction.")
    "No it isn't."
    >>> argue("It is!")
    'It is not.'
    """
    try:
        response = responses[statement]
    except KeyError:
        response = fallback
    return next(response)

if __name__ == '__main__':       
    import doctest
    doctest.testmod()
