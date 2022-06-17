function solution(lottos, win_nums) {
    
    let unidentified = 0;
    for (let lotto of lottos) {
        if (!+lotto) unidentified++;
        else win_nums.push(lotto)
    }
    
    const result = [...new Set(win_nums)]
​
    const max = result.length > 11 ? 6 : result.length - 5;
    const min = max + unidentified > 6 ? 6 : max + unidentified;
​
    return [max, min];
}
