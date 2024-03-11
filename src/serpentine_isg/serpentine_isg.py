"""Main module."""
from __future__ import annotations

from csv import reader, writer
from dataclasses import dataclass
from functools import cmp_to_key
from typing import TYPE_CHECKING, NewType

from rich import print

if TYPE_CHECKING:
    from pathlib import Path

HeaderRow = NewType("HeaderRow", tuple[str, str, str, str, str])
ValueRow = NewType("ValueRow", tuple[int, int, int, int, float])


def column_sort(a: tuple, b: tuple) -> int:
    """Sort by column in a serpentine pattern."""
    n = a[3] - b[3]
    if n != 0:
        return n
    if a[3] % 2 == 0:
        return b[2] - a[2]
    return a[2] - b[2]


def row_sort(a: tuple, b: tuple) -> int:
    """Sort by row in a serpentine pattern."""
    n = a[2] - b[2]
    if n != 0:
        return n
    if a[2] % 2 == 0:
        return b[3] - a[3]
    return a[3] - b[3]


@dataclass
class Data:
    """Data class for sorting."""

    header: HeaderRow
    values: list[ValueRow]
    sort_function: callable[[ValueRow, ValueRow], int]

    def head(self: Data) -> list[ValueRow]:
        """Return the first 5 rows."""
        return self.values[:5]

    def sort(self: Data) -> list[ValueRow]:
        """Sort the values using the sort function provided during initialization."""
        func = self.sort_function
        return [self.values[0], *sorted(self.values[1:], key=cmp_to_key(func))]

    def __len__(self: Data) -> int:
        """Return the number of rows."""
        return len(self.values)

    def print(self: Data) -> None:
        """Print the first 25 rows using rich formatting."""
        result = ""
        for i in self.values[:25]:
            result += (
                f"{i[0]} {i[1]} [bold white]{i[2]}[/bold white]",
                f" [bold white]{i[3]}[/bold white] {i[4]}\n",
            )
        print(result)


def write_values(path: Path, header: HeaderRow, values: list[ValueRow]) -> None:
    """Write values to a csv file."""
    with path.open("w") as f:
        csv_writer = writer(f, delimiter=",")
        csv_writer.writerow(header)
        csv_writer.writerows(values)


def read_values(
    path: Path,
) -> tuple[HeaderRow, list[ValueRow]]:
    """Read values from a csv file and convert them to numerical."""
    header: HeaderRow = None
    values: list[ValueRow] = []
    with path.open() as f:
        csv_reader = reader(f, delimiter=",")
        # add header withouth casting the values
        header = tuple(next(csv_reader))
        values.extend(
            (int(line[0]), int(line[1]), int(line[2]), int(line[3]), float(line[4]))
            for line in csv_reader
        )
    return header, values


def process_file(file_path: Path, orientation: str) -> None:
    """Process a file."""
    header, values = read_values(file_path)
    sort_function = column_sort if orientation == "column" else row_sort
    data = Data(header, values, sort_function)
    sorted_data = data.sort()
    output_file = file_path.with_name(
        f"{file_path.stem}_sorted_{orientation}{file_path.suffix}",
    )
    write_values(output_file, data.header, sorted_data)
