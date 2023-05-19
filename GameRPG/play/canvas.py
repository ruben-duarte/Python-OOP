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

    def  draw_rect_with_text(self, text=' Hello!'):
        print()
        width = len(text) + 4
        for row in range(self.height):
            for col in range(self.width):
                if (row == 0  or row == self.height - 1) or ((col == 0 or col == width - 1) and (row != 0 or row != self.height - 1)):
                    print("=", end='')
                elif row == self.height//2:
                    print(" " , text, " ", "=")
                    break
                else:
                    print(" ",end= ' ')
            print()

    def  heading(self):
        print()
        print("="*40)
        print("WELCOME ENGANCHA_TIC ✨📢!")
        print("="*40)


rect_1 = Rectangle(4,8)
print(rect_1.heading())
print(rect_1.draw_rect_with_text("Saludos desde Bucaramanga "))







