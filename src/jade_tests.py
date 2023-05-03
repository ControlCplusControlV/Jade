import unittest
import jade

class TestIndividualMutations(unittest.TestCase):
    def test_binary_op(self):
        mutator = jade.Mutator(jade.Mutation.BINARY_OP, 1, [
            '# @Jade: BINARY_OP', 
            'self.val = _val + 5'
        ])
        new_file = mutator.mutate()
        self.assertEqual(new_file[1], 'self.val = _val - 5')

    def test_unary_op(self):
        mutator = jade.Mutator(jade.Mutation.UNARY_OP, 1, [
            '# @Jade: UNARY_OP', 
            'self.val--'
        ])
        new_file = mutator.mutate()
        self.assertEqual(new_file[1], 'self.val++')

        mutator = jade.Mutator(jade.Mutation.UNARY_OP, 1, [
            '# @Jade: UNARY_OP', 
            'self.val++'
        ]) 

        new_file = mutator.mutate()
        self.assertEqual(new_file[1], 'self.val--')
    
    def test_require(self):
        mutator = jade.Mutator(jade.Mutation.REQUIRE, 1, [
            '# @Jade: REQUIRE', 
            'assert self.val > 5'
        ])
        new_file = mutator.mutate()
        self.assertEqual(new_file[1], 'assert not self.val > 5')

        mutator = jade.Mutator(jade.Mutation.REQUIRE, 1, [
            '# @Jade: REQUIRE',
            'assert not self.val > 5'
        ])

        new_file = mutator.mutate()
        self.assertEqual(new_file[1], 'assert self.val > 5')

    def test_if_statement(self):
        mutator = jade.Mutator(jade.Mutation.IF_STATEMENT, 1, [
            '# @Jade: IF_STATEMENT',
            'if self.val > 5:'
        ])

        new_file = mutator.mutate()
        self.assertEqual(new_file[1], 'if not self.val > 5:')

        mutator = jade.Mutator(jade.Mutation.IF_STATEMENT, 1, [
            '# @Jade: IF_STATEMENT',
            'if not self.val > 5:'
        ])

        new_file = mutator.mutate()
        self.assertEqual(new_file[1], 'if self.val > 5:')

if __name__ == '__main__':
    unittest.main()
