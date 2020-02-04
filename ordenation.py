import click
from random import randint
from ord_methods import *


@click.command()
@click.argument(
    'method',
    type=click.Choice([
        'bubble',
        'bubble2',
        'straight',
        'insertion',
        'shell',
        'quicksort'
    ])
)
@click.option(
    '-n',
    default=10,
    type=click.IntRange(0, 100),
    help="Número de itens na lista randômica (default 10)"
)
@click.option(
    '--input-list',
    '-in',
    help="Array de entrada no formato [a,b,c]"
)
def ordenation(method, n, input_list):
    """
    Função para ordenação de um array utilizando métodos definidos nas opções da interface da linha de comando.
    Se não houver lista passada por parâmetro gera uma lista randômica de tamanho n.
    """
    try:
        if input_list is None:
            input_list = [randint(1, 10) for i in range(n)]
        else:
            input_list = list(map(int, input_list.strip('[]').split(',')))

        print(f"método: {method} lista: {input_list}")
        method = eval(method)
        method(input_list)

        print(f"Lista ordenada: {input_list}")
        print(Counter())

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == '__main__':
    # inicia interface de linha de comando
    ordenation()
