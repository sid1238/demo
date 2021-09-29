# class StringClass:

#     def __init__(self):

#         self.contents = ""

#     def appends(self, character, contents = None):
#         """
#         This function should append a character to the contents variable of the object. write the function accordingly.
#         """
#         self.contents = contents
        
#         return self.contents+character

    
#     def delete(self, contents = None):
#         """
#         This function should delete the last character of contents variable of the object. if contents variable value is "" , do nothing. Write the function accordingly.
#         """
#         self.contents = contents
#         j=len(self.contents)
#         if j>0:
#             self.contents=self.contents[:j-1]
#         return self.contents


    
#     def get_output(self):

#         return self.contents



# """
# Create an object of StringClass and run the functions of append and delete with some example and see if you can get the output using the get_output function
# """
# x = "Cars"
# a = "d"
# y = "rock"
# abc = StringClass()
# print(abc.appends(a, x))
# cde = StringClass()
# print(cde.delete(y))
class StringClass:

    def __init__(self):

        self.contents = ""

    def append(self, character, contents=None):
        """
        This function should append a character to the contents variable of the object. write the function accordingly.
        """
        self.contents = contents
        
        return self.contents+character
    
    def delete(self, contents=None):
        """
        This function should delete the last character of contents variable of the object. if contents variable value is "" , do nothing. Write the function accordingly.
        """
        self.contents = contents
        j=len(self.contents)
        if j>0:
            self.contents=self.contents[:j-1]
        return self.contents
    
    def get_output(self):

        return self.contents



"""
Create an object of StringClass and run the functions of append and delete with some example and see if you can get the output using the get_output function
"""
# x = "Cars"
# a = "d"
# y = "rock"
# abc = StringClass()
# print(abc.append(a, x))
# cde = StringClass()
# print(cde.delete(y))