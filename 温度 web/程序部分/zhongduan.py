from microbit import *import ObloqIP="192.168.1.103"    #Web服务器的地址PORT="8088"           #Web服务器的端口SSID="littlefish"             #Wi-Fi的SSIDPASSWORD="lzy060625#"   #Wi-Fi的密码uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=pin2, rx=pin1)while Obloq.connectWifi(SSID,PASSWORD,10000) != True:     display.show(".")display.scroll(Obloq.ifconfig())Obloq.httpConfig(IP,PORT) while True:      temp=round((pin0.read_analog()/1024)*3000/10.24,1)       errno,resp=Obloq.get("input?id=1&val="+str(temp),10000)       if errno == 200:            display.show(str(resp))        print("resp",resp)                  else:            display.show(str(errno))        print("erron",errno)       sleep(1000*10)