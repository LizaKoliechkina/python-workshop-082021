
class Temperature:
    # dunder new - constructor, dunder __init__ is not a constructor, it just sets field values
    def __init__(self, kelvin, unit):
        self.kelvin = kelvin  # self._kelvin = kelvin in this case setter will not validate value
        self._unit = unit

    def __repr__(self):
        return f'{type(self).__name__}(kelvin={self._kelvin}, unit="{self.unit}")'

    # getters are used for formatting of return value in Python
    @property
    def kelvin(self):
        print('Getter')
        return f'{self._kelvin} K'

    # setters are used for data validation in Python
    @kelvin.setter
    def kelvin(self, value):
        if value < 0:
            raise ValueError('Too cold!')
        print('Setter')
        self._kelvin = value

    # if only getter exists for a property - read-only property
    # @property
    # def unit(self):
    #     return 'K'

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        raise AttributeError('Cannot change the unit value!')

    @property
    def celsius(self):
        return f'{self._kelvin - 273.15} C'

    @celsius.setter
    def celsius(self, value):
        self.kelvin = value + 273.15

    @property
    def fahrenheit(self):
        return f'{(self._kelvin - 273.15) * 9 / 5 + 32} F'

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.kelvin = (value - 32) * 5 / 9 + 273.15


t = Temperature(223, 'UNIT')
t.kelvin = 273
print(t.kelvin, t.celsius, t.fahrenheit)
t.celsius = 34
print(t.kelvin, t.celsius, t.fahrenheit)
t.fahrenheit = 60
print(t.kelvin, t.celsius, t.fahrenheit)
print(t.unit)
print(repr(t))
