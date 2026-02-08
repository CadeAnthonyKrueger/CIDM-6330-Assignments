import argparse
from pathlib import Path
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

def main():
    args = parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output_file)

    if not input_path.exists():
        print(f"Error: input file does not exist: {input_path}", file=sys.stderr)
        sys.exit(1)

    records_read = 0
    records_written = 0

    with input_path.open("r", newline="", encoding="utf-8") as infile, \
         output_path.open("w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []

        if not fieldnames:
            print("Error: input CSV has no header/fieldnames.", file=sys.stderr)
            sys.exit(1)

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            records_read += 1

            try:
                max_daily_temp = float(row.get("TMAX", ""))
                prcp = float(row.get("PRCP", ""))
            except (TypeError, ValueError):
                continue

            if args.temp_threshold_max is not None and max_daily_temp < args.temp_threshold_max:
                continue

            if args.prcp_min is not None and prcp < args.prcp_min:
                continue

            writer.writerow(row)
            records_written += 1

if __name__ == "__main__":
    main()
