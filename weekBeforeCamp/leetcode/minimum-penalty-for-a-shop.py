class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr_penalty = customers.count('Y')
        min_penalty = curr_penalty
        min_i = 0

        for i, is_customer in enumerate(customers):
            if is_customer == 'Y':
                curr_penalty -= 1
            else:
                curr_penalty += 1
            
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                min_i = i + 1
            
        
        return min_i
