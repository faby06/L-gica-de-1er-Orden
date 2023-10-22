# Variables que representan los s�ntomas del paciente
tiene_fiebre = True
tiene_tos = True
tiene_dolor_de_garganta = False
# Reglas de diagn�stico
if tiene_fiebre and tiene_tos and tiene_dolor_de_garganta:
    print("El paciente tiene s�ntomas de gripe.")
elif tiene_fiebre and tiene_tos:
    print("El paciente podr�a tener una infecci�n respiratoria.")
elif tiene_fiebre:
    print("El paciente podr�a tener una infecci�n sin especificar.")
else:
    print("El paciente no parece tener s�ntomas graves.")
# Reglas causales 
if tiene_fiebre:
    print("La fiebre puede ser causada por diversas enfermedades, consulte a un m�dico para un diagn�stico preciso.")
if tiene_tos:
    print("La tos podr�a deberse a una infecci�n respiratoria o alergia, consulte a un m�dico para un diagn�stico adecuado.")
if tiene_dolor_de_garganta:
    print("El dolor de garganta podr�a ser el resultado de una infecci�n viral o bacteriana, consulte a un m�dico para un diagn�stico y tratamiento adecuados.")
