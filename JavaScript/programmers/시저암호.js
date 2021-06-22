function solution(str, n) {
  let newStr = "";
  for (const s of str) {
    if (s === " ") newStr += " ";
    else
      newStr += String.fromCharCode(
        s.charCodeAt(0) > 90
          ? ((s.charCodeAt(0) + n - 97) % 26) + 97
          : ((s.charCodeAt(0) + n - 65) % 26) + 65
      );
  }
  return newStr;
}

const hi = solution("The password to the safe is an elephant", 4);
console.log(hi);
