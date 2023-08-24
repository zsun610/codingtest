// 뒤로 거슬러 올라 갈 수 없으므로 BFS 사용

let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');
let cn = parseInt(input[0]);
let nn = parseInt(input[1]);
let all = []
for(let i = 0; i < nn; i++){
  var [a,b] = input[2+i].split(' ').map(Number);
  // 원소 2개 정렬
  if(a > b){
    all.push([b,a]);
  }
  else{
    all.push([a,b]);
  }
}

// 원소 앞 번호 순으로 정렬 
all.sort((a,b) => (a[0]-b[0]));

let answer = new Set();

for (let i = 0; i < all.length; i++){
  var [x,nx] = all[i];
  // 만약 x가 answer 에 있으면 nx를 push
  if (x === 1) {
    answer.add(nx);
  }
  else if (answer.has(x)){
    answer.add(nx);
  }
  else if (answer.has(nx)){
    answer.add(x);
  }
}

console.log(answer.size);

