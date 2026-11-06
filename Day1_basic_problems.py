两数相加
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1+num2
温度调节
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin=celsius+273.15
        Fahrenheit=celsius*1.80+32.00
        return[Kelvin,Fahrenheit]
最小偶倍数
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
     if n%2==0:
        return n
     else:
        return n*2   
