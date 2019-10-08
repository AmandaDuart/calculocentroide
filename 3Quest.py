#SubPrograma
import pdb 
def num(s):
	ponto_c = s.split(' ')
	try:
		return (float(ponto_c[0])),(float(ponto_c[1]))
	except ValueError:
		return float(s)

def centroide(x, y, total_x, total_y, p):
	print(x, y)
	centro_x = total_x / p
	centro_y = total_y / p
	print('Centroide:', round(centro_x,1), centro_y)
'''
def distancia(x_p, y_p, x_c, y_c):
	print(x,y,'centro x:',centro_x,'centro y:',centro_y)
	raiz_x = (x - centro_x) ** (1/2)* 0.5
	raiz_y = (y - centro_y) ** (1/2)
	print('Ponto mais próximo:',round(raiz_x, 1), round(raiz_y, 1))
'''
#ProgramaPrincipal
lista_x = []
lista_y = []
x = []
y = []
p = 0
total_x = float(0)
total_y = float(0)
nomearquivo = open(input('digite o nome arquivo:'), 'r')
conteudo = nomearquivo.readlines()	
novoarquivo =  open(input('digite o nome arquivo:'),'w')
for ponto in conteudo:
	pdb.set_trace()
	ponto.replace('\n','')
	x = ponto[0]
	y = ponto[1]
	lista_x.append(x)
	lista_y.append(y)		
	p += 1
	total_x += x
	total_y += y
centroide(x, y, total_x, total_y, p)
