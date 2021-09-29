import unittest
import string_operation_code


# class Teststring(unittest.TestCase):

#     def test_replace_spaces_with_character(self):
#         self.assertEqual(string_operation_code.replace_spaces_with_character("I am tall", "1"), "I1am1tall")
#         self.assertEqual(string_operation_code.replace_spaces_with_character("reading a book", "&"), "reading&a&book")
#         self.assertEqual(string_operation_code.replace_spaces_with_character("take a left turn", "j"), "takejajleftjturn")
#         abc = string_operation_code.FileOperations(self.a, self.x)
#         abc.replace_spaces_with_character()

#     def test_count_characters(self):
#         self.assertEqual(string_operation_code.count_characters("I am tall", "a"), 2)
#         self.assertEqual(string_operation_code.count_characters("reading a book", "o"), 2)
#         self.assertEqual(string_operation_code.count_characters("turn left", "j"), 0)
#         cde = string_operation_code.FileOperations(self.c, self.p)
#         cde.count_characters()

# if __name__ == '__main__':
#     unittest.main()
#     # efg = string_operation_code.FileOperations(a, x)
#     # efg.replace_spaces_with_character()
#     # cde = string_operation_code.FileOperations(c, p)
#     # cde.count_characters()
class TestStringOperations(unittest.TestCase):

    def test_replace_spaces_with_character(self):

        sample_object = string_operation_code.FileOperations()

        sample_object.get_contents("abc.txt")

        self.assertEqual(sample_object.replace_spaces_with_character("-"), "I-am-a-CSE-student")
        self.assertEqual(sample_object.replace_spaces_with_character(" "),"I am a CSE student")
        self.assertEqual(sample_object.replace_spaces_with_character("&"), "I&am&a&CSE&student")

        sample_object1 = string_operation_code.FileOperations()

        sample_object1.get_contents("cde.txt")

        self.assertEqual(sample_object1.replace_spaces_with_character("-"), "I-am-a-computer-science-student")
        self.assertEqual(sample_object1.replace_spaces_with_character(" "),"I am a computer science student")
        self.assertEqual(sample_object1.replace_spaces_with_character("&"), "I&am&a&computer&science&student")
        
        

    def test_count_characters(self):

        sample_options = string_operation_code.FileOperations()

        sample_options.get_contents("abc.txt")

        self.assertEqual(sample_options.count_characters("a"), 2)
        self.assertEqual(sample_options.count_characters("C"), 1)
        self.assertEqual(sample_options.count_characters("y"), 0)

        sample_options1 = string_operation_code.FileOperations()

        sample_options1.get_contents("cde.txt")

        self.assertEqual(sample_options1.count_characters("a"), 2)
        self.assertEqual(sample_options1.count_characters("f"), 0)
        self.assertEqual(sample_options1.count_characters("x"), 0)


        


if __name__ == '__main__':
    unittest.main()
