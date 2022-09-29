// function solution(s) {
//     let answer = "";
//     let set = new Set(s);

//     return answer = [...set]
// }

// let input = ["good", "time", "good", "time", "student"]
// console.log(solution(input));

function solution(s) {
    let answer;
    answer = s.filter((v, i) => {
        return s.indexOf(v) === i;
    })

    return answer
}

let input = ["good", "time", "good", "time", "student"]
console.log(solution(input));