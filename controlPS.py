import pyvisa
from time import sleep
class BaseScan:
    def __init__(self):
        self.resource_manager = pyvisa.ResourceManager('@py')
    def select_resources(self):
        lor = self.resource_manager.list_resources()
        print(lor)
        print("Type number of insturment you want to control")
        TGT_rs =int(input())
        self.inst = self.resource_manager.open_resource(lor[TGT_rs])
        self.inst.write_termination = self.startline_char
        self.inst.read_termination = self.endline_char
        self.inst.query_delay = 0.1
        return None
class SiglentPS_SPD3303XE(BaseScan):
    def __init__(self):
        BaseScan.__init__()
        self.starline_char = '\n'
        self.endline_char = '\n'

    def setAllChannelOn(self):
        self.inst.write('OUTP CH1,ON')
        sleep(0.1)
        self.inst.write('OUTP CH2,ON')
        sleep(0.1)
        self.inst.write('OUTP CH3,ON')
        sleep(0.1)
        return None
    def setAllChannelOff(self):
        self.inst.write('OUTP CH1,OFF')
        sleep(0.1)
        self.inst.write('OUTP CH2,OFF')
        sleep(0.1)
        self.inst.write('OUTP CH3,OFF')
        sleep(0.1)
        return None
    def setCh1Volt(self,tgtvoltage):
        self.inst.write('CH1:VOLT ' + str(tgtvoltage))
        sleep(0.1)
        return None
    def setCh2Volt(self,tgtvoltage):
        self.inst.write('CH2:VOLT ' + str(tgtvoltage))
        sleep(0.1)
        return None
    def setCh1Curr(self,tgtcurrent):
        self.inst.write('CH1:CURR ' + str(tgtcurrent))
        sleep(0.1)
        return None
    def setCh2Curr(self,tgtcurrent):
        self.inst.write('CH2:CURR ' + str(tgtcurrent)) 
        sleep(0.1)
        return None

class Rigol_DS1202ZE(BaseScan):
    def __init__(self):
        BaseScan.__init__(self)
        self.starline_char = '\n'
        self.endline_char = '\n'
    def forceTrigger(self):
        self.inst.write(':SINGle')
        self.inst.write(':TFORce')
        return None
