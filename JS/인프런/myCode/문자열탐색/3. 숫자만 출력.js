function solution(s) {
    let answer = 0

    for (let x of s) {
        if (!isNaN(x)) answer = answer * 10 + Number(x);
    }
    return parseInt(answer)
}

let input = "00aoisdf2oi00asdfoi4"
console.log(solution(input));


// function solution(s) {
//     let answer = s.match(/[0-9]/g).join("")

//     return parseInt(answer)
// }

// let input = "00aoisdf2oi00asdfoi4"
// console.log(solution(input));
