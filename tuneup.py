#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Justin Rhuebottom"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def wrapper(*args, **kw):
        pr = cProfile.Profile()
        pr.enable()
        x = pr.runcall(func, *args, **kw)
        pr.disable()
        # pr.print_stats()
        Stats = pstats.Stats(pr).sort_stats("cumulative")
        Stats.print_stats()
        return x
    return wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    # while movies:
    #     movie = movies.pop()
    #     if is_duplicate(movie, movies):
    #         duplicates.append(movie)
    while movies:
        movie = movies.pop()
        if movie in movies:
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(setup="from __main__ import main", stmt="main()")
    result = t.repeat(repeat=3, number=10)
    result.sort()
    bestTime = result[0] / 10
    print(f"Best time across 3 repeats of 10 runs per repeat: {bestTime} sec")


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    timeit_helper()
    main()
