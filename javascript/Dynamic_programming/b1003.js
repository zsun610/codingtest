// 1003, 1904, 2156


// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let fs = require('fs');
const { test } = require('node:test');
let input = fs.readFileSync('input.txt').toString().split('\n');

d = new Array(100).fill(0);
d[0] = 0;
d[1] = 1;

// 다이나믹 프로그래밍 (bottom-up)
for(let i = 2; i <= 40; i++){
  d[i] = d[i-1] + d[i-2];
}

let testCases = parseInt(input[0]);
for(let t = 1; t <= testCases; t++){
  let n = parseInt(input[t]);
  if (n === 0){
    console.log(1,0);
  }
  // 0의 개수와 1의 개수 출력
  else{
    console.log(d[n-1],d[n]);
  }
}