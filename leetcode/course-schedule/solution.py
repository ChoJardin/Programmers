// [문제 링크]: https://leetcode.com/problems/course-schedule/submissions/

from collections import deque 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 진입차수 기록할 리스트 
        linked = [[] for _ in range(numCourses)]
        # 들은 수업 체크 
        taken = [ False for _ in range(numCourses) ]
        
        for each in prerequisites: 
            linked[each[0]].append(each[1])
        
        # 진입차수 숫자로 들고 있겠다.. 
        linked_cnt = [len(linked[i]) for i in range(numCourses)]
        
        queue = deque()
        for idx, each in enumerate(linked_cnt): 
            if not each: 
                queue.append(idx)
                taken[idx] = True 
                
        while queue: 
            course = queue.popleft() 
            
            for idx, pre in enumerate(linked): 
                if course in pre: 
                    pre.remove(course)
                    
                    if not pre: 
                        queue.append(idx)
                        taken[idx] = True
        
        
        if False in taken: 
            return False 
        
        return True
        
        
        
        
        
            
        
        
        