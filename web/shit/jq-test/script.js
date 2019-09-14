function showFunc() {
    $('#show').slideDown();
}

function closeFunc() {
    $('#show').slideUp();
}

function myFunction(a, b) {
    if (a > 1 && b < -1) {
        return a * b;
    } else {
        return("u r wrong");
    }
}
console.log(myFunction(-2, 3));
