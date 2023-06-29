import struct
import binascii
import time
from LoRaWAN import lora

lora = lora()

DEV_EUI = "70B3D57ED005F024"
APP_EUI = "0000000000001234"
APP_KEY = "6DBE97BDDB268214BE97A11AAE40FCCA"

lora.configure(DEV_EUI, APP_EUI, APP_KEY)

lora.startJoin()
print("Start Join.....")
while not lora.checkJoinStatus():
  print("Joining....")
  time.sleep(1)
print("Join success!")