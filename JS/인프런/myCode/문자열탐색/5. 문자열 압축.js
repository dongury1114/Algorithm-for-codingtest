function solution(s) {
    let answer = ""
    let cnt = 1
    s = s + " "
    for (let i = 0; i < s.length - 1; i++) {
        if (s[i] === s[i + 1]) {
            cnt++
        } else {
            if (cnt === 1) answer += s[i]
            else {
                answer += s[i] + cnt
                cnt = 1
            }

        }

    }
    return answer
}

let input = "KKHSSSSSSSE"
console.log(solution(input));
