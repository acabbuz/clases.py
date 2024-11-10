num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))
caracter= input("caracter para realizar la operación: ")

def calculadora(num1, num2, caracter):
    if caracter =="+":
        resultado  = num1 + num2

    elif caracter =="-":
        
        if num1<num2:
            num1 = int(input("Introduzca un número valido: "))
            num2 = int(input("Segundo numero: "))
            caracter= input("caracter para realizar la operación: ")

        resultado  = num1 - num2

    elif caracter =="/" and (not num2==0):
        resultado  = num1 / num2

    elif caracter =="*":
        resultado  = num1 * num2

    return resultado

#assert(calculadora(23,7,"+")==30)
#assert(calculadora(30,3,"-")==27)
#assert(calculadora(20,2,"/")==10)
#assert(calculadora(7,3,"*")==21)

print(calculadora(num1,num2, caracter))




