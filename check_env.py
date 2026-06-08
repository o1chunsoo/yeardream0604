import importlib
import sys


def check(module_name: str, display_name: str | None = None) -> None:
    name = display_name or module_name
    try:
        mod = importlib.import_module(module_name)
        version = getattr(mod, "__version__", "(no version info)")
        print(f"  [OK]   {name:20s} {version}")
    except ImportError:
        print(f"  [MISS] {name:20s} not installed")


def main() -> None:
    print("=" * 50)
    print("Environment Check")
    print("=" * 50)
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")
    print()
    print("Packages:")
    for pkg in ["jupyterlab", "numpy", "pandas", "matplotlib", "sklearn"]:
        check(pkg)
    print("=" * 50)


if __name__ == "__main__":
    main()
