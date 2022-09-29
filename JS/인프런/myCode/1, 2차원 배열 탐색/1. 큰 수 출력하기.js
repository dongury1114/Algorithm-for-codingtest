function solution(arr) {
    let answer = [];
    answer.push(arr[0])

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > arr[i - 1]) {
            answer.push(arr[i])
        }
    }
    return answer
}

let input = [7, 3, 9, 5, 6, 12]
console.log(solution(input));
