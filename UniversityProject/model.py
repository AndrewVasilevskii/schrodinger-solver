from enum import Enum
from modelWithParameters import ModelWithParameters
class DonorNumber(Enum):
    zeroDonors = "0"
    oneDonor = "1"
    twoDonors = "2"

class GateNumber(Enum):
    zeroGates = "0"
    oneGate = "1"
    twoGates = "2"
    threeGates = "3"

class GateShape(Enum):
    disc = "Disc"
    strip = "Strip"
    rectangle = "Rectangle"

class Electron(Enum):
    oneElectron = 0
    twoElectrons = 1

    def GetElectronNumber(self):
        return self.value + 1

class GroundedShield(Enum):
    enabledShield = True
    disabledShield = False

class Model:
    parameters = ModelWithParameters()
    def __init__(self,
                 donorNumber: DonorNumber = DonorNumber.zeroDonors,
                 gateNumber: GateNumber = GateNumber.oneGate,
                 gateShape: GateShape = GateShape.disc,
                 electron: Electron = Electron.oneElectron,
                 groundedShield: GroundedShield = GroundedShield.disabledShield):

        self.donorNumber = str(donorNumber.value)
        self.gateNumber = str(gateNumber.value)
        self.gateShape = gateShape.value
        self.electronNumber = electron.GetElectronNumber()
        self.electronNumberIndex = electron.value
        self.groundedShield = groundedShield.value

    def __str__(self):
        return f"Number of donors: {self.donorNumber}\n" \
               f"Number of gates: {self.gateNumber}\n" \
               f"Gate shape: {self.gateShape}\n" \
               f"Number of electrons: {self.electronNumber}\n" \
               f"Grounded shield enabled: {self.groundedShield}"

    def __eq__(self, other):
        if self.donorNumber == other.donorNumber and\
            self.gateNumber == other.gateNumber and\
            self.gateShape == other.gateShape and\
            self.electronNumber == other.electronNumber and\
            self.electronNumberIndex == other.electronNumberIndex and\
            self.groundedShield == other.groundedShield:
            return True
        else:
            return False

    @property
    def ModelName(self):
        gateShape = f"__{self.gateShape[:2].lower()}" if int(self.gateNumber) > 0 else ""
        name = f"d_{self.donorNumber}__g_{self.gateNumber}{gateShape}__e_{self.electronNumber}__gs_{str(self.groundedShield)[:1].lower()}"
        return name