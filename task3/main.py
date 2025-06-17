import sys
from typing import List, Dict

def parse_log_line(line: str) -> Dict[str, str]:
    # Split the line into parts based on spaces
    parts = line.strip().split(' ', 3) 
    date_part = parts[0]
    time_part = parts[1]
    level_part = parts[2].upper()
    message_part = parts[3] 
    return {
        "date": date_part,
        "time": time_part,
        "level": level_part,
        "message": message_part
    }

def load_logs(file_path: str) -> List[Dict[str, str]]:
    # Load logs from a file and parse each line into a dictionary
    logs = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            logs.append(parsed_line)
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    # Filter logs by the specified log level
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    # Count the number of logs for each log level
    counts = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARNING": 0}
    for log in logs:
        counts[log.get("level").upper()] += 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    # Display the counts of logs by level in a formatted table
    print("Log level        | Quantity ")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) in (2, 3):
        # Display the total number of logs by level
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
    
    if len(sys.argv) == 3:
        # Filter logs by the specified level if provided
        level_to_filter = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level_to_filter)
        print(f"\nLog details for level '{level_to_filter}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()