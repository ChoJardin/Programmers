// [문제 링크]: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

from functools import reduce

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        buttons = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], 
                   '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], 
                   '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        def get_strings(str1, str2): 
            ans = []
            for i in range(len(str1)): 
                for j in range(len(str2)): 
                    ans.append(str1[i] + str2[j])
            
            return ans
        
        
        if not digits: 
            return [] 
        
        digits_left = digits[1:]
        
        cur_ans = buttons[digits[0]]
        
        while digits_left: 
            cur_ans = get_strings(cur_ans, buttons[digits_left[0]])
            
            digits_left = digits_left[1:]
            
        return cur_ans
        
        
            