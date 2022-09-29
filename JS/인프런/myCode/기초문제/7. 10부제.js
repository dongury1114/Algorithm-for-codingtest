
function solution(day, arr) {
    let answer = 0;
    for (let x of arr) {
        if (x % 10 == day) answer++;
    }

    return answer;
}

arr = [25, 23, 11, 47, 53, 17, 33];
console.log(solution(3, arr));


{/* function solution(arr) {
            let answer, count = 0
            for (let x of arr) {
                if (x % 10 === 3)
                    count += 1
            }
            answer = count
            return answer
        }
        let arr = [25, 23, 11, 47, 53, 17, 33];
        console.log(solution(arr)); */}

