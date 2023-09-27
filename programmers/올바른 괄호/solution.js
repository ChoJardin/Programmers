// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12909

function solution(s){
    var answer = true;

    const stack = []; 
    
    for (let i=0; i < s.length; i++) {
        
        if (s[i] === '(') {
            stack.push('(')
        } else {
            
            if (stack.pop() !== '(') {
                answer = false; 
                break;
            }
        }
    }
    
    if (stack.length) answer = false;

    return answer;
}