Usage (with ``doctest``)
========================

.. doctest::

    >>> from argumentclinic.argumentclinic import argue
    >>> argue("This is my favorite package!")
    "No it isn't."
    >>> argue("It is!")
    'It is not.'
    >>> argue("Is!")
    "Isn't."
    >>> argue("This isn't even a proper argument.")
    "I guess you're right."
    
