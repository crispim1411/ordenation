Configuração do Ambiente do Projeto
************************************

Métodos de ordenação de uma array simples.

Procedimento de setup
======================
#. Criar um ambiente com Pipenv:

    * pipenv shell

#. Instalar os pacotes requeridos:

    * pipenv install

Utilização
===========
* ordenation.py [OPTIONS] [METHOD]

* Options:

    * -n INTEGER              Número de itens na lista randômica (default 10)
    * -in, --input-list TEXT  Array de entrada no formato [a,b,c]
    * --help                  Show this message and exit.

* Methods:
    - bubble
    - bubble2 [#]_
    - straight
    - insertion
    - shell
    - quicksort

.. [#] Método Bubble Sort melhorado


Para mais informações execute

* python ordenation.py --help

