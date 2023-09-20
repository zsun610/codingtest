/* N개의 창고가 있을 때, 얻을 수 있는 식량의 최댓값을 구하라.
이 때, 최소 한 칸 이상 떨어진 창고들만 선택할 수 있다.
*/


// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

// 정수 N 입력받기
n = 4;
// 모든 식량 정보 입력받기
array = [1,3,1,5];

// 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = new Array(100).fill(0);

// 다이나믹 프로그래밍 (bottom-up)
d[0] = 1;
d[1] = Math.max(array[0], array[1]);
for(let i = 2; i < n; i++){
  d[i] = Math.max(d[i-1], d[i-2] + array[i]);
}

console.log(d[n-1]);