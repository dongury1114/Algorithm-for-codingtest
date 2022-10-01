// function solution(s) {
//     let answer = "YES";
//     let tmp = s.toLowerCase()
//     let n = tmp.length;

//     for (let i = 0; i < Math.floor(n / 2); i++) {
//         if (s[i] !== s[n - i - 1]) return "NO"
//     }

//     return answer
// }

// let input = "go1oG"
// console.log(solution(input));

function solution(s) {
    let answer = "YES";
    let tmp = s.toLowerCase()
    let n = tmp.length;

    if (tmp.split("").reverse().join("") === tmp) {
        answer = "YES"
    } else {
        answer = "NO"
    }
    return answer
}

let input = "go1oG"
console.log(solution(input));
