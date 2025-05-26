import queue
import time
import sys
import threading
from Thread1 import Thread1
from Thread2 import Thread2

def main(argv):
    try:
        print("MAIN THREAD:", threading.get_ident())
        message_queue = queue.Queue()

        # Start three threads and connect with queue
        Thread1(1, message_queue)
        Thread2(2, message_queue)
        Thread2(3, message_queue)

        print("Main: Threads started and running in background.\n")

        start_time = time.time()
        timeout = 10 

        # Check for messages until timeout or keyboard interrupt
        while time.time() - start_time < timeout:
            try:
                msg = message_queue.get(timeout=0.5)
                print(f"Main received: {msg}")
            except queue.Empty:
                print("Main: No messages, continuing...")

        print("Main: Exiting without waiting for threads to complete.")

        return 0
    except Exception as e:
        print(e)
        return -1

if "__main__" == __name__:
    sys.exit(main(sys.argv))