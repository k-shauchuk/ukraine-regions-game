import turtle
import pandas
import ctypes

screen = turtle.Screen()
screen.title("Ukraine Regions Game")
image = "Map_of_Ukraine.gif"
screen.addshape(image)
screen.setup(840, 560)
turtle.shape(image)

# Getting coords by clicking on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("regions.csv")
all_regions = data.region.to_list()
guessed_regions = []

MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Попробуйте назвать все области Украины. Для выхода введите "Выход"', 'Добро пожаловать в игру "Назови все области Украины"!', 0)

while len(guessed_regions) < 25:    
    answer_region = screen.textinput(title=f"{len(guessed_regions)}/25 Назови область",
                                    prompt="Назови следующую область").title()
    if answer_region == "Выход":
        missing_regions = [region for region in all_regions if region not in guessed_regions]
        new_data = pandas.DataFrame(missing_regions)
        new_data.to_csv('regions_to_learn.csv')
        break
    if answer_region in all_regions:
        guessed_regions.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()    
        region_data = data[data.region == answer_region]
        t.goto(int(region_data.x), int(region_data.y))    
        t.write(answer_region, align="left", font=("Arial", 9, "bold"))