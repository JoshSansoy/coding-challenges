function run(n) {

    const alphabet = [
        {M: 1000},
        {CM: 900},
        {D: 500},
        {CD: 400},
        {C: 100},
        {XC: 90},
        {L: 50},
        {XL: 40},
        {X: 10},
        {IX: 9},
        {V: 5},
        {IV: 4},
        {I: 1}
    ]

    let n_in_roman_alphabet = '';
    
    alphabet.forEach((numeral) => {
        while (n >= Object.values(numeral)[0]){
            n_in_roman_alphabet += Object.keys(numeral)[0]
            n -= Object.values(numeral)[0]
        }
    })

    return n_in_roman_alphabet;
}
