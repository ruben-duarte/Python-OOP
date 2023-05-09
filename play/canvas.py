
def  draw_rect(width=0, height=0):
    print()
    for row in range(height):
        for col in range(width):
            if (row == 0  or row == height - 1) or ((col == 0 or col == width - 1) and (row != 0 or row != height - 1)):
                print("=", end=' ')
            else:
                print(" ",end= ' ')
        print()

draw_rect(14,8)
draw_rect(10,8)
draw_rect(6,8 )


def  draw_rect_with_text(height=0, text=' Hello!'):
    print()
    width = len(text) + 4
    for row in range(height):
        for col in range(width):
            if (row == 0  or row == height - 1) or ((col == 0 or col == width - 1) and (row != 0 or row != height - 1)):
                print("=", end='')
            elif row == height//2:
                print(" " , text, " ", "=")
                break
            else:
                print(" ",end= ' ')
        print()

text ='Wordle game Welcome! choose an option'
text2 = """
Bienvenidos 
          al sistema de usuario
                en la terminal  ✨
"""
draw_rect_with_text(3, text)