let index = 2
let num = 600851475143
while ((index * index) <= num) {
    if (num % index) index += 1
    else num = Math.floor(num / index)
}
console.log(num)
// 6857
