Rocket Project
==============


Sentry Setup
------------

You'll need to be in ansible directory.

.. code-block:: shell
    $ cd ansible 

.. code-block:: shell
    
   $ ansible-playbook ops/tasks/core/sentry.yml

Criando o primeiro usuário, precisa entrar no servidor(inicialmente).

.. code-block:: shell

    $ cd /home/rocket/tools && sudo docker-compose run sentry upgrade

Now, you just need follow step-by-step answering the questions.

That's it. Now You have awesome *Sentry* ready to use.

Generate password to user a own user like a Rocket User created by default in *base task*

.. code-block:: python

    $ python -c "from passlib.hash import sha512_crypt; import getpass; print sha512_crypt.encrypt(getpass.getpass())"


Self-signed Certificate
^^^^^^^^^^^^^^^^^^^^^^^

Generating self-signed TLS certificate for *NGINX8 and/or *Private Docker Registry*

.. code-block:: shell

    $ mkdir -p certs && openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key -x509 -days 365 -out certs/domain.crt