from pathlib import Path
from datetime import datetime
import argparse
import json
import csv
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description="Filter weather station CSV data by maximum daily temperature and/or precipitation thresholds."
    )

    parser.add_argument(
        "input",
        type=Path,
        help="Path to input CSV file containing weather data",
    )

    parser.add_argument(
        "output_csv",
        type=Path,
        help="Path to output CSV file for filtered results",
    )

    ### Only 2 filtering parameters for the sake of the exercise ###
    parser.add_argument(
        "--temp-threshold-max",
        type=float,
        help="Minimum daily maximum temperature required for a record to be included"
    )

    parser.add_argument(
        "--prcp-min",
        type=float,
        help="Minimum precipitation value required for a record to be included (0.00–1.00)"
    )
    ################################################################

    parser.add_argument(
        "--log-file",
        type=Path,
        default=Path("weather_filter.log"),
        help="Path to log file (default: weather_filter.log)",
    )

    return parser.parse_args()

def read_records(input_path):
    ext = input_path.suffix.lower()

    if ext == ".csv":
        return read_csv(input_path)

    elif ext == ".json":
        return read_json(input_path)

    else:
        raise ValueError(f"Unsupported file format: {ext}. Use .csv or .json.")

def read_csv(input_path):
    with input_path.open("r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        records = list(reader)
        fieldnames = reader.fieldnames or []

        if not fieldnames:
            raise ValueError("CSV has no headers")

    return records, fieldnames

def read_json(input_path):
    with input_path.open("r", encoding="utf-8") as infile:
        records = json.load(infile)

    if not isinstance(records, list):
        raise ValueError("JSON must be a list of records")

    fieldnames = list(records[0].keys()) if records else []
    return records, fieldnames

def write_csv(output_path, records, fieldnames):
    with output_path.open("w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

def filter_records(records, args):
    filtered_records = []

    for row in records:
        if args.temp_threshold_max is not None:
            try:
                max_daily_temp = float(row.get("TMAX", ""))
            except (TypeError, ValueError):
                continue
            if max_daily_temp < args.temp_threshold_max:
                continue

        if args.prcp_min is not None:
            try:
                prcp = float(row.get("PRCP", ""))
            except (TypeError, ValueError):
                continue
            if prcp < args.prcp_min:
                continue

        filtered_records.append(row)

    return filtered_records

def log_operation(log_path: Path, read_count: int, written_count: int):
    timestamp = timestamp = datetime.now().isoformat()

    log_entry = (
        f"{timestamp} | "
        f"records_read={read_count} | "
        f"records_written={written_count}\n"
    )

    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

def main():
    args = parse_args()

    input_path = args.input
    output_path = args.output_csv

    if not input_path.exists():
        print(f"Error: input file does not exist: {input_path}", file=sys.stderr)
        sys.exit(1)

    try:
        records, fieldnames = read_records(input_path)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    filtered_records = filter_records(records, args)

    write_csv(output_path, filtered_records, fieldnames)

    records_read = len(records)
    records_written = len(filtered_records)

    log_operation(args.log_file, records_read, records_written)

    print(
        f"Done. Read {records_read} records, "
        f"wrote {records_written} records."
    )

if __name__ == "__main__":
    main()
