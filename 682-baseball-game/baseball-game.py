class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op.isnumeric():
                record.append(int(op)) 
            elif op[0] == '-':
                if op[1:].isdigit():
                    record.append(int(op)) 
            elif op == 'C':
                record.pop()
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == '+':
                record.append(record[-1] + record[-2])

        return sum(record)

