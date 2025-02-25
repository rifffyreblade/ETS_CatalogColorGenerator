# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

red = [200, 00, 60]
orange = [247, 148, 29]
yellow = [224, 185, 80]
blue = [84, 162, 217]
violet = [185, 60, 255]
coursenum = int
lerp = float
lerp = 0.0
R = 0
G = 0
B = 0
R2 = 0
G2 = 0
B2 = 0



def find_range():
    global lerp
    global coursenum
    global R
    global G
    global B
    if coursenum == 1000:
        R = red[0]
        G = red[1]
        B = red[2]
    if coursenum < 2000:
        lerp = coursenum/2000
        find_color1000()
    if coursenum == 2000:
        R = orange[0]
        G = orange[1]
        B = orange[2]
    if 2000 <= coursenum < 3000:
        lerp = coursenum/3000
        find_color2000()
    if coursenum == 3000:
        R = yellow[0]
        G = yellow[1]
        B = yellow[2]
    if 3000 <= coursenum < 4000:
        lerp = coursenum/4000
        find_color3000()
    if coursenum == 4000:
        R = blue[0]
        G = blue[1]
        B = blue[2]
    if 4000 <= coursenum < 5000:
        lerp = coursenum/5000
        find_color4000()
    if coursenum == 5000:
        R = violet[0]
        G = violet[1]
        B = violet[2]
    find_grad()

def find_color1000():
    global lerp
    global R
    global G
    global B
    if red[0] > orange[0]:
        num0 = red[0] - orange[0]
        R = orange[0] + round(num0 * lerp)
    if red[0] < orange[0]:
        num0 = orange[0] - red[0]
        R = red[0] + round(num0 * lerp)
    if red[0] == orange[0]:
        R = red[0]
    if red[1] > orange[1]:
        num0 = red[1] - orange[1]
        G = orange[1] + round(num0 * lerp)
    if red[1] < orange[1]:
        num0 = orange[1] - red[1]
        G = red[1] + round(num0 * lerp)
    if red[1] == orange[1]:
        G = red[1]
    if red[2] > orange[2]:
        num0 = red[2] - orange[2]
        B = orange[2] + round(num0 * lerp)
    if red[2] < orange[2]:
        num0 = orange[2] - red[2]
        B = red[2] + round(num0 * lerp)
    if red[2] == orange[2]:
        B = red[2]


def find_color2000():
    global lerp
    global R
    global G
    global B
    if yellow[0] > orange[0]:
        num0 = yellow[0] - orange[0]
        R = orange[0] + round(num0 * lerp)
    if yellow[0] < orange[0]:
        num0 = orange[0] - yellow[0]
        R = yellow[0] + round(num0 * lerp)
    if yellow[0] == orange[0]:
        R = yellow[0]
    if yellow[1] > orange[1]:
        num0 = yellow[1] - orange[1]
        G = orange[1] + round(num0 * lerp)
    if yellow[1] < orange[1]:
        num0 = orange[1] - yellow[1]
        G = yellow[1] + round(num0 * lerp)
    if yellow[1] == orange[1]:
        G = yellow[1]
    if yellow[2] > orange[2]:
        num0 = yellow[2] - orange[2]
        B = orange[2] + round(num0 * lerp)
    if yellow[2] < orange[2]:
        num0 = orange[2] - yellow[2]
        B = yellow[2] + round(num0 * lerp)
    if yellow[2] == orange[2]:
        B = yellow[2]

def find_color3000():
    global lerp
    global R
    global G
    global B
    if yellow[0] > blue[0]:
        num0 = yellow[0] - blue[0]
        R = blue[0] + round(num0 * lerp)
    if yellow[0] < blue[0]:
        num0 = blue[0] - yellow[0]
        R = yellow[0] + round(num0 * lerp)
    if yellow[0] == blue[0]:
        R = yellow[0]
    if yellow[1] > blue[1]:
        num0 = yellow[1] - blue[1]
        G = blue[1] + round(num0 * lerp)
    if yellow[1] < blue[1]:
        num0 = blue[1] - yellow[1]
        G = yellow[1] + round(num0 * lerp)
    if yellow[1] == blue[1]:
        G = yellow[1]
    if yellow[2] > blue[2]:
        num0 = yellow[2] - blue[2]
        B = blue[2] + round(num0 * lerp)
    if yellow[2] < blue[2]:
        num0 = blue[2] - yellow[2]
        B = yellow[2] + round(num0 * lerp)
    if yellow[2] == blue[2]:
        B = yellow[2]

def find_color4000():
    global lerp
    global R
    global G
    global B
    if violet[0] > blue[0]:
        num0 = violet[0] - blue[0]
        R = blue[0] + round(num0 * lerp)
    if violet[0] < blue[0]:
        num0 = blue[0] - violet[0]
        R = violet[0] + round(num0 * lerp)
    if violet[0] == blue[0]:
        R = violet[0]
    if violet[1] > blue[1]:
        num0 = violet[1] - blue[1]
        G = blue[1] + round(num0 * lerp)
    if violet[1] < blue[1]:
        num0 = blue[1] - violet[1]
        G = violet[1] + round(num0 * lerp)
    if violet[1] == blue[1]:
        G = violet[1]
    if violet[2] > blue[2]:
        num0 = violet[2] - blue[2]
        B = blue[2] + round(num0 * lerp)
    if violet[2] < blue[2]:
        num0 = blue[2] - violet[2]
        B = violet[2] + round(num0 * lerp)
    if violet[2] == blue[2]:
        B = violet[2]

def find_grad():
    global R
    global G
    global B
    global R2
    global G2
    global B2
    R2 = R+35
    if R2>255:
        R2 = 255
    G2 = G+35
    if G2>255:
        G2 = 255
    B2 = B+35
    if B2>255:
        B2 = 255

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def colorFinder():
    global coursenum
    coursenum = int(input("Enter course number (Example, 1035):"))
    find_range()
    print("Main Accent Color RGB is:  " + str(R) + " " + str(G) + " " + str(B))
    print("Main Accent Color Hex is:  " + rgb_to_hex(R, G, B))
    print(colored_background("           "))
    print(colored_background("           "))
    print(colored_background("           "))
    print(colored_background("           "))
    print("Gradient Accent Secondary Color RGB is:  " + str(R2) + " " + str(G2) + " " + str(B2))
    print("Gradient Accent Secondary Color Hex is:  " + rgb_to_hex(R2, G2, B2))
    print(colored_backgroundGrad("           "))
    print(colored_backgroundGrad("           "))
    print(colored_backgroundGrad("           "))
    print(colored_backgroundGrad("           "))
    print("")
    newSearch()

def newSearch():
    colorFinder()

def colored_background(text):
    global R
    global G
    global B
    return f'\033[48;2;{R};{G};{B}m{text}\033[0m'
def colored_backgroundGrad(text):
    global R2
    global G2
    global B2
    return f'\033[48;2;{R2};{G2};{B2}m{text}\033[0m'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    colorFinder()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
