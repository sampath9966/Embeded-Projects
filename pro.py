import serial
import time
import lcd
import math
import string
import RPi.GPIO as GPIO
import gsm
import os
import mcp3202


##### INITIALIZATION



gsm.Gsminit()
lcd.lcd_init()




lcd.stringlcd(0xC0,"welcome")
default_port='/dev/ttyUSB0'
#
#configure IO ports
act1=7
act2=5
act3=3
act4=11
GPIO.setup(act1,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act2,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act3,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act4,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(act1,GPIO.OUT)
GPIO.setup(act2,GPIO.OUT)
GPIO.setup(act3,GPIO.OUT)
GPIO.setup(act4,GPIO.OUT)
''' DO NOT DISTURB THE BELLOW CODE
        ***********IT'S OUTPUT WILL BE IN yaw,pitch,roll************
      '''
number = "9133050069"##GSM NUMBER TO TO THE GURDIAN
count =0
time.sleep(0)
sleep=0
def action1():
    if GPIO.input(act1):        
        GPIO.output(act1,False)
        gsm.Sendmsg(number,"act1 OFF")
        os.system('mpg321 1.mp3 &')
        print ("act1 false")
        ser.flushInput()
                                        
    elif act1 != 1:        
        GPIO.output(act1,True)
        gsm.Sendmsg(number,"act1 ON")
        os.system('mpg321 1.mp3 &')
        print("act1 true")
        ser.flushInput()
        
def action2():
    if GPIO.input(act2):        
        GPIO.output(act2,False)
        gsm.Sendmsg(number,"act2 OFF")
        print ("act2 false")
        ser.flushInput()
        
    elif act2 != 1:
        GPIO.output(act2,True)
        gsm.Sendmsg(number,"act2 ON")
        print("act2 true")
        ser.flushInput()
def action3():
    if GPIO.input(act3):        
        GPIO.output(act3,False)
        gsm.Sendmsg(number,"act3 OFF")
        print ("act3 false")
        ser.flushInput()
        
    elif act3 != 1:
        GPIO.output(act3,True)
        gsm.Sendmsg(number,"act3 ON")
        print("act3 true")
        ser.flushInput()

def action4():
    if GPIO.input(act4):        
        GPIO.output(act4,False)
        gsm.Sendmsg(number,"act4 OFF")
        print ("act4 false")
        ser.flushInput()
        
    elif act4 != 1:
        GPIO.output(act4,True)
        gsm.Sendmsg(number,"act4 ON")
        print("act4 true")
        ser.flushInput()





################################################################################
        ###########################################################

def function1():
    
    r01 = 0        
    p01= 0
    p02 =0
    rfun1 =0
    pfun1=0


    while (1):
        

        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        print("In Function1")
    
            
    
        if len(words) > 2:                                          
                    try:
                        pfun1 = -float(words[1])*grad2rad
                        rfun1 = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print (rfun1,pfun1,p2)

        
        if (rfun1 > 0.5):
            r01 +=1
        else:
            r01=0   
        
        if (pfun1 > 0.5):
            p01 +=1
        else:
            p01=0
        if (pfun1 < -0.5):
            p02 +=1
        else:
            p02=0
        if r01 > 3:
            r01=0
            action1()
            main()

        if (p01 >= 3):
            p01 = 0
            print ("fun2")
            lcd.stringlcd(0xC0,"In Function2")
            function2()
        if (p02 >= 3):
            p02 = 0
            print ("fun3")
            lcd.stringlcd(0xC0,"In Function8")
            function8()
        ser.flushInput()
        time.sleep(1)
       




def function2():
    

    r11 = 0        
    p11= 0
    p12 =0
    rfun2 =0
    pfun2=0


    while (1):
        

        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        
    
            
    
        if len(words) > 2:                                          
                    try:
                        pfun2 = -float(words[1])*grad2rad
                        rfun2 = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print ("2",rfun2,pfun2,p2)
        
        if (rfun2 > 0.5):
            r11 +=1
        else:
            r11=0   
        
        if (pfun2 > 0.5):
            p11 +=1
        else:
            p11=0
        if (pfun2 < -0.5):
            p12 +=1
        else:
            p12=0
        if r11 > 3:
            r11=0
            action2()         

        if (p11 >= 3):
            p11 = 0
            print ("fun3")
            lcd.stringlcd(0xC0,"Changed to Function3")
            function3()
        if (p12 >= 3):
            p12 = 0
            print ("fun1")
            lcd.stringlcd(0xC0,"Changed to Function1")
            function1()
        ser.flushInput()
        time.sleep(1)
       


    
def function3():
    r21 = 0        
    p21= 0
    p22 =0
    rfun3 =0
    pfun3=0


    while (1):
        

        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        
    
            
    
        if len(words) > 2:                                          
                    try:
                        pfun3 = -float(words[1])*grad2rad
                        rfun3 = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print ("3",rfun3,pfun3,p2)
        
        if (rfun3 > 0.5):
            r21 +=1
        else:
            r21=0   
        
        if (pfun3 > 0.5):
            p21 +=1
        else:
            p21=0
        if (pfun3 < -0.5):
            p22 +=1
        else:
            p22=0
        if r21 > 3:
            r21=0
            
            action3()

        if (p21 >= 3):
            p21 = 0
            print ("fun4")
            lcd.stringlcd(0xC0,"Changed to Function4")
            function4()
        if (p22 >= 3):
            p22 = 0
            print ("fun2")
            lcd.stringlcd(0xC0,"Changed to Function2")
            function2()
        ser.flushInput()
        time.sleep(1)


def function4():
    r31 = 0        
    p31= 0
    p32 =0
    rfun4 =0
    pfun4=0


    while (1):
        

        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        
    
            
    
        if len(words) > 2:                                          
                    try:
                        pfun4 = -float(words[1])*grad2rad
                        rfun4 = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print ("4",rfun4,pfun4,p2)
        
        if (rfun4 > 0.5):
            r31 +=1
        else:
            r31=0   
        
        if (pfun4 > 0.5):
            p31 +=1
        else:
            p31=0
        if (pfun4 < -0.5):
            p32 +=1
        else:
            p32=0
        if r31 > 3:
            r31=0            
            action4()

        if (p31 >= 3):
            p31 = 0
            print ("fun5")
            lcd.stringlcd(0xC0,"Changed to Function5")
            function5()
        if (p32 >= 3):
            p32 = 0
            print ("fun3")
            lcd.stringlcd(0xC0,"Changed to Function3")
            function3()
        ser.flushInput()
        time.sleep(1)


def function5():
    r41 = 0        
    p41= 0
    p42 =0
    rfun5 =0
    pfun5=0


    while (1):
        

        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        
    
            
    
        if len(words) > 2:                                          
                    try:
                        pfun5 = -float(words[1])*grad2rad
                        rfun5 = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print ("5",rfun5,pfun5,p2)
        
        if (rfun5 > 0.5):
            r41 +=1
        else:
            r41=0   
        
        if (pfun5 > 0.5):
            p41 +=1
        else:
            p41=0
        if (pfun5 < -0.5):
            p42 +=1
        else:
            p42=0
        if r41 > 3:
            r41=0
            print ("Doctor")
            gsm.Sendmsg(number,"Doctor")

        if (p41 >= 3):
            p41 = 0
            print ("fun6")
            lcd.stringlcd(0xC0,"Changed to Function6")
            function6()
        if (p42 >= 3):
            p42 = 0
            print ("fun4")
            lcd.stringlcd(0xC0,"Changed to Function4")
            function4()
        ser.flushInput()
        time.sleep(1)

def function6():
    r51 = 0        
    p51= 0
    p52 =0
    rfun6 =0
    pfun6=0


    while (1):
        

        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        
    
            
    
        if len(words) > 2:                                          
                    try:
                        pfun6 = -float(words[1])*grad2rad
                        rfun6 = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print ("6",rfun6,pfun6,p2)
        
        if (rfun6 > 0.5):
            r51 +=1
        else:
            r51=0   
        
        if (pfun6 > 0.5):
            p51 +=1
        else:
            p51=0
        if (pfun6 < -0.5):
            p52 +=1
        else:
            p52=0
        if r51 > 3:
            r51=0
            print ("Medicine")
            gsm.Sendmsg(number,"Medicine")
            lcd.stringlcd(0xC0,"Medicine")

        if (p51 >= 3):
            p51 = 0
            print ("fun7")
            lcd.stringlcd(0xC0,"Changed to Function7")
            function7()
        if (p52 >= 3):
            p52 = 0
            print ("fun5")
            lcd.stringlcd(0xC0,"Changed to Function5")
            function5()
        ser.flushInput()
        time.sleep(1)


def function7():
    r61 = 0        
    p61= 0
    p62 =0
    rfun7 =0
    pfun7=0


    while (1):
        

        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        
    
            
    
        if len(words) > 2:                                          
                    try:
                        pfun7 = -float(words[1])*grad2rad
                        rfun7 = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print ("7",rfun7,pfun7,p2)
        
        if (rfun7 > 0.5):
            r61 +=1
        else:
            r61=0   
        
        if (pfun7 > 0.5):
            p61 +=1
        else:
            p61=0
        if (pfun7 < -0.5):
            p62 +=1
        else:
            p62=0
        if r61 > 3:
            r61=0
            print ("Water")
            lcd.stringlcd(0xC0,"Water")
            gsm.Sendmsg(number,"Water")

        if (p61 >= 3):
            p61 = 0
            print ("fun8")
            lcd.stringlcd(0xC0,"Changed to Function8")
            function8()
        if (p62 >= 3):
            p62 = 0
            print ("fun6")
            lcd.stringlcd(0xC0,"Changed to Function6")
            function6()
        ser.flushInput()
        time.sleep(1)

def function8():
    r71 = 0        
    p71= 0
    p72 =0
    rfun8 =0
    pfun8=0


    while (1):
        

        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        
    
            
    
        if len(words) > 2:                                          
                    try:
                        pfun8 = -float(words[1])*grad2rad
                        rfun8 = -float(words[2])*grad2rad                                                             
                    except Exception as e:                   
                        print e
        
        print ("8",rfun8,pfun8,p2)
        
        if (rfun8 > 0.5):
            r71 +=1
        else:
            r71=0   
        
        if (pfun8 > 0.5):
            p71 +=1
        else:
            p71=0
        if (pfun8 < -0.5):
            p72 +=1
        else:
            p72=0
        if r71 > 3:
            r71=0
            print ("Food")
            lcd.stringlcd(0xC0,"FOOD")
            gsm.Sendmsg(number,"FOOD")
        if (p71 >= 3):
            p71 = 0
            print ("fun1")
            lcd.stringlcd(0xC0,"Changed to Function1")
            function1()
        if (p72 >= 3):
            p72 = 0
            print ("fun7")
            lcd.stringlcd(0xC0,"Changed to Function7")
            function7()
        ser.flushInput()
        time.sleep(1)

        


            #####################################################
################################################################################

                
        

roll=0
pitch=0
yaw=0        
r0=0
r1=0
r2=0
p1=0
p2=0
def main():
        global r0
        global roll
        global yaw
        global pitch                  

        print ("sam")
        if len(words) > 2:                                          
                try:
                    pitch = -float(words[1])*grad2rad
                    roll = -float(words[2])*grad2rad                                                             
                except Exception as e:                   
                    print e
       
        if (roll > 1.0):
            r0 += 1
        else:
            r0 =0
        if r0 >=4:
            r0= 0
            r1=0
            p1=0
            p2=0            
            ser.flushInput()
            time.sleep(1)
            function1()
        
        lcd.stringlcd(0xC0,"P:"+str(r0)+str(roll))
        time.sleep(1)
        ser.flushInput()



################################################################################
        ###########################################################
                ##########################################

                                    
    # Check your COM port and baud rate
#ser = serial.Serial(port=default_port,baudrate=9600, timeout=1)
ser = serial.Serial('/dev/ttyUSB0', 9600)
#gsmser = serial.Serial('/dev/ttyAMA0',9600)
# To start display angle and sensor reading in text

ser.write('#ox' + chr(13))
#Pi value
grad2rad = 3.141592/180.0


"""START THE MAIN PROGRAM"""
while (1):    
    
        line = ser.readline()
        line = line.replace("#YPR=","")
        line = line.replace("#YPRAMG=","")   # Delete "#YPR="
        #f.write(line)                     # Write to the output log file
        words = string.split(line[4:],",")
        if __name__ == "__main__":
                main()
            

    
