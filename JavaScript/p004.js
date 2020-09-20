let palindromes = []

for (let x = 999; x >= 0; x--) {
    for (let y = 999; y >= 0; y--) {
        let ans = x * y
        
        if (ans.toString() === ans.toString().split('').reverse().join('')) {
            palindromes.push(ans)
        }
    }
}

console.log(Math.max.apply(Math, palindromes))
// 906609
