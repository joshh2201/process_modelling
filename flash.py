import math

class Component:
    """
    Represents a pure component within the flash mixture.
    """
    def __init__(self, A, B, C, temperature=None, vap_pressure=None):
        # Antoine equation constants
        self.A = A
        self.B = B
        self.C = C
        self.temperature = temperature if temperature else self.antoine_equation(vap_pressure=vap_pressure)
        self.vap_pressure = vap_pressure if vap_pressure else self.antoine_equation(temperature=temperature)

    def antoine_equation(self, temperature=None, vap_pressure=None):
        """
        Antoine equation to calculate temperature or vapour pressure of the pure component.

        Args:
            temperature (float): temperature of the pure component in K
            vap_pressure (float): vapour pressure of the pure component in mmHg
        Returns:
            float: temperature in K or vapour pressure in mmHg depending on method input
        """
        if temperature:
            return math.exp(self.A - self.B / (self.C + temperature))
        return self.B /(self.A - math.log(vap_pressure)) - self.C

benzene = Component(15.9008,2788.51,-52.34,temperature=385)
print(benzene.vap_pressure)

o_xylene = Component(16.1156,3395.57,-59.44,vap_pressure=356.5)
print(o_xylene.temperature)