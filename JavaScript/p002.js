// Fibonacci Generator
function fibonacci_generator(num) {
    if (num <= 1) return 1;
    return fibonacci_generator(num - 1) + fibonacci_generator(num - 2);
}

let fib = []
let x = 0

while (true) {
    current_fib = fibonacci_generator(x)
    if (current_fib >= 4000000) break
    if (current_fib % 2 === 0) fib.push(current_fib)
    x += 1
}

console.log(
    fib.reduce( (a, b) => a + b, 0 )
) // 4613732
