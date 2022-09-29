// function solution(s, t) {
//     let answer = 0;
//     for (let x of s) {
//         if (x === t) answer++
//     }
//     return answer
// }

// let input = "COMPUTERPROMGRAMMING";
// console.log(solution(input, "G"));

function solution(s, t) {
    let answer = s.split(t).length;
    return answer - 1
}

let input = "COMPUTERPROMGRAMMING";
console.log(solution(input, "G"));