var_verdadeiro = True
var_falso = False

print(type(var_verdadeiro), type(var_falso)) #boolean

if var_verdadeiro == True:
    print("É verdadeiro")
else:
    print("É falso")

if var_falso == False:
    print("É verdadeiro")
else:
    print("É falso")

if var_verdadeiro == True and var_falso == False:
    print("É verdadeiro, segundo parâmetro")
else:
    print("É falso, segundo parâmetro")


