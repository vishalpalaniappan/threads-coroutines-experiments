import queue
import time
import sys
from Thread1 import Thread1
from Thread2 import Thread2

# Used multiple references to learn about threads and assemble this program.
# I decided not to link the references because its generic code.

def main(argv):
    try:
        message_queue = queue.Queue()

        # Start threads (daemon = True, so they will terminate when this program is finished.)
        Thread1(1, message_queue)
        Thread2(2, message_queue)
        Thread2(2, message_queue)

        # Main app can do other things while threads run
        print("Main: Threads started and running in background.\n")

        # Optionally, monitor queue for a while
        start_time = time.time()
        timeout = 10  # seconds

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