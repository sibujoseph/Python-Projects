class Evaluate():
    
    r=False
    def isPalindrome(self, text):
        x=len(text)
        if x>0: 
            if text[0]==text[x-1]:
                text=text[1:x-1]
                self.r=True
                self.isPalindrome(text)
            else:
                self.r=False
        return self.r


if __name__ == "__main__":
    
    
    x=Evaluate()
    print(x.isPalindrome("aba"))
