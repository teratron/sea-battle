STATE_STOP = 0
STATE_RUN = 1
STATE_PAUSE = 2

app_state = STATE_STOP


def main():
    while app_state == STATE_RUN:
        if app_state == STATE_STOP:
            break


if __name__ == '__main__':
    main()
