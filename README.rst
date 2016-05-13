Rocket Project
==============


Instalação do Sentry
--------------------

.. code-block:: shell
    $ cd ansible 

.. code-block:: shell
    
   $ ansible-playbook ops/tasks/core/sentry.yml

Criando o primeiro usuário, precisa entrar no servidor(inicialmente).

.. code-block:: shell

    $ cd /home/rocket/tools && sudo docker-compose run sentry upgrade

Agora é só seguir o step-by-step e ao fim você consiguirá acessar a interface.

Generate password to user

.. code-block:: python

    $ python -c "from passlib.hash import sha512_crypt; import getpass; print sha512_crypt.encrypt(getpass.getpass())"

