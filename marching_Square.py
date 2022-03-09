import matplotlib.pyplot as plt
import random
import time
from matplotlib.animation import FuncAnimation
def get_coord(char,i,j):
	if(char=='a'):
		x=[i+0.5,i+1]
		y=[j,j+0.5]
		plt.plot(x,y,color="black")
	elif(char=='b'):
		x=[i+1,i+0.5]
		y=[j+0.5,j+1]
		plt.plot(x,y,color="black")
	elif(char=='c'):
		x=[i+0.5,i]
		y=[j,j+0.5]
		plt.plot(x,y,color="black")
	elif(char=='d'):
		x=[i,i+0.5]
		y=[j+0.5,j+1]
		plt.plot(x,y,color="black")
	elif(char=='e'):
		x=[i+1,i]
		y=[j+0.5,j+0.5]
		plt.plot(x,y,color="black")
	elif(char=='f'):
		x=[i+0.5,i+0.5]
		y=[j,j+1]
		plt.plot(x,y,color="black")
field=[]
rows=40
cols=40
fig,ax=plt.subplots(1,1,figsize=(20,20))
#ax.set_facecolor('0.9')
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

for i in range(rows):
		row=[]
		for j in range(cols):
			row.append(0)
		field.append(row)
def animation(i):
	ax.cla()
#	ax.set_facecolor('0.9')
	ax.get_xaxis().set_ticks([])
	ax.get_yaxis().set_ticks([])
	for i in range(rows):
		for j in range(cols):
			field[i][j]=random.randint(0,1)/1	
	for i in range(rows):
		for j in range(cols):
			plt.scatter(i,j,s=12,color=str(field[i][j]))
	for i in range(rows-1):
		for j in range(cols-1):
			number=field[i][j+1]+field[i][j]*2+field[i+1][j+1]*4+field[i+1][j]*8
			if(number==1 or number==14):
				get_coord('d',i,j)
			elif(number==2 or number==13):
				get_coord('c',i,j)
			elif(number==3 or number==12):
				get_coord('f',i,j)
			elif(number==4 or number==11):
				get_coord('b',i,j)
			elif(number==5 or number==10):
				get_coord('e',i,j)
			elif(number==6 or number==9):
				get_coord('a',i,j)
				get_coord('d',i,j)
			elif(number==7 or number==8):
				get_coord('a',i,j)				
anim=FuncAnimation(fig,animation,interval=100)
plt.show()
