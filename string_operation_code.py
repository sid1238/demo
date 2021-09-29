# class  FileOperations: 
    
        

#     def __init__(self, contents, values):
#         self.values = values
#         self.contents = contents
        
#     #def __init__(self, contents1, values1):
#         #self.values1 = values1
#         #self.contents1 = contents1
        


#     def replace_spaces_with_character(self):
#         b=" "
#         for i in range(0,len(self.contents)):
#             if(self.contents[i]==' '):
#                 b=b+self.values
#             else:
#                 b=b+self.contents[i]
#         return b  

#     def count_characters(self):
#         k=0
#         for i in range(0,len(self.contents)):
#             if(self.contents[i]==self.values):
#                 k = k+1
#         return k

# a ="adity akk oo "
# x= '*'
# c ="I am a good boy"
# p ="a"
# abc = FileOperations(a, x)
# #print(abc.replace_spaces_with_character())
# abc.replace_spaces_with_character()
# cde = FileOperations(c, p)
# #print(cde.count_characters())
# cde.count_characters()

"""

First exercise to start with unittesting.

Task:

1. Read about class - __init__, self - ?
2. Implement replace_spaces_with_character, count_characters
3. Write a test python file to test the above functions.

"""

class FileOperations:

    def __init__(self):
        self.contents = ""
        self.file_name = ""

    def get_contents(self, file_name):

        """
        To be implemented
        """
        t = open(file_name, 'r')
        self.contents = t.read()
        # for each in self.contents:
        #     print (each)
        # self.contents.close()

    def replace_spaces_with_character(self, character):

        """
        In the string "contents", replace all the occurences of spaces with characters and print them.
        Ex: "This is an example" -> contents and 1 -> character
        Return: "This1is1an1example"
        """
        # contents = None
        # if contents:
        # self.contents = open(self.file_name, 'r')
        # text = self.contents.read()
        output = ""
        for string_character in self.contents:
            if string_character == " ":
                output+=character
            else:
                output+=string_character
        #print(output)
        return output

    def count_characters(self, character):

        """
        In the string "contents", get the count of the occurences of the "character"
        Ex: "This is an example" -> contents and i -> character.
        Return: 2
        """

        count = 0
        #print(count)
        # self.contents = open(self.file_name, 'r')
        # text = self.contents.read()
        #print(self.contents)
        for char in self.contents:
            if char == character:
                count+=1

        #print(count)
        return count
# a = FileOperations()
# a.get_contents("abc.txt")
# b = FileOperations()
# b.get_contents("cde.txt")



