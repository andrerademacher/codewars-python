from Morse import decode_morse
import codewars_test as test

@test.describe("Morse Code 1")
def tests():
        
    @test.it("Should obtain correct decoding of Morse code from the description")
    def test_morse_hey_jude():
        test.assert_equals(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

    @test.it("Should obtain correct decoding of Morse code for basic examples")
    def test_morse_basic_examples():
        test.assert_equals(decode_morse('.-'), 'A')
        test.assert_equals(decode_morse('--...'), '7')
        test.assert_equals(decode_morse('...-..-'), '$')
        test.assert_equals(decode_morse('.'), 'E')
        test.assert_equals(decode_morse('..'), 'I')
        test.assert_equals(decode_morse('. .'), 'EE')
        test.assert_equals(decode_morse('.   .'), 'E E')
        test.assert_equals(decode_morse('...-..- ...-..- ...-..-'), '$$$')
        test.assert_equals(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
        test.assert_equals(decode_morse('.-... ---...   -..-. --...'), '&: /7')
        test.assert_equals(decode_morse('...---...'), 'SOS')
        test.assert_equals(decode_morse('... --- ...'), 'SOS')
        test.assert_equals(decode_morse('...   ---   ...'), 'S O S')
        
    @test.it("Should obtain correct decoding of Morse code for examples with extra spaces")
    def test_morse_basic_examples_with_extra_spaces():
        test.assert_equals(decode_morse(' . '), 'E')
        test.assert_equals(decode_morse('   .   . '), 'E E')

    @test.it("Should obtain correct decoding of Morse code for a complex example, and should ignore leading and trailing whitespace")
    def test_morse_complex_example():
        test.assert_equals(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')