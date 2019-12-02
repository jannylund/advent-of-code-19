#!/usr/bin/env python3
from timeit import default_timer as timer


def get_time(start_time):
    return str(round((timer() - start_time) * 1000, 4)) + " ms"
