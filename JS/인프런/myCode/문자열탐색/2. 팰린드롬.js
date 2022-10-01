function solution(s) {
    let answer = "YES";
    s = s.toLowerCase().replace(/[^a-z]/g, "");

    console.log(s);
    if (s.split("").reverse().join("") !== s) return answer = "NO"

    return answer
}

let input = "found7, time: study; Yduts; emit, 7Dnuof";
console.log(solution(input));
