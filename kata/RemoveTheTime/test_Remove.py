import codewars_test as test
from kata.RemoveTheTime.Remove import shorten_to_date


@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(shorten_to_date("Monday February 2, 8pm"), "Monday February 2")
        test.assert_equals(shorten_to_date("Tuesday May 29, 8pm"), "Tuesday May 29")
        test.assert_equals(shorten_to_date("Wed September 1, 3am"), "Wed September 1")
        test.assert_equals(shorten_to_date("Friday May 2, 9am"), "Friday May 2")
        test.assert_equals(shorten_to_date("Tuesday January 29, 10pm"), "Tuesday January 29")