function solution(s) {
    let answer = 0;
    let searchChar = "a";
    for (let x of s) {
        if (x === searchChar) answer++
    }
    return answer
}

let input = "aaabbbaaabababaaaabaa"
console.log(solution(input));
