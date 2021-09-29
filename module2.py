# """
# Import the module1
# """
# import module1

# class FileClass:

#     def __init__(self):
#         self.file_name = ""
#         self.string_object = None

#     def create_string_object(self):
#         """
#         In this function, create a StringClass object from module1 and store the object in self.string_object
#         """
#         self.string_object = module1.StringClass()
    
#     def add_value(self, values):
#         """
#         In this function, add some random values to the StringClass object and delete it 
#         """
#         self.values = values
#         self.string_object = self.values
#         print(self.string_object)
#         self.string_object = self.string_object[0:0]
#         print(self.string_object)

#     def get_output(self):
#         """
#         In this function, return the StringClass object that you have created(self.string_object).
#         """
#         return self.string_object

# """
# Create a FileClass object and run all the functions in it to verify if they are working right
# """
# efg = FileClass()
# efg.create_string_object()
# x="run"
# efg.add_value(x)
# efg.get_output()
"""
Import the module1
"""
import module1
class FileClass:

    def __init__(self, file_name):
        """
        Create a file with self.file_name
        """
        self.file_name = ""
        self.string_object = None
        file= open(file_name, 'w')
        self.file_name=file.write("I am a student")
        #print(self.file_name)

    def create_string_object(self):
        """
        In this function, create a StringClass object from module1 and store the object in self.string_object
        """
        self.string_object = module1.StringClass()
    
    def add_value(self, value):
        """
        In this function, add "value" to the StringClass object 
        """
        self.values = value
        self.string_object = self.values
        #print(self.string_object)

    def delete_value(self, contents = None):
        """
        In this function, delete the last character.
        """
        self.contents = contents
        j=len(self.contents)
        if j>0:
            self.contents=self.contents[:j-1]
        #print(self.contents)

    def write_to_file(self):
        """
        In this function, write the self.string_object contents to the file with name - self.file_name
        """
        #file= open(file_name, 'w')
        self.file_name = self.string_object
        print(self.file_name)
    def get_contents(self):
        """
        In this functions, return the contents of the file.
        """
        return self.contents

"""
Create a FileClass object.
Using the member functions,
Create a string object.
Add some characters,
delete one,
store the content to file
return the contents of the file using get_contentsß
"""
cde=FileClass("abc.txt")
cde.create_string_object()
x="write"
cde.add_value(x)
cde.delete_value(x)
cde.write_to_file()
cde.get_contents()