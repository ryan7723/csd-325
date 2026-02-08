#Ryan Barber Assignment  4.2 2/7/26

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


def get_col_index(header_row, possible_names, fallback_index):
    """
    Try to find a column index by searching header names.
    If not found, return the fallback index.
    """
    header_lower = [h.strip().lower() for h in header_row]

    for name in possible_names:
        name = name.strip().lower()
        if name in header_lower:
            return header_lower.index(name)

        return fallback_index


def load_weather_data(filename):
    """
    Reads the CSV once and returns:
      dates: list[datetime]
      highs: list[int]
      lows: list[int]
    Uses header names if available; otherwise falls back to the known indexes:
      date index 2, high index 5, low index 6
    """
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        #detect columns
        date_i = get_col_index(header_row, ["date"], 2)
        #headers based on NOAA-style
        high_i = get_col_index(header_row, ["tmax", "high", "highs"], 5)
        low_i = get_col_index(header_row, ["tmin", "low", "lows"], 6)

        for row in reader:
            try:
                current_date = datetime.strptime(row[date_i], "%Y-%m-%d")
                high = int(row[high_i])
                low = int(row[low_i])
            except (ValueError, IndexError):
                #skip any missing rows
                continue

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows

def plot_temps(dates, temps, color, title):
    """Plots the given temperature list against dates."""
    plt.close("all") #prevents multiple figures from stacking
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    plt.title(title, fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()


def main():
    filename = "sitka_weather_2018_simple.csv"
    # loads the data once, then plots based on user choice.
    dates, highs, lows = load_weather_data(filename)

    while True:
        print("\n=== Stika Weather Menu ===")
        print("Type one of the following options:")
        print("  highs - display high temperatures (red)")
        print("  lows - display low temperatures (blue)")
        print("  exit - exit the menu")

        choice = input("Your choice: ").strip().lower()

        if choice in ("highs", "h"):
            plot_temps(dates, highs, "red", "Daily high temperatures - 2018")
        elif choice in ("lows", "l"):
            plot_temps(dates, lows, "blue", "Daily low temperatures - 2018")
        elif choice in ("exit", "e", "q", "quit"):
            print("Exiting... Have a nice day and stay warm!")
            sys.exit(0)
        else:
            print("Invalid option. Please type: highs, lows, or exit.")

if __name__ == "__main__":
    main()
