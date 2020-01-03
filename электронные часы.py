import datetime
import time
import os

symbols ={
'0':['  ▇▇▇▇    ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','  ▇▇▇▇    '],
'1':['      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  '],
'2':['▇▇▇▇▇▇▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','▇▇▇▇▇▇▇▇  ','▇▇        ','▇▇        ','▇▇        ','▇▇▇▇▇▇▇▇  '],
'3':['▇▇▇▇▇▇▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','▇▇▇▇▇▇▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','▇▇▇▇▇▇▇▇  '],
'4':['▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇▇▇▇▇▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  '],
'5':['▇▇▇▇▇▇▇▇  ','▇▇        ','▇▇        ','▇▇        ','▇▇▇▇▇▇▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','▇▇▇▇▇▇▇▇  '],
'6':['▇▇▇▇▇▇▇▇  ','▇▇        ','▇▇        ','▇▇        ','▇▇▇▇▇▇▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇▇▇▇▇▇▇  '],
'7':['▇▇▇▇▇▇▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  '],
'8':['▇▇▇▇▇▇▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇▇▇▇▇▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇▇▇▇▇▇▇  '],
'9':['▇▇▇▇▇▇▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇    ▇▇  ','▇▇▇▇▇▇▇▇  ','      ▇▇  ','      ▇▇  ','      ▇▇  ','▇▇▇▇▇▇▇▇  '],
':':['          ','          ','          ','          ','   ▇▇▇▇   ','   ▇▇▇▇   ','          ','          ','          '],
'_':['          ','          ','          ','          ','          ','          ','          ','          ','          '],
}

def numbers_for_clock(x):
    numbs = []
    for numb in x:
        numbs.append(symbols[numb])
    print(numbs[0][0], ' ', numbs[1][0], ' ', numbs[2][0], ' ', numbs[3][0], ' ', numbs[4][0], ' ', numbs[5][0], ' ', numbs[6][0], ' ', numbs[7][0])
    print(numbs[0][1], ' ', numbs[1][1], ' ', numbs[2][1], ' ', numbs[3][1], ' ', numbs[4][1], ' ', numbs[5][1], ' ', numbs[6][1], ' ', numbs[7][1])
    print(numbs[0][2], ' ', numbs[1][2], ' ', numbs[2][2], ' ', numbs[3][2], ' ', numbs[4][2], ' ', numbs[5][2], ' ', numbs[6][2], ' ', numbs[7][2])
    print(numbs[0][3], ' ', numbs[1][3], ' ', numbs[2][3], ' ', numbs[3][3], ' ', numbs[4][3], ' ', numbs[5][3], ' ', numbs[6][3], ' ', numbs[7][3])
    print(numbs[0][4], ' ', numbs[1][4], ' ', numbs[2][4], ' ', numbs[3][4], ' ', numbs[4][4], ' ', numbs[5][4], ' ', numbs[6][4], ' ', numbs[7][4])
    print(numbs[0][5], ' ', numbs[1][5], ' ', numbs[2][5], ' ', numbs[3][5], ' ', numbs[4][5], ' ', numbs[5][5], ' ', numbs[6][5], ' ', numbs[7][5])
    print(numbs[0][6], ' ', numbs[1][6], ' ', numbs[2][6], ' ', numbs[3][6], ' ', numbs[4][6], ' ', numbs[5][6], ' ', numbs[6][6], ' ', numbs[7][6])
    print(numbs[0][7], ' ', numbs[1][7], ' ', numbs[2][7], ' ', numbs[3][7], ' ', numbs[4][7], ' ', numbs[5][7], ' ', numbs[6][7], ' ', numbs[7][7])
    print(numbs[0][8], ' ', numbs[1][8], ' ', numbs[2][8], ' ', numbs[3][8], ' ', numbs[4][8], ' ', numbs[5][8], ' ', numbs[6][8], ' ', numbs[7][8])

def clear_screen():
  if os.name == 'posix': #MacOs/Unix/Linux/BSD/etc
    os.system('clear')
  elif os.name in ('nt', 'dos', 'ce'): #DOS/Windows
    os.system('cls')

def clock():
    while True:
        time.sleep(1.0)
        clear_screen()
        dtn1 = datetime.datetime.now()
        str_dtn1 = dtn1.strftime("%H:%M:%S")
        numbers_for_clock(str_dtn1)
        time.sleep(1.0)
        clear_screen()
        dtn2 = datetime.datetime.now()
        str_dtn2 = dtn2.strftime("%H_%M_%S")
        numbers_for_clock(str_dtn2)

clock()
