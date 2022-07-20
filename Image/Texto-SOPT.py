from time import sleep

print('Sabe oq é loko ?')
sleep(1.0)
Resposta = str(input('Digite sua resposta [S/N]: ')).upper()
sleep(0.5)

if Resposta == 'S':
    print('Então você é uma pessoa de cultura!')
    
elif Resposta == 'N':
    print('''
    Não sabe!, Então aprenda:
    [ 1 ]: Front-end é maneiro!
    [ 2 ]: Bon Jovi é maneiro!
    [ 3 ]: Ser Nerd/Otaku é maneiro!
    [ 4 ]: Tecnologia é maneiro!
    [ 5 ]: Jogar games é maneiro!
    ''')
