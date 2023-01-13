import threading

odd_event = threading.Event()
even_event = threading.Event()
TIMEOUT = 0.1


def printEven(n):
    for i in range(0, n, 2):
        print(i, flush=True)
        odd_event.set()
        even_event.clear()
        # print("waiting for even event", flush=True)
        even_event.wait(timeout=TIMEOUT)
    # print("printEven finished", flush=True)


def printOdd(n):
    odd_event.wait()
    for i in range(1, n, 2):
        print(i, flush=True)
        even_event.set()
        odd_event.clear()
        # print("waiting for odd event", flush=True)
        odd_event.wait(timeout=TIMEOUT)
    # print("printOdd finished", flush=True)


if __name__ == "__main__":
    n = 99
    t1 = threading.Thread(target=printEven, args=(n,), daemon=False)
    t2 = threading.Thread(target=printOdd, args=(n,), daemon=False)

    t1.start()
    t2.start()