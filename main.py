import threading

lock = threading.Lock()


# Функция, которая будет выполняться в каждом потоке
def worker():
    lock.acquire()
    try:
        """Код, который нужно выполнить в каждом потоке"""
        thread_name = threading.current_thread().name
        print(f"Выполняется поток {thread_name}")

    finally:
        lock.release()


def main():
    # Создаем список потоков
    threads = []

    # Создаем и запускаем 5 потоков
    for i in range(5):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
