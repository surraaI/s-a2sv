class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)
        folders = []
        ans = []
        for i in range(len(paths)):
            folders.append(paths[i].split())
        
        for folder in folders:
            for fil in range(1, len(folder)):
                temp = folder[fil].split('(')
                files[temp[1][:-1]] += [folder[0] +'/'+temp[0]] 
            
        for i in files:
            if len(files[i])>1:
                ans.append(files[i])
        return ans
        
        
    
        
            
        

        