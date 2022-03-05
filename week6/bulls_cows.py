class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        i = b = c = 0
        l = len(secret)
        secret = list(secret)
        guess = list(guess)
        while i < l:
            if secret[i] == guess[i]:
                b += 1
                secret.pop(i)
                guess.pop(i)
                l -= 1
            else:
                i += 1
        i = 0
        #print(guess, secret)
        while i < l:
            if guess[i] in secret:
                ind = secret.index(guess[i])
                guess[i] = 'x'
                secret[ind] = 'x'
                c += 1
                #print(secret, guess)
                
            i+=1
                
            
            
        
        return "{}A{}B".format(b,c)
