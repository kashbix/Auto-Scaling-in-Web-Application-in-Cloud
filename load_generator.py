import requests
import threading
import argparse
import time

def send_request(url):
    while True:
        try:
            requests.get(url)
        except:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--threads', type=int, default=10)
    parser.add_argument('--url', type=str, default='http://127.0.0.1:8000/')
    parser.add_argument('--infinite', action='store_true')
    parser.add_argument('--duration', type=int, default=60)
    args = parser.parse_args()

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=send_request, args=(args.url,))
        t.daemon = True
        t.start()
        threads.append(t)

    if not args.infinite:
        time.sleep(args.duration)
    else:
        while True:
            time.sleep(1)
