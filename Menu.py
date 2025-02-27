#Menu que no de error para entradas del usuario

fercho = True
comidas = ["1-Hamburgueza","2-Pizza","3-Tacos","4-Sushi","5-Pasta"]
while fercho == True:
    print("Esta es la lista de comidas: ",comidas)
    print("Que comida desea?")
    
    
    try:
        n=int(input())
        print(comidas[n-1])
        fercho = False
    
    except IndexError:
        print("No tenemos disponible una comida ",n)
    except ValueError:
        print("Eso es una palabra animal vuelva y lea")  