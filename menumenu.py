import os, random, turtle, time, sys

def programa_1():
    
    print("El destino dice que:" + "\n")

    def respuesta(numResp):
        if numResp == 1:
            return 'Simon, lo que quieras'
        elif numResp == 2:
            return 'Ni creas we, no va a pasar'
        elif numResp == 3:
            return 'Chingate una chela'
        elif numResp == 4:
            return 'Valio verga, Alexa reproduce "No hay Novedad" de Los Cardenales' 
        elif numResp == 5:
            return 'No te vas a morir, si lo intentas'
        elif numResp == 6:
            return 'Simon'
        elif numResp == 7:
            return 'De todos modos, el mundo ya se va a acabar'
        elif numResp == 8:
            return 'Piensalo bien, mejor.'

    r = random.randint(1,8)
    suerte = respuesta(r) 
    print("\t"+suerte+"\n")       
    
def programa_2():
    
    print("\t" + "amongos" + "\n")
    print("NO PUEDES DIBUJAR MAS DE DOS AMONG US, SI LO HACES CRASHEO TU PC Y ME ROBo TUS V-BUCKS")
    BODY_COLOR =  'red'
    BODY_SHADOW = ''
    GLASS_COLOR = '#9acedc'
    GLASS_SHADOW = ''

    screen = turtle.Screen()
    t = turtle.Turtle()

    def body():
        """ draws the body """
        t.pensize(20)
        #t.speed(15)
        t.fillcolor(BODY_COLOR)
        t.begin_fill()
        # right side
        t.right(90)
        t.forward(50)
        t.right(180)
        t.circle(40, -180)
        t.right(180)
        t.forward(200)

        # head curve
        t.right(180)
        t.circle(100, -180)
        # left side
        t.backward(20)
        t.left(15)
        t.circle(500, -20)
        t.backward(20)

        #t.backward(200)
        t.circle(40, -180)
        #t.right(90)
        t.left(7)
        t.backward(50)

        # hip
        t.up()
        t.left(90)
        t.forward(10)
        t.right(90)
        t.down()
        #t.right(180)
        #t.circle(25, -180)
        t.right(240)
        t.circle(50, -70)

        t.end_fill()


    def glass():
        t.up()
        #t.right(180)
        t.right(230)
        t.forward(100)
        t.left(90)
        t.forward(20)
        t.right(90)

        t.down()
        t.fillcolor(GLASS_COLOR)
        t.begin_fill()

        t.right(150)
        t.circle(90, -55)

        t.right(180)
        t.forward(1)
        t.right(180)
        t.circle(10, -65)
        t.right(180)
        t.forward(110)
        t.right(180)
            
        #t.right(180)
        t.circle(50, -190)
        t.right(170)
        t.forward(80)

        t.right(180)
        t.circle(45, -30)

        t.end_fill()

    def backpack():
        t.up()
        t.right(60)
        t.forward(100)
        t.right(90)
        t.forward(75)

        t.fillcolor(BODY_COLOR)
        t.begin_fill()

        t.down()
        t.forward(30)
        t.right(255)

        t.circle(300, -30)
        t.right(260)
        t.forward(30)

        t.end_fill()


    body()
    glass()
    backpack()

    turtle.bye()

def programa_3():
    
    print("Mucha suerte!")

    NumeroSec = random.randint(1, 20)
    print('Tengo un numero en mente, del 1 al 20' + "\n")
    print('Solo tienes 6 intentos' + "\n")

    # Aqui se empiezan a contar los intentos
    for intentosHechos in range(1, 7):
        print('A ver, atinale.' + "\n")
        adivina = int(input()) #Mas que obvio, el valor escrito por el user debe ser en entero 

        if adivina < NumeroSec:
            print("\n" + 'El numero es muy bajo.' + "\n")
        elif adivina > NumeroSec:
            print("\n" + 'Ya te pasaste, es muy alto.' + "\n")
        else:
            break
    if adivina == NumeroSec:
        print('Felicidades, le atinaste en : ' + str(intentosHechos) + ' intentos!')
    else:
        print('La cagaste we, el numero que tenia en mente era el:  ' + str(NumeroSec))

def main():
    while True:
        
        print("Bienvenido al menú:" + "\n")
        print("Elige sabiamente" + "\n")
        print("1. Te dare la respuesta que buscas")
        print("2. Amogos")
        print("3. Atinale al numero!")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            programa_1()
        elif opcion == "2":
            programa_2()
        elif opcion == "3":
            programa_3()
        elif opcion == "4":
            
            print("¡Hasta luego!")
            turtle.bye()
            break
        else:
            input("Opción no válida. Ahora por menso, me burlare de ti.")
            indent = 0 # Espacio de la sangria
            indentIncreasing = True # Este ciclo sirve para llevar la cantidad de sangrias
            try:
                while True: # Ciclo principal del programa
                    print(' ' * indent, end='')
                    print('jejejeje')
                    time.sleep(0.1) # Pausa ligera, de una decima de segundo.

                    if indentIncreasing:
                        # Aumente el espacio de las lineas
                        indent = indent + 1
                        if indent == 20:
                            # Para cambiar la direccion:
                            indentIncreasing = False

                    else:
                        # Reducir espacios
                        indent = indent - 1
                        if indent == 0:
                            # Y cambiar direccion. 
                            indentIncreasing = True
            # Y al darle cualquier tecla, detener programa
            except KeyboardInterrupt:
                sys.exit()
    turtle.mainloop()    

if __name__ == "__main__":
    main()
