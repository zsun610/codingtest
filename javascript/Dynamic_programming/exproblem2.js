/* 정수 x가 주어졌을 때, 정수 x에 사용할 수 있는 연산은 4가지이다.
  정수 x가 주어졌을 때, 연산 4개를 적절히 사용하여 값을 1로 만들고자 한다.
  연산을 사용하는 횟수의 최솟값을 출력하라.

  1. x가 5로 나누어 떨어지면, 5로 나눈다.
  2. x가 3으로 나누어 떨어지면, 3으로 나눈다.
  3. x가 2로 나누어 떨어지면, 2로 나눈다.
  4. x에서 1을 뺀다.
  
  점화식을 코드로 끌어내는 거 포인트
*/


// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let x = 26;
let d = new Array(30001).fill(0);

// 다이나믹 프로그래밍(bottom-up)
for(let i = 2; i <= x; i++){
  d[i] = d[i-1] + 1;
  if (i % 2 === 0){
    d[i] = Math.min(d[i],d[parseInt(i/2)] + 1);
  }
  if (i % 3 === 0){
    d[i] = Math.min(d[i], d[parseInt(i/3)] + 1);
  }
  if(i % 5 === 0){
    d[i] = Math.min(d[i], d[parseInt(i/5)] + 1);
  }
}

console.log(d[x]);
