function factorial(num) {
    var rval=1;
    for (var i = 2; i <= num; i++)
        rval = rval * i;
    return rval;
}

let num = 20
console.log(factorial(2 * num) / (factorial(num) ** 2))
// 137846528820