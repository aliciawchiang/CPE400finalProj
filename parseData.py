import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('export.xml')
root = tree.getroot()

# Find all heart rate records
heart_rate_records = root.findall('.//Record[@type="HKQuantityTypeIdentifierHeartRate"]')

# Extract relevant information from each record
heart_rate_data = []
for record in heart_rate_records:
    date_time = record.attrib['creationDate']
    heart_rate = float(record.attrib['value'])
    heart_rate_data.append({'date_time': date_time, 'heart_rate': heart_rate})

# Save heart rate data to a new file
with open('heart_rate_data.csv', 'w') as f:
    # Write header
    f.write("Date Time,Heart Rate\n")
    # Write data
    for data_point in heart_rate_data:
        f.write(f"{data_point['date_time']},{data_point['heart_rate']}\n")

print("Heart rate data saved to heart_rate_data.csv")
