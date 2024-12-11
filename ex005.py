#Desafio 5
x = input('Digite qualquer coisa:')

print(f'''Ele é alfanúmerico? {x.isalnum()}
          Ele contém letras? {x.isalpha()}
          Ele é númerico? {x.isnumeric()}
        Ele é digito? {x.isdigit()}''')