import csv
from collections import defaultdict

def analyze_results(csv_file):
    # Dictionary: ThreadGroup -> {Count, Time, Errors, ...}
    stats = defaultdict(lambda: {'count': 0, 'total_time': 0, 'min_time': float('inf'), 'max_time': 0, 'errors': 0})
    
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                thread_name = row['threadName']
                elapsed = int(row['elapsed'])
                success = row['success'] == 'true'
                
                # Identify group
                if "Thread Group 1" in thread_name:
                    group = "Group 1 - Basic"
                elif "Thread Group 2" in thread_name:
                    group = "Group 2 - Heavy"
                elif "Thread Group 3" in thread_name:
                    group = "Group 3 - Custom"
                else:
                    group = "Other"
                
                s = stats[group]
                s['count'] += 1
                s['total_time'] += elapsed
                s['min_time'] = min(s['min_time'], elapsed)
                s['max_time'] = max(s['max_time'], elapsed)
                if not success:
                    s['errors'] += 1
                    
        print("| Kịch bản | Samples | Avg Time (ms) | Min (ms) | Max (ms) | Error % | Throughput (est) |")
        print("|----------|---------|---------------|----------|----------|---------|------------------|")
        
        # Sort by group name
        for group in sorted(stats.keys()):
            s = stats[group]
            avg = s['total_time'] / s['count'] if s['count'] > 0 else 0
            error_rate = (s['errors'] / s['count']) * 100 if s['count'] > 0 else 0
            # Throughput estimation is hard without total duration of that specific group, 
            # but we can omit it or just provide counts/times.
            # I will leave throughput blank or calculate simply if I knew duration. 
            # For this report, Just Time and Error is good enough.
            print(f"| {group} | {s['count']} | {avg:.2f} | {s['min_time']} | {s['max_time']} | {error_rate:.2f}% | - |")
            
    except Exception as e:
        print(f"Error analyzing results: {e}")

if __name__ == "__main__":
    analyze_results('jmeter/results.csv')
