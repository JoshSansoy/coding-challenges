function run(p) {


    let vowels = ['a','e','i','o','u']
    let vowelCount = 0;
    let spaceCount = 0;
    const pLength = p.length

    pCharacters = p.split('');
    pvArray = p.split('');

    eachCounter = 0

    pCharacters.forEach((character, index) => {
        if(vowels.indexOf(character) !== -1){
            vowelCount++;
        }
        if([''].indexOf(character) !== -1){
            spaceCount++;
        }
    })
    let i = 0

    while(i <= pvArray.length){
        if(vowels.indexOf(pvArray[i]) !== -1){
            pvArray.splice(i-1, 1, 'pv')
        }
        i++
    }

    pArrayCaps = [];
    pArray = p.split('')
    pArray.forEach((character) => {
        if(character === character.toLowerCase()){
            pArrayCaps.push(character.toUpperCase())
        }
        if(character === character.toUpperCase()){
            pArrayCaps.push(character.toLowerCase())
        }
    })
    
    pReversed = pArrayCaps.reverse().join('');
    pvString = pvArray.join('');
    pDashed = p.split(' ').join('-');


    combined_queries = vowelCount + ' ' + (pLength - vowelCount - spaceCount) +'::' + pReversed + '::' + pDashed + '::' + pvString;
    return combined_queries
}

run('This is p')