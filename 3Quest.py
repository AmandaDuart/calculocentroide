#SubPrograma

def converteNum(s):
	ponto_c = s.split(' ')
	try:
		return (float(ponto_c[0])),(float(ponto_c[1]))
	except ValueError:
		return float(s)

def centroide(total_x, total_y, p):
	centro_x = total_x / p
	centro_y = total_y / p
	return centro_x, centro_y

def distancia(x_p, y_p, x_c, y_c):
	lista_xy = []
	distancias= {}
	menor = float(0)
	for i in range(0, len(x_p)):
		distancia_xy = (((x_c - x_p[i])**2) + (y_c - y_p[i]) ** 2) ** 0.5 
		lista_xy.append(distancia_xy)
		distancias = lista_xy[i], x_p[i], y_p[i]
		if menor == 0:
			menor = lista_xy[i]
		else:
			if lista_xy[i]< menor:
				menor = lista_xy[i]
	for p , v in enumerate(lista_xy):
		if v == menor:
			posição = p
	print('Ponto Mais Próximo:', x_p[posição], y_p[posição])

#ProgramaPrincipal
lista_x = []
lista_y = []
p = 0
total_x = float(0)
total_y = float(0)
nomearquivo = open(input('digite o nome arquivo:'), 'r')
conteudo = nomearquivo.readlines()	
novoarquivo =  open(input('digite o nome arquivo:'),'w')
for ponto in conteudo:
	ponto.replace('\n','')
	ponto = converteNum(ponto)	
	x = ponto[0]
	y = ponto[1]
	lista_x.append(x)
	lista_y.append(y)		
	p += 1
	total_x += x
	total_y += y
centro_x,centro_y = centroide(total_x, total_y, p)
distancia(lista_x, lista_y, centro_x, centro_y)
print('Centroide:', round(centro_x, 1), centro_y)
