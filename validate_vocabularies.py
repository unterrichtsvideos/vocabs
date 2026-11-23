#!/usr/bin/env python3
"""Validate all Turtle vocabulary files in this repository."""

from pathlib import Path
import argparse
import sys

try:
    from rdflib import Graph
except ImportError:
    print(
        "Missing dependency 'rdflib'. Install it with:\n"
        "  python -m pip install -r requirements.txt",
        file=sys.stderr,
    )
    raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Parse Turtle (.ttl) vocabulary files and report syntax errors."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="TTL files or directories to validate (defaults to the repository root)",
    )
    return parser.parse_args()


def find_ttl_files(paths: list[Path]) -> list[Path]:
    if not paths:
        paths = [Path(__file__).resolve().parent]

    files: set[Path] = set()
    for path in paths:
        if path.is_dir():
            files.update(path.rglob("*.ttl"))
        elif path.suffix.lower() == ".ttl":
            files.add(path)
    return sorted(files)


def main() -> int:
    args = parse_args()
    files = find_ttl_files(args.paths)
    if not files:
        print("No .ttl files found.", file=sys.stderr)
        return 1

    errors = 0
    for file_path in files:
        graph = Graph()
        try:
            graph.parse(file_path.as_posix(), format="turtle")
        except Exception as error:
            errors += 1
            print(f"FAIL {file_path}: {error}", file=sys.stderr)
        else:
            print(f"OK   {file_path}: {len(graph)} triples")

    if errors:
        print(f"\nValidation failed: {errors} of {len(files)} files contain errors.")
        return 1

    print(f"\nValidation passed: {len(files)} TTL files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
