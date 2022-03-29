import argparse
import hashlib
import time
import subprocess


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--f")
    parser.add_argument("-a", "--a")
    return parser.parse_args()


def get_hash_of_file(f):
    return hashlib.md5(open(f, "r").read().encode()).hexdigest()


def compare_hash(h1, h2):
    return h1 == h2


def run_program(f, a):
    return subprocess.Popen((["py", f, a if a else ""]))


if __name__ == "__main__":
    args = get_args()
    program = run_program(args.f, args.a)
    previous_hash = get_hash_of_file(args.f)
    while True:
        new_hash = get_hash_of_file(args.f)
        if previous_hash != new_hash:
            print("Change detected in file, restarting.")
            program.terminate()
            program = run_program(args.f, args.a)
            previous_hash = new_hash
        time.sleep(1)
