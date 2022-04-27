# Créditos: código del equipo "Rodi Balboa", ganador del torneo de robot-sumo (RoDI)

import rodi
import time
import keyboard


robot = rodi.RoDI()
# for i in range(4):
#   robot.move_forward()
#  time.sleep(1.5)
# robot.move_stop()
# robot.move_left()
# time.sleep(0.55)
# robot.move_stop()
# RODI CANTA
doremi_hz = ["2093", "2349", "2637", "2794", "3136", "3520", "3951", "4699", "4186"]
do = doremi_hz[0]
re = doremi_hz[1]
mi = doremi_hz[2]
fa = doremi_hz[3]
sol = doremi_hz[4]
la = doremi_hz[5]
si = doremi_hz[6]
re1 = doremi_hz[7]
do1 = doremi_hz[8]
cumple = [
    sol,
    sol,
    la,
    sol,
    do,
    si,
    sol,
    sol,
    la,
    sol,
    re1,
    do1,
    do,
    mi,
    sol,
    mi,
    do,
    si,
    la,
    fa,
    fa,
    mi,
    do,
    re,
    do,
]
rodi_entrada = [mi, sol, sol, la, la, la, la]
# print(len(cumple))
# RODI ESQUIVA AUTOMATICO
# for i in range(4):
#   print(robot.see())
#  time.sleep(0.1)
# def ataque():
#    if int(robot.see()) < 10:
#        robot.move_stop()
#        robot.move_left()
#        time.sleep(0.5)

# while True:
#    robot.move_forward()
#    print(robot.see())
#    ataque()
#    time.sleep(0.2)
"""def al_frente():
  if keyboard.is_pressed('w'):
    robot.move_forward()
def izquierda():
  if keyboard.is_pressed('a'):
    robot.move_left()"""


def entrada():
    robot.sing(mi, 250)
    time.sleep(0.25)
    robot.sing(sol, 500)
    time.sleep(0.5)
    robot.sing(la, 2000)
    time.sleep(2)
    robot.sing(la, 250)
    time.sleep(0.25)
    robot.sing(si, 500)
    time.sleep(0.5)
    robot.sing(mi, 2000)
    time.sleep(2)
    # robot.move_forward()
    """for i in range(len(rodi_entrada)):  
    robot.sing(int(rodi_entrada[i]),250)
    time.sleep(0.250)
  robot.move_stop()"""


# entrada()

while True:
    if keyboard.is_pressed("w"):
        robot.move_forward()
    elif keyboard.is_pressed("a"):
        robot.move_left()
    elif keyboard.is_pressed("d"):
        robot.move_right()
    elif keyboard.is_pressed("s"):
        robot.move_backward()
    elif keyboard.is_pressed("p"):
        entrada()
    else:
        robot.move_stop()
