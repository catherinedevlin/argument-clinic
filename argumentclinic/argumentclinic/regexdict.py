import doctest
from collections import OrderedDict

"""
A dictionary whose keys are regular expression patterns

Adapted from https://djangosnippets.org/snippets/309/
"""
import re

class RegExDict(OrderedDict):
    """A dictionary-like object for use with regular expression keys.
    Setting a key will map all strings matching a certain regex to the
    set value.
   
    >>> d = RegExDict()
    >>> d[r'moo.*haha'] = 7
    >>> d[r'holler.*fool'] = 2
    >>> d['mooWORDhaha']
    7
    >>> d2 = RegExDict({r'\w*A\w*': 1, r'\w*B\w*': 2})
    >>> d2['cat']
    1
    >>> ordered = RegExDict({r'cats$': 1})
    >>> ordered[r's$'] = 2
    >>> ordered['how many cats']
    1
    >>> ordered = RegExDict({r's$': 1})
    >>> ordered[r'cats$'] = 2
    >>> ordered['how many cats']
    1
    >>> import re
    >>> ordered[re.compile(r's$')]
    1
    """

    """
    def __init__(self, dct={}):
        super(RegExDict, self).__init__(dct)        
        for (k, v) in dct.items():
            self[k] = v
    """
        
    def __getitem__(self, name):
        if hasattr(name, 'lower'):
            for regex in self.keys():
                m = regex.search(name)
                if m is not None:
                    return super(OrderedDict, self).__getitem__(regex)
            raise KeyError('Key does not match any regex')
        if hasattr(name, 'pattern'):
            for regex in self.keys():
                if regex.pattern == name.pattern:
                    return super(OrderedDict, self).__getitem__(regex)
            raise KeyError('Key does not match any regex')
        else:
            return super(OrderedDict, self).__getitem__(name)
            
    def __setitem__(self, key, value):
        if not hasattr(key, 'pattern'):  # is not already a regex
            key = re.compile(key, re.IGNORECASE)
        super(RegExDict, self).__setitem__(key, value)
        
if __name__ == '__main__':
    doctest.testmod()
