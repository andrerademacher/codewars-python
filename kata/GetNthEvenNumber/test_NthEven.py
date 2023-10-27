import codewars_test as test
from kata.GetNthEvenNumber.NthEven import nth_even


@test.describe("nth even number kata")
def nth_even_test():
    @test.it("positive input values")
    def positive_input_values():
        test.assert_equals(nth_even(1), 0)
        test.assert_equals(nth_even(2), 2)
        test.assert_equals(nth_even(3), 4)
        test.assert_equals(nth_even(10), 18)
        test.assert_equals(nth_even(51), 100)
        test.assert_equals(nth_even(100), 198)