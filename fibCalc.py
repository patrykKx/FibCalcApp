def getFibonacciElement():
    print("=================================================================")
    while True:
        try:
            numb = int(input(("Podaj proszę numer elementu ciągu Fibonacciego (nieujemna liczba całkowita): ")))
        except:
            numb = -1
        finally:
            if(numb >= 0):
                break
            
    a = 0
    b = 1
    temp = 1        
    for i in range(0, numb): 
        temp = a
        a = a + b
        b = temp
        
    print("fib("+str(numb)+") = "+str(a))    
    print("=================================================================")
    

def getAuthorInfo():
    print("=====================================")
    print("NAZWA PROGRAMU:")
    print("FibCalc")
    print("");
    print("DANE AUTORA:")
    print("Patryk Kaźmierak") 
    print("Grupa 2")   
    print("=====================================")

while True:
    print("MENU GŁÓWNE")
    print("1. Wyświetl wartość ciągu Fibonacciego")
    print("2. Wyświetl dane autora")
    print("3. Wyjdź z programu")
    try:
        decision = int(input("Twój wybór: "))
    except: 
        decision = -1
    
    if(decision == 1):
        getFibonacciElement()
    elif(decision == 2):
        getAuthorInfo()
    elif(decision == 3):
        break