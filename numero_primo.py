numero= int(input("digite un numero primo: "))
def numeros_primos():
    contador = 0
    for i in range(1, numero+1):
        if numero % i== 0:
            contador += 1
    if contador == 2:
        print(f"el numero: {numero} es primo")
        return True
    else:
        print(f"el numero: {numero} no es primo")
    return False           


   

def main():
    numeros_primos()

if __name__ == "__main__":
    main()         