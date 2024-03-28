#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
	""" Function find_peak from list."""
	if len(list_of_integers) == 0 :
		return None
	ls = list_of_integers
	ls.sort()
	return ls[-1]
