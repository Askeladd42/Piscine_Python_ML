import time


def ft_tqdm(lst: range):
    """A simple tqdm implementation: prints a progress bar
    and percentage of completion."""
    total = len(lst)
    bar_length = 40
    for i, item in enumerate(lst):
        percent = (i + 1) / total * 100
        filled_length = int(bar_length * (i + 1) // total)
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        print(f'\r|{bar}| {percent:.2f}%', end='\r')
        yield item
        time.sleep(0.1)  # Simulate work being done
    print()
