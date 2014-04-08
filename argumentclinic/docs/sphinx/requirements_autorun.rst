Software Requirements (``autorun``)
===================================

(Discovered with Sphinx's ``autorun`` extension)

Python packages
---------------

.. runblock:: pycon

    >>> import sys
    >>> sys.path.insert(0, '.')
    >>> from get_reqs import requirements_met
    >>> print("\n".join(requirements_met()))

PostgreSQL
----------


Your system should run PostgreSQL 9.1 or better.

.. runblock:: console

   $ psql --version


