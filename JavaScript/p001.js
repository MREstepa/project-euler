var divisible_container = []

for (let i = 0; i < 1000; i++) {
  if (((i % 3) === 0) || ((i % 5) === 0)) {
      divisible_container.push(i)
  } 
}

console.log(
    divisible_container.reduce( (a, b) => a + b, 0)
) // 233168
