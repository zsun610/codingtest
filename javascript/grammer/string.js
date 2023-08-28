// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let T = Number(input[0]);
for(let i = 1; i <= T; i++){
  let answer = '';
  let [r,s] = input[i].split(" ");
  for(let j = 0; j < s.length; j++){
    // 문자열.charAt(인덱스).repeat(반복횟수)
    answer += s.charAt(j).repeat(r);
  }
  console.log(answer);
}