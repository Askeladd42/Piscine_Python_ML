import time, datetime

current_time_sec = time.time()
scientific_notation = f"{current_time_sec:.2e}"
current_date = datetime.datetime.now()
formatted_date = current_date.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {current_time_sec:,.4f} or {scientific_notation} in scientific notation")
print(formatted_date)