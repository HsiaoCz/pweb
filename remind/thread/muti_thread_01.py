import time


def game():
    """play game for 5 secends"""

    for i in range(5):
        print("---playing game---")
        time.sleep(1)


def shopping():
    """city walk"""

    for i in range(5):
        print("---city walking---")
        time.sleep(1)



def main():
    shopping()
    game()