import argparse
import sys
from .LibCore import raw_input 

class Cli:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="luah")
        self._setup_arguments()
        self.args = self.parser.parse_args()

        if self.args.file:
            self.process_file(self.args.file)
        elif len(sys.argv) > 1 and sys.argv[1].endswith(".lua"):
            self.process_file(sys.argv[1])

    def _setup_arguments(self):
        self.parser.add_argument("--version", action="version", version="luah 0.1.0")
        self.parser.add_argument("--verbose", action="store_true", help="verbose mode")
        self.parser.add_argument("--debug", action="store_true", help="debug mode")
        self.parser.add_argument("--quiet", action="store_true", help="quiet mode")
        self.parser.add_argument("--config", help="config file")
        self.parser.add_argument("--file", help="file to process")
        self.parser.add_argument("--log", help="log file")
        self.parser.add_argument("--log-level", help="log level")
        self.parser.add_argument("--log-format", help="log format")
        self.parser.add_argument("--log-date-format", help="log date format")
        self.parser.add_argument("--log-file-max-size", help="log file max size")
        self.parser.add_argument("--log-file-backup-count", help="log file backup count")
        self.parser.add_argument("--log-file-rotation-count", help="log file rotation count")
        self.parser.add_argument("--log-file-rotation-interval", help="log file rotation interval")
        self.parser.add_argument("--log-file-rotation-backup-count", help="log file rotation backup count")
        self.parser.add_argument("--log-file-rotation-backup-interval", help="log file rotation backup interval")

    def process_file(self, file_name):
        try:
            raw_input(file_name)
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

    def get_args(self):
        return self.args

    def get_help(self):
        return self.parser.format_help()

if __name__ == "__main__":
    cli = Cli()
    args = cli.get_args()
    if args.verbose:
        print("Verbose mode is enabled.")
