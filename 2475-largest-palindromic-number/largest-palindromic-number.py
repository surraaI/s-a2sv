class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = Counter(num)
    
        first_half = []
        middle = ''
        
        # Step 2: Construct the first half of the palindrome
        for digit in range(9, -1, -1):
            d = str(digit)
            if freq[d] >= 2:
                # Add pairs of the digit to the first half
                pairs = freq[d] // 2
                # Avoid leading zeros
                if first_half or d != '0':
                    first_half.append(d * pairs)
                freq[d] -= pairs * 2
        
        # Step 3: Find the middle digit (if any)
        for digit in range(9, -1, -1):
            d = str(digit)
            if freq[d] > 0:
                middle = d
                break
        
        # Step 4: Construct the full palindrome
        first_half_str = ''.join(first_half)
        if not first_half_str and not middle:  # Only zeros
            return "0"
        
        return first_half_str + middle + first_half_str[::-1]