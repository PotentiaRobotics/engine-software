import math as m
def createXProjection(length, duration):
    t = 0;
    f = open("xValues.txt", "w")
    f2 = open("timeX.txt", "w")
    xLambda = length/duration
    w = m.pi * 2
    w = w/duration
    projectedPoints = []
    deltaT = 0.01 #this is an arbitrary delta t, which can be changed later on
    while(t < duration+deltaT):
        value = xLambda*t - (xLambda/w)*m.sin(w*t)
        projectedPoints.append(value)
        f.write(str(value) + "\n")
        f2.write(str(t) + "\n")
        t += deltaT
        t = round(t, 2)
    f.close()
    f2.close()
    return projectedPoints
def createZProjection(height, duration):
    t = 0;
    f = open("zValues.txt", "w")
    f2 = open("timeZ.txt", "w")
    duration = duration/2
    zLambda = height/(duration)
    w = m.pi * 2
    w = w/duration
    projectedPoints = []
    deltaT = 0.01 #this is an arbitrary delta t, which can be changed later on
    while(t < duration+deltaT):
        value = zLambda*t - (zLambda/w)*m.sin(w*t)
        projectedPoints.append(value)
        f.write(str(value) + "\n")
        f2.write(str(t) + "\n")
        t += deltaT
        t = round(t, 2)
    t = duration+deltaT
    while(t < (2 * duration)+deltaT):
        value = -(zLambda*t - (zLambda/w)*m.sin(w*t)) + (height*2)
        projectedPoints.append(value)
        f.write(str(value) +"\n")
        f2.write(str(t)+"\n")
        t += deltaT
        t = round(t, 2)
    f.close()
    f2.close()
    return projectedPoints

#change the values based on the length/height of the step and how long the duration is
createXProjection(0.5,3)
createZProjection(0.4,3)