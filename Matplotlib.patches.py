#Circle

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig, ax =plt.subplots()
shape=mpatches.Circle((0.5,0.5),radius=2)
ax.add_patch(shape)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_aspect("equal")
plt.title("Circle")
plt.show()

#Axes Coordinates 
circle=mpatches.Circle((0,0),radius=0.2,transform=ax.transAxes)
ax.add_patch(circle)
ax.set_aspect("equal")
plt.title("Circle2")
plt.show()

# Data Coordinates
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
ax.plot(x,y)
circle=mpatches.Circle((3,1),radius=.2,
                       label="Mera Gola")
ax.add_patch(circle)
ax.set_aspect("equal")
plt.legend()
plt.title("Circle3")
plt.show()

#Circle
fig, ax=plt.subplots()
shape=mpatches.Circle(
    (2,2),
    radius=2,
    )
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.add_patch(shape)
ax.set_aspect("equal")
plt.show()

#reactangle
fig,ax=plt.subplots()
rect=mpatches.Rectangle(
    (2,2),
    width=2,
    height=2,
    angle=0
)
ax.add_patch(rect)
ax.set_xlim(0,5)
ax.set_ylim(0,5)
plt.show()

#Ellipse
fig,ax=plt.subplots()
eli=mpatches.Ellipse(
    (2,2),
    width=2,
    height=2,
    angle=0
    )
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.add_patch(eli)
plt.show()

#Trangle
fig,ax=plt.subplots()
tr=mpatches.Polygon(
    ([1,1],[1,2],[3,5]),closed=True
)
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.add_patch(tr)
ax.set_aspect("equal")
plt.title("Trangle")
plt.show() 

#hexagon
import numpy as np
fig,ax=plt.subplots()
angles=np.linspace(0,2*np.pi,7)[:-1]
hex=np.column_stack([0.5+0.3*np.cos(angles),
                    0.5+0.3*np.sin(angles)],)
hexagon=mpatches.Polygon(hex,closed=True)
ax.add_patch(hexagon)
plt.show()

#The atom diagram(not real)

fig,ax=plt.subplots()
circle=mpatches.Circle((5,5),radius=1,
                    color="darkred")
for angle in [0,60,120]:
    elp=mpatches.Ellipse((5,5),
                         width=6.5,
                         height=2,
                         color="steelblue",
                         fill=False,
                         linewidth=2,
                         angle=angle)
    ax.add_patch(elp)
ax.add_patch(circle)

position_electron=[(8.23,4.90),(6.58,7.78),(6.58,2.16)]
for i in position_electron:
    cir=mpatches.Circle((i),radius=.3,
                        color="dodgerblue")
    ax.add_patch(cir)
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_aspect("equal")
plt.show()