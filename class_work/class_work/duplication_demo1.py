class MissingPropertiesException(Exception):
    pass


def get_times(**kargs):
    if ("interval" in kargs) == 0:
        raise MissingPropertiesException("monitor interval")
    value = kargs["interval"]

    if (value <= 0):
        raise MissingPropertiesException("monitor interval > 0")
    check_interval = value

    if ("duration" in kargs) == 0:
        raise MissingPropertiesException("duration")
    value = kargs["duration"]
    if (value <= 0):
        raise MissingPropertiesException("duration > 0")
    if ((value % check_interval) != 0):
        raise MissingPropertiesException("duration % check_interval")
    monitor_time = value

    if ("departure" in kargs) == 0:
        raise MissingPropertiesException("departure offset")
    value = kargs["departure"]
    if (value <= 0):
        raise MissingPropertiesException("departure > 0")
    if ((value % check_interval) != 0):
        raise MissingPropertiesException("departure % check_interval")
    departure_offset = value

    result = []
    result.append(check_interval)
    result.append(monitor_time)
    result.append(departure_offset)
    return result


if __name__ == "__main__":
    # print(get_times(interval=10, duration=50, departure=12))
    print(get_times(interval=10, duration=10, departure=20))
