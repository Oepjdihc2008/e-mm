"""Produce the same competition artwork on every run."""

from pathlib import Path
import shutil


SOURCE = Path(__file__).with_name("art.jpg")
DESTINATION = Path("/output/entry.png")


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)


if __name__ == "__main__":
    main()
