# Importa a classe 'date' do módulo 'datetime' para trabalhar com datas
from datetime import date

# Obtém o ano atual usando a função today() e acessa apenas o ano
atual = date.today().year

# Solicita ao usuário que informe o ano de nascimento e converte o input em inteiro
nasc = int(input("Qual ano você nasceu? "))

# Calcula a idade atual subtraindo o ano de nascimento do ano atual
idade = atual - nasc

# Exibe a idade do usuário com base no ano de nascimento e no ano atual
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))

# Verifica se o usuário tem exatamente 18 anos
if idade == 18:
    print("Você Deve se Alistar!")

# Se o usuário for menor de 18 anos, ainda não precisa se alistar
elif idade < 18:
    print("Você tem {} anos. Você não precisa se ALISTAR ainda!".format(idade))
    
    # Calcula e informa o ano futuro em que o usuário deverá se alistar
    print("Seu alistamento será em {}".format(atual + (18 - idade)))

# Se o usuário tiver mais de 18 anos, já deveria ter se alistado
else:
    print("Você tem {} anos, você tinha que ter se alistado há {} anos, em {}. Vá Urgente se ALISTAR!".format(
        idade, idade - 18, atual - (idade - 18)))