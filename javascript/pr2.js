const dx = ["+","-","*","/"];
let s = 7
for(let i = 0; i < 4; i++){
  if(dx[i] === "+"){
    s += s;
  }
  else if(dx[i] === "-"){
    s -= s;
  }
  else if(dx[i] === "*"){
    s *= s; 
  }
  else if(dx[i] === "/"){
    s /= s;
  }
}