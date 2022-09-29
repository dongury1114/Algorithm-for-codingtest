function solution(arr) {
    let len = arr.length
    let answer = Array.from({ length: len }, () => 1);

    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            if (arr[i] < arr[j]) {
                answer[i]++
            }
        }
    }
    return answer
}
let input = [87, 89, 92, 100, 76]
console.log(solution(input));



