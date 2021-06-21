MORSE = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

class Solution:

    def run(morseToEnglish, textToTranslate):	
        translatedText = 'Invalid Morse Code Or Spacing'
        message = ''

        if textToTranslate != '':
            if morseToEnglish == False:
                for letter in textToTranslate.upper():
                    if letter != ' ':
                        message += MORSE[letter] + ' '
                    elif letter == ' ':
                        message += '  '
                    else:
                        translatedText = 'Invalid Morse Code Or Spacing'

            if morseToEnglish == True:
                inv_MORSE = {v: k for k, v in MORSE.items()}

                words = []
                words = textToTranslate.split('   ')
                for word in words:
                    letters = word.split(' ')
                    for letter in letters:
                        if letter != '':
                            message += inv_MORSE[letter]
                    message += ' ';

        translatedText = message.lower();
        return translatedText

    print(run(False,'Message'))