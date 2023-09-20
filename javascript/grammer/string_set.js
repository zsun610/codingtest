// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

// 단어에 존재하는 모든 문자에 대해서 각 단어가 연속해서 나타나는 경우
let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let n = parseInt(input[0]);
let answer = 0;

for(let i = 1; i <= n; i++){
  let tmp = input[i];
  let existChar = new Set()

  let check = true;
  for(let j = 0; j < tmp.length; j++){
    if(!existChar.has(tmp[j])){
      existChar.add(tmp[j]);
    }
    else if(existChar.has(tmp[j]) && (tmp[j-1] === tmp[j])){
      continue;
    }
    else{
      check = false;
      break;
    }
  }
  if(check === true) answer++;
}
console.log(answer);

// trim() 메서드는 문자열 양 끝의 공백을 제거한다.
let result = input[0].trim().split(" ");