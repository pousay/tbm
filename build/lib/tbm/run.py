from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os


def check_existance(file: str) -> bool:
    return os.path.isfile(file)


class FileChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if not check_existance("./run.py"):
            print('[ERROR] "run.py" DOES NOT EXISTS')
            exit()
        changed_file = str(event.src_path)

        if not changed_file.endswith(".py"):
            return

        bs = " \ ".strip()
        print(f"File {changed_file.split(bs)[-1]} has {event.event_type}. ")


def run():
    print("running...")

    if not check_existance("./run.py"):
        print('[ERROR] "run.py" DOES NOT EXISTS')
        exit()

    event_handler = FileChangeHandler()
    ob = Observer()
    ob.start()
    ob.schedule(event_handler, path="/", recursive=True)
    subprocess.Popen(
        ["python", "run.py"],
        shell=True,
    )
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nBOT IS OFF NOW")
        ob.stop()
