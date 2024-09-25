class Solution:
    def fractionAddition(self, expression: str) -> str:
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        def parse_fraction(s):
            numerator, denominator = map(int, s.split('/'))
            return numerator, denominator

        
        fractions = []
        num = ''
        
        for char in expression:
            if char in '+-':
                if num:  
                    fractions.append(num)
                num = char  
            else:
                num += char
        
        
        fractions.append(num)
        
        numerator, denominator = 0, 1
        
        
        for fraction in fractions:
            frac_num, frac_den = parse_fraction(fraction)
            common_den = lcm(denominator, frac_den)
            numerator = numerator * (common_den // denominator) + frac_num * (common_den // frac_den)
            denominator = common_den
        
        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        
        if denominator == 1:
            return f"{numerator}/1"
        
        return f"{numerator}/{denominator}"
