import os
import time
import numpy as np
import pandas as pd

from balancedIntervalTree import Interval
from balancedIntervalTree import BalancedIntervalTree


def days_since_reference(date, reference_date):
    return (date - reference_date).days


def search(df, reference_date, interval_queries):
    # Build intervals from the data
    intervals = []
    for index, row in df.iterrows():
        start_date = row['D.O.A']
        end_date = row['D.O.D'] if pd.notna(row['D.O.D']) else start_date

        # Convert dates to integer (days since reference)
        start_day = days_since_reference(start_date, reference_date)
        end_day = days_since_reference(end_date, reference_date)

        intervals.append(Interval(start_day, end_day))

    # Sort intervals and build the balanced tree directly
    intervals.sort(key=lambda interval: interval.low)
    balancedTree_index = BalancedIntervalTree()
    start_time = time.time()
    balancedTree_index.root = balancedTree_index.buildBalancedTree(intervals, start=0, end=len(intervals) - 1)
    tree_build_time = time.time() - start_time
    print(f"Time to build the tree: {tree_build_time} seconds")   # time : 0.01459503173828125 seconds

    # Process queries
    times = []
    start_time = time.time()
    for index, row in interval_queries.iterrows():
        start_date = row['start_date']
        end_date = row['end_date']

        # Convert the query interval into integer (days since reference)
        start_day = days_since_reference(start_date, reference_date)
        end_day = days_since_reference(end_date, reference_date)

        # Define the interval query using the integer representation
        query_interval = Interval(start_day, end_day)
        results = []

        # Search for overlapping intervals
        query_start_time = time.time()
        balancedTree_index.isOverlapping(balancedTree_index.root, query_interval, results)
        query_end_time = time.time()
        query_time = query_end_time - query_start_time
        times.append(query_time)
        print(f"Results for query {index + 1} [{start_day} to {end_day}]: {len(results)} matching entries")

    return times



def main():
    df = pd.read_csv("shuffled_HDHI.csv")
    df['D.O.A'] = pd.to_datetime(df['D.O.A'], errors='coerce')
    df['D.O.D'] = pd.to_datetime(df['D.O.D'], errors='coerce')

    # Remove rows where 'D.O.A' is NaT (missing values)
    df = df.dropna(subset=['D.O.A'])
    reference_date = df['D.O.A'].min()

    interval_queries = pd.read_csv("mixed_interval_queries_10K.csv")  # CPU time for scan = 5.349354982376099 seconds
    interval_queries['start_date'] = pd.to_datetime(interval_queries['start_date'], errors='coerce')
    interval_queries['end_date'] = pd.to_datetime(interval_queries['end_date'], errors='coerce')

    print("interval_queries['start_date']  = ", interval_queries['start_date'])

    start_time = time.time()
    times = search(df, reference_date, interval_queries)
    end_time = time.time()
    cpu_time = end_time - start_time
    print("CPU time for scan =", cpu_time, "seconds")
    np.save("Times_mixed.npy", times)


if __name__ == "__main__":
    main()
