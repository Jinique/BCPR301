# Refactoring Workbook Chapter 6 Duplication Challenge 1 (Exercise 14)

# Step 8 - return a list with items directly


class MissingPropertiesException(Exception):
    pass


def get_value(kargs, target, message1, message2=None):
    if target not in kargs:
        raise MissingPropertiesException(message1)
    value = kargs[target]
    if value <= 0:
        if not message2:
            raise MissingPropertiesException(message1 + " > 0")
        else:
            raise MissingPropertiesException(message2 + " > 0")
    return value


def check_value(value, check_interval, target):
    if (value % check_interval) != 0:
        raise MissingPropertiesException(target + " % checkInterval")


def get_times(**kargs):
    #    if "interval" not in kargs:
    #        raise MissingPropertiesException("monitor interval")
    #    value = kargs["interval"]
    #    if value <= 0:
    #        raise MissingPropertiesException("monitor interval > 0")

    #    check_interval = value
    check_interval = get_value(kargs, "interval", "monitor interval")

    #    if "duration" not in kargs:
    #        raise MissingPropertiesException("duration")
    #    value = kargs["duration"]
    #    if value <= 0:
    #        raise MissingPropertiesException("duration > 0")

    #    value = get_value(kargs, "duration", "duration")
    monitor_time = get_value(kargs, "duration", "duration")
    #    if (value % check_interval) != 0:
    #        raise MissingPropertiesException("duration % check_interval")
    check_value(monitor_time, check_interval, "duration")

    #    monitor_time = value
    #    if "departure" not in kargs:
    #        raise MissingPropertiesException("departure offset")
    #    value = kargs["departure"]
    #    if value <= 0:
    #        raise MissingPropertiesException("departure > 0")

    #    value = get_value(kargs, "departure", "departure offset", "departure")
    departure_offset = get_value(kargs, "departure", "departure offset",
                               "departure")
    #    if (value % check_interval) != 0:
    #        raise MissingPropertiesException("departure % check_interval")
    check_value(departure_offset, check_interval, "departure")

    #    departure_offset = value

    #    result = []
    #    result.append(check_interval)
    #    result.append(monitor_time)
    #    result.append(departure_offset)
    #    return result
    return [check_interval, monitor_time, departure_offset]


if __name__ == "__main__":
    # print(get_times(interval=10, duration=50, departure=12))
    print(get_times(interval=10, duration=10, departure=20))
