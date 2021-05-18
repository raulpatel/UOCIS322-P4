"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

# globals for static information
CONTROLS = [0, 200, 400, 600, 1000, 1300]
SPANS = [0, 200, 200, 200, 400, 300]
MIN_SPEED = [0, 15.0, 15.0, 15.0, 11.428, 13.333]
MAX_SPEED = [0, 34.0, 32.0, 30.0, 28.0, 26.0]


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km > brevet_dist_km:
        return None
    # keeping track of segments
    index = 0
    # total of hours
    total = 0
    # determine how many full segments
    for dist in CONTROLS:
        if control_dist_km > dist:
            index += 1
    # add the times of the segments
    for i in range(1, index):
        total += SPANS[i]/MAX_SPEED[i]
    # add the partial segment
    if MIN_SPEED[index] != 0:
        total += (control_dist_km - CONTROLS[index - 1])/MAX_SPEED[index]

    return brevet_start_time.shift(hours=+total)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km > brevet_dist_km:
        return None
    index = 0
    total = 0
    for dist in CONTROLS:
        if control_dist_km > dist:
            index += 1
    # same but divide by minimum speed
    for i in range(1, index):
        total += SPANS[i]/MIN_SPEED[i]
    if MIN_SPEED[index] != 0:
        total += (control_dist_km - CONTROLS[index - 1])/MIN_SPEED[index]

    return brevet_start_time.shift(hours=+total)
