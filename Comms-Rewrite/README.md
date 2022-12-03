#Comms Rewrite

Rewritten comms code, since the old one had 95% one way integrity and about 20% two way integrity (not good)


3 step comms (Slave arduino, Master arduino, Pi)
- `MasterCode/` = code for Master Arduino
- `SlaveCode/` = code for Slave Arduino generating IMU data (90% complete)
- `SlaveFakeCode/` = code for Slave
- `toA.py` = code for RPi

2 step comms (Arduino (echos data). Pi)
- `bouncer/` = code for Arduino to "bounce"/echo back whatever it got sent by pi
- `toA.py` = code for RPi
