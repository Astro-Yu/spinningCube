import numpy as np
import time

cubeWidth = 20
cubeHeight = 20
A,B,C = 0,0,0
distanceFromCam = 100
width = 160
height = 44
K1 = 40
horizontalOffset = 0
incrementSpeed = 1.5
backgroundASCIICode = ' '

print("\x1b[2J",end='')

def calculateX(i, j, k):
  return j * np.sin(A) * np.sin(B) * np.cos(C) - \
    k * np.cos(A) * np.sin(B) * np.cos(C) + \
    j * np.cos(A) * np.sin(C) + \
    k * np.sin(A) * np.sin(C) + \
    i * np.cos(B) * np.cos(C);

def calculateY(i, j, k):
  return j * np.cos(A) * np.cos(C) + \
    k * np.sin(A) * np.cos(C) - \
    j * np.sin(A) * np.sin(B) * np.sin(C) + \
    k * np.cos(A) * np.sin(B) * np.sin(C) - \
    i * np.cos(B) * np.sin(C);

def calculateZ(i, j, k) :
  return k * np.cos(A) * np.cos(B) - \
    j * np.sin(A) * np.cos(B) + \
    i * np.sin(B);


def calculateOnSurface(i, j, k, ch):
    x = calculateX(i, j, k)
    y = calculateY(i, j, k)
    z = calculateZ(i, j, k) + distanceFromCam

    ooz = 1 / z

    xp = (int)(width / 2 + horizontalOffset + K1 * ooz * x * 2);
    yp = (int)(height / 2 + K1 * ooz * y);

    idx = xp + yp * width;

    if idx >= 0 and idx < width * height:
       if ooz > zBuffer[idx]:
          zBuffer[idx] = ooz
          buffer[idx] = ch

def clear_terminal():
    print('\x1b[H')
        

while(True):
    
    buffer = [backgroundASCIICode] * (width * height)
    zBuffer = [0] * (width * height)

    cubeWidth = 20
    horizontalOffset = 0.5 * cubeWidth
    for cubeX in np.arange(-cubeWidth,cubeWidth,incrementSpeed):
        for cubeY in np.arange(-cubeWidth,cubeWidth,incrementSpeed):
            calculateOnSurface(cubeX,cubeY,-cubeWidth,'\033[95m' + '@' + '\033[0m')
            calculateOnSurface(cubeWidth,cubeY,cubeX,'\033[34m'+ '$' + '\033[0m')
            calculateOnSurface(-cubeWidth,cubeY,-cubeX,'\033[32m' + '~' + '\033[0m')
            calculateOnSurface(-cubeX,cubeY,cubeWidth,'\033[38;5;208m' + '#' + '\033[0m')
            calculateOnSurface(cubeX,-cubeWidth,-cubeY,'\033[38;5;159m' + ';' + '\033[0m')
            calculateOnSurface(cubeX,cubeWidth,cubeY,"+" + '\033[0m')

    clear_terminal()
    for k in range(width * height):
        print(buffer[k] if k % width != 0 else '\n', end='')

    A += 0.1
    B += 0.1
    C += 0.05

    time.sleep(0.016)