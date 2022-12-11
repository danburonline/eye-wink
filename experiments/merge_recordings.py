"""This script merges the markers.csv and eeg.csv files into a single file"""
import csv

# Set the maximum difference in timestamp between the markers and EEG data
# to consider them "aligned"
MAX_TIMESTAMP_DIFF = 0.1

# Read the markers from the markers.csv file
markers = []
with open("markers.csv") as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    for row in reader:
        timestamp = float(row[0])
        marker = row[1]
        markers.append((timestamp, marker))

# Read the eeg data from the eeg.csv file
eeg_data = []
with open("eeg.csv") as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    for row in reader:
        timestamp = float(row[0])
        ch1 = float(row[1])
        eeg_data.append((timestamp, ch1))

merged = []
MARKER_INDEX = 0
for timestamp, ch1 in eeg_data:
    # If the timestamp of the current marker is within the maximum
    # allowed difference from the timestamp of the current eeg data,
    # and if the marker_index is within the bounds of the markers list,
    # append the marker to the merged data
    if (
        MARKER_INDEX < len(markers)
        and abs(timestamp - markers[MARKER_INDEX][0]) < MAX_TIMESTAMP_DIFF
    ):
        merged.append((timestamp, ch1, markers[MARKER_INDEX][1]))
        MARKER_INDEX += 1
    else:
        merged.append((timestamp, ch1))

# Write the merged data to a new csv file
with open("merged.csv", "w") as f:
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(["timestamp", "ch1", "marker"])
    for row in merged:
        writer.writerow(row)
