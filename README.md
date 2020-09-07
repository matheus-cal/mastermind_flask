# Mastermind Game

A tarefa inicial consiste em implementar uma função que gera um número com 4 dígitos não repetidos.

Em seguida, utilizar o flask para disponibilizar esta função via chamada web.

A seguir é implementado uma função que chame a função de geração de número e guarde o número aleatório em um arquivo de texto. Disponibilizar também esta função via API Rest com flask, chamando essa nova interface e retornado um 'OK'.

Em seguida, outra função recebe o conteúdo do arquivo .txt e analisa:

- Se um dígito desse segundo número encontra-se no primeiro número mas na posição errada, coloca-se na resposta um caracter "0".
- Se esse dígito estiver no primeiro número e na posição correta, coloca-se na resposta um caracter "1".
- Se o dígito não estiver no primeiro número, não agregar caracter na resposta.
- Repetir para os demais dígitos.

# Mastermind Game

The initial task consists of implementing a function which creates a 4-digits non-repeated random number.

Then, to use Flask to make this function available in web browser.

Next, another function that calls the first function to create another 4-digits non-repeated random number and save it in a text file is implemented. Provide this function via API Rest with Flask as well, and returning an 'Ok'.

Lastly, a third function that receives the .txt content, another 4-digits non-repeated random number and evaluate:

- If there is an equal digit in both numbers but in different position, it returns a "0".
- If there is an equal digit in both numbers but in the same position, it returns a "1".
- If there is no equal numbers, do not return response.
- Repeat to all digits in the number.

