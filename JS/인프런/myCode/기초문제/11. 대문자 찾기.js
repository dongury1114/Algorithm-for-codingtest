// function solution(s) {
//     let answer = 0;
//     for (let x of s) {

//         if (x === x.toUpperCase()) answer++;
//     }
//     return answer
// }

// let input = "ABCabc"

// console.log(solution(input));

function solution(s) {
    let answer = 0;
    for (let x of s) {
        let num = x.charCodeAt();
        if (num >= 65 && num <= 90) answer++
    }
    return answer
}
// 65 - 90
let input = "ABCabc"

console.log(solution(input));