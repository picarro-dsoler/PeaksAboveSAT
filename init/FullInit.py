import runpy
import sys
from pathlib import Path


def _find_project_root() -> Path:
    init_dir = Path(__file__).resolve().parent
    root = init_dir.parent
    if (root / "locallib").is_dir() and (root / "lib" / "tables").is_dir():
        return root
    raise FileNotFoundError(
        f"Could not find PeakAboveSAT root (locallib + lib/tables). cwd={Path.cwd()!r}"
    )


PROJECT_ROOT = _find_project_root()
INIT_DIR = Path(__file__).resolve().parent

_project_root_str = str(PROJECT_ROOT)
sys.path = [_project_root_str] + [p for p in sys.path if p != _project_root_str]


def main() -> None:
    print("=== Running Setup.py ===")
    runpy.run_path(str(INIT_DIR / "Setup.py"), run_name="__main__")

    print("\n=== Running PeaksAboveSAT_Init.py ===")
    runpy.run_path(str(INIT_DIR / "PeaksAboveSAT_Init.py"), run_name="__main__")

    print("\nFull initialization complete.")


if __name__ == "__main__":
    main()
