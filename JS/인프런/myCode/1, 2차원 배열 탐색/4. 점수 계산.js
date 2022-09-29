function solution(arr) {
    let answer = 0;
    let tmp = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 1) {
            tmp++
            answer += tmp
        } else if (arr[i] === 0) {
            tmp = 0
        }
    }

    return answer
}

let input = [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
console.log(solution(input));
