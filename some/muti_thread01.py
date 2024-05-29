import time


def game():
    """play game 5 seconds"""

    for i in range(5):
        print("---playing game now.....")
        time.sleep(1)


def shopping():
    """shopping 5 seconds"""

    for i in range(5):
        print("---shopping now")
        time.sleep(1)


def main():
    shopping()
    game()
