class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
       
        print(path)
        stack = []
        for i in path:
            if i == '..' and stack:
                stack.pop()
            elif i !='' and i != '..' and i != '.':
                stack.append('/'+i)
            
        
        
        return ''.join(stack) if stack else '/'
        
           

        