def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a,2)
        decimal_b = int(b,2)
        add=decimal_a+decimal_b
        return bin(add).replace("0b","")
