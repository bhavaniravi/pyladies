def echo_bot(text):
    """
    I repeat what you say
    :param text:
    :return:
    """
    pass


def search_bot(text):
    """
    I search google for you
    :param text:
    :return:
    """
    pass


def draw_bot(text):
    """
    I draw shapes for you
    :param text:
    :return:
    """
    pass


def get_bot_response(text):
    return echo_bot(text)
    # return search_bot(text)
    # return draw_bot(text)

while True:
    user_text = input("User ::")
    bot_text = get_bot_response(user_text)
    print ("Bot :: " + bot_text)
