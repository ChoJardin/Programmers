// [문제 링크]: https://leetcode.com/problems/break-a-palindrome/submissions/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1: 
            return "" 
        
        if palindrome.count('a') == len(palindrome): 
            return palindrome[:-1] + 'b'
        
        for i in range(len(palindrome)): 
            if palindrome[i] != 'a':
                if len(palindrome) // 2 == i: 
                    continue 

                return palindrome[:i] + 'a' + palindrome[i+1:]  
        
        return palindrome[:-1] + 'b'
        
    
        

        