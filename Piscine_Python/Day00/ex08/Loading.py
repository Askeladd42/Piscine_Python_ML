def ft_tqdm(lst: range):
    """A simple tqdm implementation: prints a progress bar
    and percentage of completion. Since no functions are allowed, not adapted
    to all size of terminal compared to the original tqdm."""
    total = len(lst)
    bar_length = 61  # size of the progress bar, to ajust manually if needed
    for i, item in enumerate(lst):
        percent = (i + 1) / total * 100
        filled_length = int(bar_length * (i + 1) // total)
        bar = '[' + '=' * filled_length + '>' + ']' + \
              '-' * (bar_length - filled_length)
        print(f'\r{percent:3.0f}%|{bar}| {i + 1}/{total}', end='\r')
        yield item
    print()
