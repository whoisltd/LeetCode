class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A,B=0,0
        hash = Counter(secret)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                A += 1
                hash[guess[i]]-=1
                if hash[guess[i]]<0:
                    B-=1
            if secret[i]!=guess[i] and guess[i] in hash.keys():
                if hash[guess[i]]>0:
                    B+=1
                    hash[guess[i]]-=1 
        return f"{A}A{B}B"
                