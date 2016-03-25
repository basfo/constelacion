# Integrantes:
# 19521626-6 Jose Follert Muller
# 19542551-5 Andres Navarro Galleguillos
# 18000890-k Barbara Uribe Cataldo
###############################################################
import turtle
import os
###############################################################
def dibujarcords(cords):
    lar = len(cords)
    i = 0
    n = ""
    sw = False
    turtle.up()
    turtle.color("green")
    x = ""
    y = ""
    gr = ""
    ds = ""
    ch = False
    letra = ""
    pos = False
    
    while i < lar:
        if sw == True:
            if cords[i] not in "0123456789-":
                if pos == True:
                    print(x,y)
                    turtle.goto(int(x),int(y))
                    turtle.down()
                    sw = False
                    pos = False
                    
                if letra == "x":
                    letra=""
                    sw = False
                
                if letra == "y":
                    pos = True
                    letra = ""

                if letra == "r":
                    sw = False
                    turtle.rt(int(gr))
                    print gr
                    letra = ""
                    gr = ""

                if letra == "l":
                    sw = False
                    turtle.lt(int(gr))
                    print gr
                    letra = ""
                    gr = ""

                if letra == "c":
                    sw = False
                    turtle.fd(int(ds))
                    print ds
                    letra = ""
                    ds = ""
                    
            else:
                if letra == "x":
                    x = x + cords[i]
                    i = i + 1
                    
                elif letra == "y":
                    y = y + cords[i]
                    i = i + 1
                    
                    
                elif letra == "r":
                    gr = gr + cords[i]
                    i = i + 1

                elif letra == "l":
                    gr = gr + cords[i]
                    i = i + 1

                elif letra == "c":
                    ds = ds + cords[i]
                    i = i +1

                    
        else:
            if cords[i] not in "0123456789-":
                sw = True
                letra = cords[i]
                i = i + 1

    turtle.fd(int(ds))
    print ds
                     

def salida():
    print """
    Hasta la proxima
    """
def menuprin():
    os.system("cls")
    print "Bienvenido al menu de La Constelacion de Santa Maria"
    print "Opciones"
    print """
    I-----------------------------------------I
    I 1 - Buscar constelaciones               I
    I 2 - Ingresar constelacion               I
    I 3 - Distancia entre dos constelaciones  I
    I 4 - Salir                               I
    I-----------------------------------------I
    """
    op = int(raw_input('Ingrese una opcion:'))
    
    if op==1:
        os.system("cls")
        print """
        Que constelacion desea visualizar?
        I------------------------------------------I
        I 1  - Aries                               I
        I 2  - Auriga                              I
        I 3  - Cancer                              I
        I 4  - Canismajor                          I
        I 5  - Canisminor                          I
        I 6  - Cassioppeia                         I
        I 7  - Cepheus                             I
        I 8  - Geminis                             I
        I 9  - Leo                                 I
        I 10 - Osamenor                            I
        I 11 - Picis                               I
        I------------------------------------------I

        Si desea volver al menu ingrese 12 y si desea limpiar ingrese 0
        """
        const = raw_input("-->")
		aries = "x-235y41r54c9l40c19l54c76"
		auriga = "x-10y-23r50c54l136c48l102c38r80c64r69c38r93c54r41c38"
		cancer = "x200y0l70c63r35c33l180c33r110c59"
		canismajor = "x70y344r12c56r36c20l80c23l180c23l20c55r70c31r180c31r1c26"
		canisminor = "x146y140l29c25"
		cassioppeia = "x-102y-147r181c24l60c18r68c24l105c26"
		cepheus = "x-128y-237r47c49r112c41r70c55r118c43r5c63r131c54"
		geminis = "x142y38r138c20r89c63l9c27l25c9l22c12x142y38r76c42l30c20r8c38r87c18"
		leo = "x320y25r62c95l5c46r142c50r110c33x320y25l186c28l36c24r49c19r61c29r75c15"
		osamenor =
		picis =
		

    elif op==2:
        print """
        Ingrese la constelacion en la forma indicada
        Si desea volver al menu ingrese 1 y si desea limpiar ingrese 0
        """
        cords = raw_input("Ingrese coordenadas:")
        dibujarcords(cords)
        

    elif op==3:
        print """
        Distancia entre 2 constelaciones
        I------------------------------------------I
        I 1  - Aries                               I
        I 2  - Auriga                              I
        I 3  - Cancer                              I
        I 4  - Canismajor                          I
        I 5  - Canisminor                          I
        I 6  - Cassioppeia                         I
        I 7  - Cepheus                             I
        I 8  - Gemini                              I
        I 9  - Leo                                 I
        I 10 - Osamenor                            I
        I 11 - Picis                               I
        I------------------------------------------I
        Ingrese el numero de las dos constelaciones
        Si desea volver al menu ingrese 12 y si desea limpiar ingrese 0
        """
        
    elif op==4:
        salida()
        raw_input()

    else:
        os.system("cls")
        print """ingrese un numero valido plox"""
        raw_input() 
        menuprin()

###############################################################

turtle.title("La Constelacion de Santa Maria")
turtle.setup(880, 880, 0, 0)

turtle.bgpic("bg.gif")
turtle.color("white")
turtle.hideturtle()

turtle.speed("100")

#SE GRAFICAN LAS CIRCUNFERENCIAS
turtle.up()
turtle.setpos(440, 0)
turtle.down()
turtle.left(90)
turtle.circle(440)

#SEGUNDA CIRCUNFERENCIA
turtle.setpos(220, 0)
turtle.circle(220)

turtle.goto(0, 0)
turtle.left(90)
turtle.down()

#SE GRAFICAN LAS LINEAS CENTRALES
i = 0
while i < 8:
    turtle.forward(440) # El radio
    turtle.up()
    turtle.goto(0, 0)
    turtle.right(45) # giramos 45 grados
    turtle.down()
    i = i + 1

####################################################

menuprin()
raw_input()
