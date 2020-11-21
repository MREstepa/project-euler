// Prime generator
function isPrime(n) {
    if (isNaN(n) || !isFinite(n) || n%1 || n<2) return false;
    var m = Math.sqrt(n);
    for (var i=2;i<=m;i++) if (n%i==0) return false;
    return true;
}
 
function *prime_generator() {
    var count = 0;
    while(1) {
     if(isPrime(count)) yield count;
     count++;
    }
}

var prime = prime_generator();
let count = 0
while (count != 10001) {
 console.log(prime.next().value);
 count+=1
}  // 104743