import threading

def process_lines(lines):
    for line in lines:
        print(f"{threading.current_thread().name} processed: {line.strip()}")

def threaded_file_processing(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    chunk_size = len(lines) // 4  # 4 threads
    threads = []

    for i in range(0, len(lines), chunk_size):
        t = threading.Thread(target=process_lines, args=(lines[i:i+chunk_size],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

threaded_file_processing("data.txt")