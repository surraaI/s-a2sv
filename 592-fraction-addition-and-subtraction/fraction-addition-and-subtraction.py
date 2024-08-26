class Solution:
    def fractionAddition(self, expression: str) -> str:
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        def parse_fraction(s):
            numerator, denominator = map(int, s.split('/'))
            return numerator, denominator

        # List to store the fractions
        fractions = []
        num = ''
        
        # Parse the expression into fractions
        for char in expression:
            if char in '+-':
                if num:  # If num is not empty, append it to the fractions list
                    fractions.append(num)
                num = char  # Start a new fraction
            else:
                num += char
        
        # Append the last fraction
        fractions.append(num)
        
        # Initialize the numerator and denominator of the result fraction
        numerator, denominator = 0, 1
        
        # Perform the addition/subtraction
        for fraction in fractions:
            frac_num, frac_den = parse_fraction(fraction)
            common_den = lcm(denominator, frac_den)
            numerator = numerator * (common_den // denominator) + frac_num * (common_den // frac_den)
            denominator = common_den
        
        # Simplify the fraction by dividing by the GCD
        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        # If the denominator is 1, return the result as `numerator/1`
        if denominator == 1:
            return f"{numerator}/1"
        
        return f"{numerator}/{denominator}"
