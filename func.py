import random
import os
from flask import request


def num_ran():

    num = random.sample(range(0, 9), 4)
    ran = "".join(map(str, num))

    return ran


def inicia():

    local = os.getcwd()
    arq = os.path.join(local, 'arquivo.txt')

    with open(arq, 'w') as file:
        arquivo = num_ran()
        file.write(str(arquivo))

    return 'OK'


def tentativa():

    ran_num2 = request.args['num']

    local = os.getcwd()
    arq = os.path.join(local, 'arquivo.txt')

    with open(arq, 'r') as file:
        arquivo = file.readline()

    ran_num1 = str(arquivo)
    bin_num = ''

    for i, it in enumerate(ran_num1):

        if it in ran_num2 and it != ran_num2[i]:
            bin_num += str(0)
        elif it in ran_num2 and it == ran_num2[i]:
            bin_num += str(1)
        else:
            pass

    return bin_num


# if __name__ == "__main__":
#     num_ran()
#     inicia()
#     tentativa()