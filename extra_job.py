def make_readable(second):
    return f"{'{:02}'.format(second//3600)}:{'{:02}'.format(second//60%60)}:{'{:02}'.format(second%60)}"


print(make_readable(0))            # "00:00:00"
print(make_readable(5))            # "00:00:05"
print(make_readable(60))           # "00:01:00"
print(make_readable(86_399))       # "23:59:59"
print(make_readable(359_999))      # "99:59:59"
