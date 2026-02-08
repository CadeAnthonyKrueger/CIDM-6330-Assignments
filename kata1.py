import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description="Filter weather station CSV data by maximum daily temperature threshold."
    )

    parser.add_argument(
        "input_csv",
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
        required=True,
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