Contributing to Everest
=======================

Topics
------

* `Coding Style`_
* `Quick Contribution Tips and Guidelines`_
* `Design and Cleanup Proposals`_
* `Reporting Issues`_

.. _reporting-issue:

Reporting Issues
----------------

A great way to contribute to the project is to send a detailed report when you encounter an issue.
I always appreciate a well-written, thorough bug report, and will thank you for it!

.. _quick-contribution-tips-and-guidelines:

Quick Contribution Tips and Guidelines
--------------------------------------

This section gives the experienced contributor some tips and guidelines.

Pull requests are always welcome
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not sure if that typo is worth a pull request? Found a bug and know how to fix
it? Do it! We will appreciate it. Any significant improvement should be
documented as `a GitHub issue <https://github.com/jesuejunior/everest/issues>`_ before
anybody starts working on it.

We are always thrilled to receive pull requests. We do our best to process them
quickly. If your pull request is not accepted on the first try,
don't get discouraged!


Merge approval
~~~~~~~~~~~~~~

Everest maintainers use (:+1:) :+1 emoji in comments on the code review to indicate acceptance.

.. _design-and-cleanup-proposals:

Design and Cleanup Proposals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can propose new designs for existing everest's features. You can also refactor entirely new features. 
I really appreciate contributors who want to refactor or otherwise cleanup our project.

I try hard to keep Everest's lean and focused. Everest's can't do everything for everybody. 
This means that we might decide against incorporating a new feature. 
However, there might be a way to implement that feature on top of Everest's app.

.. _coding-style:

Coding Style
------------

See `PEP8 Docs <https://www.python.org/dev/peps/pep-0008/>`_

*Except for limit all lines to a maximum of 79 characters.*

It can be to maximum of 100 characters.

You must do a check code style with command.

.. code-block:: C
  make check

or 

.. code-block:: C
  make test

All of them will execute pep8 checker and pyflakes.
