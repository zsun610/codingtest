let string = '123456789';
let answer = 0;

// for문으로 문자열 탐색 가능
for (let x of string){
    answer += Number(x);
}

console.log(answer);