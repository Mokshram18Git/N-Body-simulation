Web VPython 3.2


#The physical properties
G = 1
M = 1 
R = 1
rsoft = 0.03 #softening parameter
w = vector(0,0.01,0)

#Creating the stars
n = 0
N = 120

stars = []

#Random positions in the space
while n<N:
  rt = R*vector(2*random()-1,2*random()-1,2*random()-1)
  #the starf
  stars = stars + [sphere(pos=rt,radius=R/30,make_trail=True,retain=100)]
  n = n+1
  
#assigning physical properties
for star in stars:
  star.m = M/N
  #giving the initial Momentum
  star.p = star.m*cross(w,vector(star.pos.x,0,star.pos.z))
  #initial force
  star.F = vector(0,0.05,0)

#time setup for evolution for everyloop
t = 0
dt = 0.01

while t<10:
  rate(100) #simulation speed
  #resetiing the forces before computing gravity
  for star in stars:
    star.F = vector(0,0,0)
    #computing gravity between every pair
  for i in range(len(stars)):
    for j in range(len(stars)):
      if i!=j:
        rji = stars[i].pos - stars[j].pos #distance vector
        #Gravitational forces
        stars[i].F = stars[i].F - G*stars[i].m*stars[j].m*norm(rji)/(mag(rji)**2+rsoft**2)
  #updating the motion
  for star in stars:
    star.p = star.p + star.F*dt
    star.pos = star.pos + star.p*dt/star.m
  t = t+dt #finally increasing the time for further simulation.
      
  
