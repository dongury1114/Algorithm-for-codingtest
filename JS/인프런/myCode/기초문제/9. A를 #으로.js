// function solution(s) {
//     let answer = "";
//     for (let x of s) {
//         if (x === "A") answer += "#";
//         else answer += x;
//     }
//     return answer
// }

// let string = "BANANA";
// console.log(solution(string));

function solution(s) {
    let answer = s;
    answer = answer.replace(/A/g, "#")
    return answer
}

let input = "BANANA"
console.log(solution(input));