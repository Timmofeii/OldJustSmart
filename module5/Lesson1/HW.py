import  pygame
def create_txt(txt,x,y):
    font_path = "C:/Users/Дениса ПК/Desktop/Шрифты/Doto-VariableFont_ROND,wght.ttf"

    font = pygame.font.Font(font_path, 35)
    text = pygame.render(txt,True,(255,255,255))
    return text
