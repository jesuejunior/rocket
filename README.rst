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

    $ cd /tools && sudo docker-compose run sentry upgrade

Agora é só seguir o step-by-step e ao fim você consiguirá acessar a interface.

