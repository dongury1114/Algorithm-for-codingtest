function solution(s) {
    let answer = "";
    for (let x of s) {
        answer += x.toUpperCase()
    }
    return answer
}


let input = "itsTIMEtoSTUdy"
console.log(solution(input));