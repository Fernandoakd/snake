import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
highScore = 0
vidas = 3


#Configuracion de la ventana
ventana = turtle.Screen()
ventana.title("Juego de Snake")
ventana.bgcolor("black")
ventana.setup(width = 600, height = 600)
ventana.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
cabeza.color("white")

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")

#Segmentos / cuerpo serpiente
segmentos = []


#Marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,250)
texto.write("Score: 0	  Vidas: 3	  High Score: 0",
			align = "center", font =("Courier", 14, "normal"))

#Funciones
def arriba():
	cabeza.direction = "up"

def abajo():
	cabeza.direction = "down"

def izquierda():
	cabeza.direction = "left"

def derecha():
	cabeza.direction = "right"

def limpiaPantalla():
	texto.clear()
	texto.write("Score: {}	 Vidas: {}	 High Score: {}".format(score,vidas,highScore),
				align = "center", font =("Courier", 14, "normal"))

def esconderSeg():
	#esconder segmentos
	for segmento in segmentos:
		segmento.goto(2000,2000)

	#limpiar segmentos
	segmentos.clear()


def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)

	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)


#Teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")


while vidas != 0:
	ventana.update()

	if cabeza.distance(comida) < 20:
		#mover la comida a la posicion random
		x = random.randint(-280,280)
		y = random.randint(-280,240)
		comida.goto(x,y)

		nuevoSegmento = turtle.Turtle()
		nuevoSegmento.speed(0)
		nuevoSegmento.shape("square")
		nuevoSegmento.penup()
		nuevoSegmento.color("grey")
		segmentos.append(nuevoSegmento)

		#Aumentar marcador
		score += 10

		if score > highScore:
			highScore = score
			limpiaPantalla()

	#Colisiones bordes
	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"
		esconderSeg()

		#Resetear marcador
		score = 0
		vidas -= 1
		limpiaPantalla()


	#Colisiones con el cuerpo
	for segmento in segmentos:
		if segmento.distance(cabeza) < 20:
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction = "stop"
			esconderSeg()	

			#Resetear marcador
			score = 0
			vidas -= 1
			limpiaPantalla()


	#Mover el cuerpo de la serpiente
	totalSeg = len(segmentos)
	for index in range(totalSeg - 1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x,y)

	if totalSeg>0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x,y)



	mov()
	time.sleep(posponer)

