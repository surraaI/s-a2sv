class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        check ={}
        ans=[]
        for domain in cpdomains:
            s=domain.split(" ")
            t=s[1].split(".")
            for i in range(len(t)):
                check['.'.join(t[i:])]=check.get('.'.join(t[i:]),0)+int(s[0])

        for key,value in check.items():
            a=str(value)+" "+str(key)
            ans.append(a)
        return ans
