import codewars_test as test
from Knight import knight


@test.describe("Shortest knight path")
def shortest_night_path_test():
    @test.it("starting at a1")
    def a1_tests():
#        test.assert_equals(knight('a1', 'c1'), 2)
#        test.assert_equals(knight('a1', 'f1'), 3)
#        test.assert_equals(knight('a1', 'f3'), 3)
#        test.assert_equals(knight('a1', 'f4'), 4)
#        test.assert_equals(knight('a1', 'f7'), 5)
        test.assert_equals(knight('d1', 'a2'), 2)