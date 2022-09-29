// function solution(s) {
//     let set = new Set(s);


//     return answer = [...set].join("");
// }

// let input = "ketstappse"
// console.log(solution(input));

// https://ddoni-code.tistory.com/21

function solution(s) {
    let answer = "";
    for (let i = 0; i < s.length; i++) {
        if (s.indexOf(s[i]) === i) {
            answer += s[i];
        }
    }
    return answer
}

let input = "ketstappse"
console.log(solution(input));