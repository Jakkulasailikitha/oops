# creating a class with assess of object
# class human():
#     color="white"
#     height=5.11
#     def run(self):
#         print("running")
#     def walk (self):
#         print("walking")
# # creating a class  
# # creating odject with class
# man=human()
# mini=human()
# print(man.color,mini.height)
# man.run()
# mini.walk()

# using constructor that means init




class human:
    def __init__(self):
        # self.color=c
        # self.height=h
        print("constructor")
    def run(self):
        print("running")
    def walk(self):
        print("walking")
man=human()
mini=human()




