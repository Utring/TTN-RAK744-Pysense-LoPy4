from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))
