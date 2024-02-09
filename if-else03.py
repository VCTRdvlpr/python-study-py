altura = int(input('Preencha sua altura em centímetros: '));
peso = int(input('Informe seu peso em kg: '));
idade = int(input('Informe sua idade em anos: '));

if altura > 150:
    if peso < 100:
        if peso > 50:
            if idade >= 18:
                if idade <= 30:
                    print('Está apto!');
                else:
                    print('Não está apto, não possui idade necessária!');
            else:
                print('Não está apto, não possui idade necessária!');
        else:
            print('Não está apto, peso abaixo do requisito!');
    else:
        print('Não está apto, peso acima do requisito!');
else:
    print('Não está apto, altura abaixo do requisito!');

