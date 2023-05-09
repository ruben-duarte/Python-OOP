class Rectangle:

    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def  draw_rect(self):
        print()
        for row in range(self.height):
            for col in range(self.width):
                if (row == 0  or row == self.height - 1) or ((col == 0 or col == self.width - 1) and (row != 0 or row != self.height - 1)):
                    print("=", end=' ')
                else:
                    print(" ",end= ' ')
            print()



rect_1 = Rectangle(4,8)
rect_2 = Rectangle(2,4)
rect_3 = Rectangle(5,10)

print(rect_1.draw_rect())
print(rect_2.draw_rect())
print(rect_3.draw_rect())















# def  draw_rect_with_text(height=0, text=' Hello!'):
#     print()
#     width = len(text) + 4
#     for row in range(height):
#         for col in range(width):
#             if (row == 0  or row == height - 1) or ((col == 0 or col == width - 1) and (row != 0 or row != height - 1)):
#                 print("=", end='')
#             elif row == height//2:
#                 print(" " , text, " ", "=")
#                 break
#             else:
#                 print(" ",end= ' ')
#         print()

# text ='Wordle game Welcome! choose an option'
# text2 = """
# Bienvenidos 
#           al sistema de usuario
#                 en la terminal  ✨
# """
# draw_rect_with_text(3, text)