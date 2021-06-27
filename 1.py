H=116
Vy=79
g=1.62
G=9.81
Ma=2150
m=200
Vp=3660
amax=3*G
M=Ma+m
alfa=180
r=0
t=0
dt=0.1

print(' Vy    ''   H       '' alfa    '    '  dm   ' '     t   ')
while(H-(Vy**2)/(amax-g)>0 and m>0):
 print(f'{Vy:.3f}',' ',f'{H:.3f}',' ',f'{alfa:.3f}',' ',f'{r*dt:.3f}',' ',f'{t:.3f}')
 H-=(Vy*dt-(-g)*(dt**2)/2)
 Vy+=g*dt
 M-=r*dt
 t+=dt
 m-=r*dt
while(H>0 and m>0 and Vy>3):
 print(f'{Vy:.3f}',' ',f'{H:.3f}',' ',f'{alfa:.3f}',' ',f'{r*dt:.3f}',' ',f'{t:.3f}')
 a=amax
 r=M*a/Vp
 H-=(Vy*dt-(a-g)*(dt**2)/2)
 Vy+=(g-a)*dt
 M-=r*dt
 t+=dt
 m-=r*dt
while(H>0 and m>0):
 print(f'{Vy:.3f}',' ',f'{H:.3f}',' ',f'{alfa:.3f}',' ',f'{r*dt:.3f}',' ',f'{t:.3f}')
 a=g
 r=M*a/Vp
 H-=(Vy*dt-(a-g)*(dt**2)/2)
 Vy+=(g-a)*dt
 M-=r*dt
 t+=dt
 m-=r*dt
print(f'{Vy:.3f}',' ',0,' ',f'{alfa:.3f}',' ',f'{r*dt:.3f}',' ',f'{t:.3f}')


