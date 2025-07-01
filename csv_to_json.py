import csv
import json
import sys
import os

# Check if CSV filename is provided as argument
if len(sys.argv) != 2:
    print("Usage: python csv_to_json.py <csv_filename>")
    sys.exit(1)

# Input and output file paths
csv_filename = sys.argv[1]
# Always use the same output filename
json_filename = 'accountLookup.json'

lookup_dict = {}

try:
    with open(csv_filename, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            # Extract Account ID (remove quotes if present)
            account_id = row['Account ID'].strip('"')
            # Extract Name (remove quotes if present)
            name = row['Name'].strip('"')
            
            # Add to lookup dictionary
            lookup_dict[account_id] = name
            
except FileNotFoundError:
    print(f"Error: File '{csv_filename}' not found.")
    sys.exit(1)
except KeyError as e:
    print(f"Error: Required column {e} not found in CSV file.")
    print("Expected columns: 'Account ID', 'Name'")
    sys.exit(1)
except Exception as e:
    print(f"Error processing CSV file: {e}")
    sys.exit(1)

# Write out json
with open(json_filename, 'w', encoding='utf-8') as outfile:
    json.dump(lookup_dict, outfile, indent=2)

print(f"Successfully converted {csv_filename} to {json_filename}")
print(f"Created lookup dictionary with {len(lookup_dict)} account mappings")

