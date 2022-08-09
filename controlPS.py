import pyvisa
from time import sleep
class BaseScan:
    def __init__(self):
        self.resource_manager = pyvisa.ResourceManager('@py')
    def select_resources(self,startline_char='\n',endline_char='\n',preselect_resource=""):
        if preselect_resource == "":
            lor = self.resource_manager.list_resources()
            print(lor)
            print("Type number of insturment you want to control")
            TGT_rs =int(input())
            self.inst = self.resource_manager.open_resource(lor[TGT_rs])
        else:
            self.inst = self.resource_manager.open_resource(preselect_resource)
        self.inst.write_termination = startline_char
        self.inst.read_termination = endline_char
        self.inst.query_delay = 0.1
        return None
class SiglentPS_SPD3303XE(BaseScan):
    def __init__(self):
        BaseScan.__init__(self)
        self.startline_char = '\n'
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
        self.startline_char = '\n'
        self.endline_char = '\n'
    def forceTrigger(self):
        self.inst.write(':SINGle')
        self.inst.write(':TFORce')
        return None
class Keithly_2410(BaseScan):
    def __init__(self):
        self.startline_char = '\r'
        self.endline_char = '\r'
        BaseScan.__init__(self)
        self.select_resources(startline_char=self.startline_char,
                              endline_char=self.endline_char,
                              preselect_resource="ASRL/dev/ttyUSB0::INSTR")
    def getVoltageReading(self):
        self.inst.write('SOUR1:CLE:AUTO ON') #Source1 Clear Auto On
        self.inst.write(':FORM:ELEM VOLT')
        asdf = self.inst.query(':MEAS:VOLT?')
        return float(asdf)
