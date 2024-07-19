import json

def remove_slot(file_path, day, time):
    # Read the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Remove the specified time slot
    for period in ['weekdays', 'weekends']:
        for entry in data['availability'][period]:
            if entry['day'] == day:
                if time in entry['slots']:
                    entry['slots'].remove(time)
                    print(f"Removed {time} from {day}.")
                else:
                    print(f"{time} not found in {day}.")
                break
        else:
            continue
        break
    else:
        print(f"{day} not found.")
    
    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)



