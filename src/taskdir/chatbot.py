def echo(text):
    return text


def search_bot(text):
    from googlesearch import search
    return "I have a link for you" + search(text, num=1, stop=1, pause=2)

def draw_bot(text):
    sides = [int(s) for s in text.split() if s.isdigit()][0]
    import turtle
    for i in range(sides):
        turtle.forward(200)
        turtle.right(360/sides)
    return "I drew it somewhere here."

while True:
    user_text = input("User ::")
    bot_text = draw_bot(user_text)
    print ("Bot :: " + bot_text)
