/* 다이나믹 프로그래밍(재귀함수)의 코드 형식
  1. 문제 이해하기
  2. 점화식 찾아내기
  3. 구현 방식(상향식/하향식) 결정하기
    3-1. 상향식(Bottom-up) : 반복문을 이용해 초기항부터 계산
    3-2. 하향식(Top-down) : 재귀 함수로 큰 항을 구하기 위해 작은(이전) 항을 호출하는 방식
    => 이미 구한 함수 값을 담는 테이블을 dp테이블이라 한다.
  4. 코드로 구현하기  */

function dp(){
  // 1. 종료 조건 (점화식에서 초기값)
  // 2. 이미 해결한 문제라면, 정답을 그대로 반환
  // 3. 점화식에 따라 정답 계산
}


// 하향식(Top-down) 피보나치 수열
let d = new Array(100).fill(0); // dp테이블, 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화

// fibonacci function을 재귀함수로 구현 (top-down programming)
function fibo(x){
  // 1. 종료 조건(초기값)
  if(x == 1 || x == 2){    
    return 1;
  }
  // 2. 이미 계산한 적 있는 문제라면 그대로 반환 (중복 계산 방지)
  if(d[x] !== 0){
    return d[x];
  }
  // 3. 아직 계산하지 않은 문제라면 점화식 재귀함수로 구현
  d[x] = fibo(x - 1) + fibo(x - 2);
  return d[x];
}

console.log(fibo(99));


// 상향식(Bottom-up) 피보나치 수열
let db = new Array(100).fill(0);  // dp테이블, 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화

// 1. 초기값 (첫 번째, 두 번째 피보나치 수는 1)
db[1] = 1;
db[2] = 2;
n = 99;

// 2. 점화식 반복문으로 구현
for(let i = 3; i <= n; i++){
  db[i] = db[i - 1] + db[i - 2];
}
console.log(db[n]);