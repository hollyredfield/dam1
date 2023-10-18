age = int((input("Dime tu edad: ")))
ingresos = int((input("Ingresos mensuales: ")))
if age <16:
        print("Has de ser mayor de 16")
elif age >16 & ingresos >= 1000:
    print("Puedes tributar")
else:
    print("no puedes tributar")
