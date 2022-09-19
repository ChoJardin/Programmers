// [문제 링크]: https://leetcode.com/problems/number-of-provinces/submissions/

from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        
        provinces = 0 
        
        # 방문체크
        visited = [False for _ in range(n)]
        
        for i in range(n): 
            
            # 아직 방문 하지 않았으면
            if not visited[i]:
                queue = deque() 
                
                queue.append(i)
                visited[i] = True 
                
                while queue: 
                    v = queue.popleft() 
                    
                    for j in range(n):
                        if isConnected[v][j] and not visited[j]: 
                            queue.append(j)
                            visited[j] = True 
            
                provinces += 1
        
                        
        return provinces
            
        
        
        