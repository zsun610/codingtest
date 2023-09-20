// 1003, 1904, 2156


// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let fs = require('fs');
const { test } = require('node:test');
let input = fs.readFileSync('input.txt').toString().split('\n');

let n = 6
let d = new Array(1000000).fill(0);

d[1] = ['1']; // 1
d[2] = ['00','11']; // 00, 11
d[3] = 3; // 001, 100, 111
d[4] = 5; // 0000, 0011, 1001, 1100, 1111
d[5] = 7; // 00001, 10000, 00111, 10011, 11001, 11100, 11111
d[6] = 10; // 000000, 000011, 110000, 001100, 001111, 100111, 110011, 111001, 111100, 111111 
// d[7] = ; // 1000000, 0000001, 0000111, 1110000, 1001100, 1001100, 0011001, 1001111, 0011111, 100111, 110011, 111001, 111100, 111111 

let cnt = parseInt(n/2);
while(cnt > 0){
  let string = '';
  string += '00' * cnt
  cnt--;
  if(n % 2 === 0){
    
  }
  else{

  }
}

for(let i = 2; i <= n; i++){
  tmp = []
  for(let j = 0; j < d[i-1].length; j++){
    for(let k = 0; k < d[i-1][j].length; k++){
      if ()
    }
  }
}
/* while 문으로
우선 n이 짝수일 때
1. 00이 최대 n/2개까지 가능
2. 00이 0개일 때까지 경우의 수 구하기)

n이 홀수일 때 
1. 00이 최대 (n-1)/2개(짝수) 까지 가능
2. 00이 0개일 때까지 경우의 수 구하기)