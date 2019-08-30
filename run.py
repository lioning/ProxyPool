from proxypool.scheduler import Scheduler
import sys
import io
import traceback

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        traceback.print_exc()
        main()


if __name__ == '__main__':
    main()
