import random
import math

def random_point_on_sphere(radius=1,hemisphere=False) :
    xiTheta=random.uniform(0,1)
    temp=2.0*radius*math.sqrt(xiTheta*(1.0 - xiTheta))
    twoPiXiPhi=math.pi*2*random.uniform(0,1)
    x=temp*math.cos(twoPiXiPhi)
    y=temp*math.sin(twoPiXiPhi)
    if hemisphere == True :
        y=abs(y)
    z=radius*(1.0 - 2.0*xiTheta)
    return x,y,z

for _ in range(5):
    x,y,z=random_point_on_sphere(14,hemisphere=True)
    print(f"{x=}, {y=}, {z=}")