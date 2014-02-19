#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:  #kludge because import confuses me
    from argumentclinic.regexdict import RegExDict
except ImportError:
    from regexdict import RegExDict
from itertools import cycle

responses = RegExDict()
responses[r"\byou\b"] = cycle(["No I didn't.", "Did not.", "Didn't."])
responses[r"\bdid not\b"] = responses[r"\bdidn't\b"] = cycle(["Yes you did.", "You did.", "You did.", "You did.", "Oh you did!"])
responses[r"\bdid\b"] = cycle(["No you didn't.", "You didn't.", "You didn't!", "You did not!"])
responses[r"\bis not\b"] = responses[r"\bisn't\b"] = cycle(["Yes it is.", "It is!", "It can be.", ])
responses[r"\bis\b"] = cycle([r"No it isn't.", "No it isn't", "It is not.", "Isn't."])
fallback = cycle(["I told you once.", "Nonsense.", "Look, if I argue with you, I must take up a contrary position."])

def argue(statement):
    """
    Provides an argument.
    
    >>> argue("You did.")
    "No I didn't."
    >>> argue("You did.")
    'Did not.'
    >>> argue("Yes, you did.")
    "Didn't."
    """
    try:
        response = responses[statement]
    except KeyError:
        response = fallback
    return next(response)
       
import doctest
doctest.testmod()