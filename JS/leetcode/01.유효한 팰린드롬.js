
const isPalindrome = s => {
    s = s.toLowerCase().replace(/[^a-z0-9]/gi, '');
    for (let i = 0, j = s.length - 1; i <= j; i++, j--) {
        if (s.charAt(i) !== s.charAt(j)) return console.log(false);
    }
    return console.log(true);
}

// isPalindrome("A man, a plan, a canal: Panama")