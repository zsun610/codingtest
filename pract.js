// 1003, 1904, 2156


// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let fs = require('fs');
const { test } = require('node:test');
let input = fs.readFileSync('input.txt').toString().split('\n');

let n = parseInt(input[0]);
let d = new Array(1000000).fill(0);

for(let i = 1; i <= n; i++){
  d[i]
}