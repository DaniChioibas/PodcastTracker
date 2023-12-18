def ms_to_hh_mm(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return "{:2} Hours {:2} minutes".format(int(hours), int(minutes))