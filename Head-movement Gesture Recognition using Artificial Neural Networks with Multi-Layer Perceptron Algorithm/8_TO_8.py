###import
import serial
import time
import lcd

import math
import string
import RPi.GPIO as GPIO
import gsm
import os
import mcp3202
from sklearn.externals import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
import pandas as pd

##### INITIALIZATION

gsm.Gsminit()
lcd.lcd_init()
lcd.stringlcd(0x80,"Welcome")
time.sleep(1)
default_port='/dev/ttyUSB0'

    # Check your COM port and baud rate
#ser = serial.Serial(port=default_port,baudrate=9600, timeout=1)
ser1 = serial.Serial('/dev/ttyUSB0', 9600)

number = ""##GSM NUMBER TO TO THE GURDIAN
count =0
time.sleep(0)
sleep=0


#configure IO ports
act1=7
act2=5
act3=3
act4=11
act5=13
act6=15
act7=19
act8=21
buz=29
GPIO.setup(act1,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act2,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act3,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act4,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act5,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act6,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act7,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act8,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act1,GPIO.OUT)
GPIO.setup(act2,GPIO.OUT)
GPIO.setup(act3,GPIO.OUT)
GPIO.setup(act4,GPIO.OUT)
GPIO.setup(act5,GPIO.OUT)
GPIO.setup(act6,GPIO.OUT)
GPIO.setup(act7,GPIO.OUT)
GPIO.setup(act8,GPIO.OUT)
GPIO.setup(buz,GPIO.OUT)
GPIO.output(buz,False)
GPIO.output(act1,False)
GPIO.output(act2,False)
GPIO.output(act3,False)
GPIO.output(act4,False)
GPIO.output(act5,False)
GPIO.output(act6,False)
GPIO.output(act7,False)
GPIO.output(act8,False)
''' DO NOT DISTURB THE BELLOW CODE
        ***********IT'S OUTPUT WILL BE IN yaw,pitch,roll************
      '''

def action1():
    if GPIO.input(act1):        
        GPIO.output(act1,False)
        gsm.Sendmsg(number,"act1  Fan OFF")
        os.system('mpg321 FanOFF.mp3 &')
        lcd.lcd_init()
        lcd.stringlcd(0xC0,"FAN OFF")
        print ("act1 false")
        ser1.flushInput()
        DA()
                                        
    elif act1 != 1:        
        GPIO.output(act1,True)
        gsm.Sendmsg(number,"act1 Fan ON")
        os.system('mpg321 FanON.mp3 &')
        lcd.lcd_init()
        lcd.stringlcd(0xC0,"FAN ON")
        print("act1 true")
        ser1.flushInput()
        DA()
        
def action2():
    if GPIO.input(act2):        
        GPIO.output(act2,False)
        gsm.Sendmsg(number,"act2 Light OFF")
        os.system('mpg321 LightOFF.mp3 &')
        print ("act2 Light false")
        lcd.lcd_init()
        lcd.stringlcd(0xC0,"LIGHT OFF")
        ser1.flushInput()
        
    elif act2 != 1:
        GPIO.output(act2,True)
        gsm.Sendmsg(number,"act2 Light ON")
        os.system('mpg321 LightON.mp3 &') 
        lcd.lcd_init()
        lcd.stringlcd(0xC0,"LIGHT ON" )
        print("act2 Light true")
        ser1.flushInput()
        
def action3():
    if GPIO.input(act3):        
        GPIO.output(act3,False)
        gsm.Sendmsg(number,"Water")
        os.system('mpg321 water.mp3 &')
        print ("act3 false")
        ser1.flushInput()
        
    elif act3 != 1:
        GPIO.output(act3,True)
        gsm.Sendmsg(number,"Water")
        print("act3 true")
        os.system('mpg321 water.mp3 &')
        ser1.flushInput()

def action4():
    if GPIO.input(act4):        
        GPIO.output(act4,False)
        gsm.Sendmsg(number,"Food")
        print ("act4 false")
        os.system('mpg321 Food.mp3 &')
        ser1.flushInput()
        
    elif act4 != 1:
        GPIO.output(act4,True)
        gsm.Sendmsg(number,"Food")
        print("act4 true")
        os.system('mpg321 Food.mp3 &')
        ser1.flushInput()

def action5():
    if GPIO.input(act5):        
        GPIO.output(act5,False)
        gsm.Sendmsg(number,"Toilet")
        os.system('mpg321 Toilet.mp3 &')
        lcd.lcd_init()
        lcd.stringlcd(0xC0,"Toilet")
        print ("act5 false")
        ser1.flushInput()
                                        
    elif act5 != 1:        
        GPIO.output(act5,True)
        gsm.Sendmsg(number,"Toilet")
        os.system('mpg321 Toilet.mp3 &')
        lcd.lcd_init()
        lcd.stringlcd(0xC0,"Toilet")
        print("act5 true")
        ser1.flushInput()
        
def action6():
    if GPIO.input(act6):        
        GPIO.output(act6,False)
        gsm.Sendmsg(number,"Medicine")
        print ("act6 Medicine false")
        os.system('mpg321 Medicine.mp3 &')
        lcd.lcd_init()
        lcd.stringlcd(0xC0,"Medicine")
        ser1.flushInput()
        
    elif act6 != 1:
        GPIO.output(act6,True)
        gsm.Sendmsg(number,"Medicine")
        os.system('mpg321 Medicine.mp3 &') 
        lcd.lcd_init()
        lcd.stringlcd(0xC0,"Medicine" )
        print("act6 Medicine true")
        ser1.flushInput()
        
def action7():
    if GPIO.input(act7):        
        GPIO.output(act7,False)
        gsm.Sendmsg(number,"Doctor")
        print ("act7 false")
        os.system('mpg321 Doctor.mp3 &') 
        ser1.flushInput()
        
    elif act7 != 1:
        GPIO.output(act7,True)
        gsm.Sendmsg(number,"Doctor")
        print("act7 true")
        os.system('mpg321 Doctor.mp3 &') 
        ser1.flushInput()

def action8():
    if GPIO.input(act8):        
        GPIO.output(act8,False)
        gsm.Sendmsg(number,"Emergency")
        print ("act8 false")
        os.system('mpg321 Emergency.mp3 &')
        DA()
        ser1.flushInput()
        
    elif act8 != 1:
        GPIO.output(act8,True)
        gsm.Sendmsg(number,"Emergency")
        print("act8 true")
        os.system('mpg321 Emergency.mp3 &') 
        ser1.flushInput()
        DA()




################################################################################
        ###########################################################



'''
MLPClassifier
'''
''''
##df = pd.read_csv('train_300.txt')#Filename
##df1 = df.replace(np.nan, '', regex=True)
###print (df)
###define X & Y
####X = np.array(df1.drop(['position'], 1))
####y = np.asarray(df1['position'] )#dtype = '|S6'
####X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state = 5)
####
##clf = MLPClassifier(activation='logistic',solver='sgd', max_iter=200, hidden_layer_sizes=(900,90,),random_state=1)       


clf = joblib.load(mlp_100_78.sav)
#clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print ("Accuracy:"+str(accuracy)+"%")     
####Stable the sensor
'''
lcd.stringlcd(0x80,"Stable the sensor")         
time.sleep(3)
while(1):
    x = ser1.read(1)
    if(x == '*'):
        y = ser1.read(1)
        lcd.stringlcd(0x80,"L:"+str(y))
        time.sleep(0.5)
        if(y == '0'):
            count = count + 1
        else:
            count = 0
        if(count > 10):
            count = 0
            break
        ser1.flushInput()
lcd.stringlcd(0x80,"Stabled")           
time.sleep(3)
ser1.flushInput()
        
        
        
########################################################################################################

def main():
    dar = 0
    dal = 0
    darl = 0
    daroll = 0
    dap = 0
    GPIO.output(buz,True)
    time.sleep(1.5)
    GPIO.output(buz,False)
   
        
    while (1):
        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")                      # Delete "#YPR="
        #f.write(line)                                          # Write to the output log file
        words = string.split(line[4:],",")
        
    
            
    
        if len(words) > 2:                                          
                    try:
                        dap = -float(words[1])*grad2rad
                        daroll = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print dap
        if (daroll > 0.5):
            darl += 1
        else:
            darl = 0
        if (dap > 0.5):
            dar +=1
        else:
            dar=0
        
        
##        if (dap < -0.5):
##            
##            dal +=1
##        else:
##            dal=0
##        if (dar > 2):
##            print ("fun1")
##            function1()
##        if (dal > 2):
##            print("fun5")
##            function5()
##        ser.flushInput()
##        time.sleep(1)

        if (darl > 5):
            main()
            print ("STABLED")

#Main function

def Activities():
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    p6=0
    p7=0
    p8=0
    action3()
    sleep = 0
    while(1):
        
        x = ser1.read(1)
        if(x == '*'):
            line = ser1.readline()
            print (line)
            line = line.replace("#YPR=","")
            
            line = line.replace("#YPRAMG=","")
            # Delete "#YPR="
            line = line.rstrip()
           
            raw_ypr = line.split(",")
            if len(raw_ypr)>2:
                try:
                    raw_y = raw_ypr[0]
                    raw_p = raw_ypr[1]
                    raw_r = raw_ypr[1]
                except Exception as e:
                    print e
                        
            #print ('yaw='+str(raw_y)+'\t'+'pitch='+str(raw_p)+'\t'+'raoll='+str(raw_r))
            live_data = np.array([raw_p,raw_r])
            live_data = live_data.reshape(1, 2)
           
            

            prediction = clf.predict(live_data)
            print (prediction)
            

           
            clf = joblib.load("filename_model.sav")
            line = ser1.readline()
            print (line)
            line = line.replace("#YPR=","")

            line = line.replace("#YPRAMG=","")
            # Delete "#YPR="
            line = line.rstrip()

            raw_ypr = line.split(",")
            if len(raw_ypr)>2:
                    try:
                        raw_y = raw_ypr[0]
                        raw_p = raw_ypr[1]
                        raw_r = raw_ypr[1]
                    except Exception as e:
                        print e
                    
            #print ('yaw='+str(raw_y)+'\t'+'pitch='+str(raw_p)+'\t'+'raoll='+str(raw_r))
            live_data = np.array([raw_p,raw_r])
            live_data = live_data.reshape(1, 2)



            prediction = clf.predict(live_data)
            print (prediction)
            y =''.join(prediction)
            
            
            
            #kNNpredict()
            
            print (y)
                    
                  
            if(y == '0'):
                if(sleep == 0):
                    lcd.stringlcd(0x80,"Normal")
            else:
                if(sleep == 0):
                    lcd.stringlcd(0x80,"Position: "+str(y))
                    
                    time.sleep(1)
                    
            if(y == '1.0'):
                p1 += 1
            else:
                p1 = 0  
            if(y == '2.0'):
                p2 += 1
            else:
                x2 = 0
##            if(y == '3.0'):
##                p3 += 1
##            else:
##                x3 = 0
            if(y == '4.0'):
                p4 += 1
            else:
                x4 = 0  
            if(y == '5.0'):
                p5 += 1
            else:
                x5 = 0  
            if(y == '6.0'):
                p6 += 1
            else:
                x6 = 0
            if(y == '7.0'):
                p7 += 1
            else:
                x7 = 0
            if(y == '8.0'):
                p8 += 1
            else:
                x8 = 0
            
                
                    
                    
                    
                    
                    
        ####################################################
        #####______________ACTIVITIES________###############
        
            
        
            #######_____activity1   
            if(p1 >= 5):
                p1 = 0
                sleep = 0
                action1()
                lcd.stringlcd(0x80,"Act1")
                time.sleep(2)
                ser1.flushInput()
            if(sleep == 1):
                continue
            ########_____activity2
            if(p2 >= 5):
                p2 = 0
                sleep = 0
                action2()
                lcd.stringlcd(0x80,"Act2")
                time.sleep(2)
                ser1.flushInput()
            if(sleep == 1):
                 continue
            ########_____activity3
            if(p3 >= 5):
                p3 = 0            
                sleep = 0
                action3()
                lcd.stringlcd(0x80,"Act3")
                time.sleep(2)
                ser1.flushInput()
            if(sleep == 1):
                continue    
            #######_____activity4   
            if(p4 >= 5):
                p4 = 0
                sleep = 0
                action4()
                lcd.stringlcd(0x80,"Act14")
                time.sleep(2)
                ser1.flushInput()
            if(sleep == 1):
                continue
           ########_____activity5
            if(p5 >= 5):
                p5 = 0
                sleep = 0
                action5()
                lcd.stringlcd(0x80,"Act5")
                time.sleep(2)
                ser1.flushInput()
            if(sleep == 1):
                continue 
          ########_____activity6      
            if(p6 >= 5):
                p6 = 0
                sleep = 0
                action6()
                lcd.stringlcd(0x80,"Act6")
                time.sleep(2)
                ser1.flushInput()
            if(sleep == 1):
                continue
          ########_____activity7      
            if(p7 >= 5):
                
                p7 = 0
                sleep = 0
                action7()
                lcd.stringlcd(0x80,"Act7")
                time.sleep(2)
                ser1.flushInput()
            if(sleep == 1):
                
                continue
        ########_____activity8      
            if(p8 >= 5):
                p8 = 0
                sleep = 0
                action8()
                lcd.stringlcd(0x80,"Act8")
                time.sleep(2)
                ser1.flushInput()
            if(sleep == 1):
                continue
            
__init__=main()
                    
                    
                
                

