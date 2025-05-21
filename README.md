# BigWeather - Dyno Bucket Optimization

This project solves an optimization problem for a distributed weather forecasting system (BigWeather) using graph algorithms and exhaustive search. Each compute unit (dyno) must have access to a high-performance data cache (bucket), either locally or via a bond to a neighboring dyno. The goal is to find the **cheapest configuration** for this setup.

# Problem Description

Given:
- A set of dynos and possible pairwise connections (edges)
- Cost of assigning a bucket to a dyno
- Cost of establishing a bond between dynos

Find the configuration of bucket placements and bonds such that:
1. Every dyno has access to a bucket (either directly or via a bond)
2. The **total cost is minimized**

### Bonus:
- Count the number of cheapest configurations
- Visualize one optimal solution

---

## ▶ How to Run

1. Make sure Python 3 is installed.
2. Clone the repository or download the files.
3. Run the main script:

```bash
python BigWeatherFinal.py


4. When prompted, enter the absolute path to your input file.


Input Format
An input file must follow this structure:

n k bucket_cost bond_cost
u1 v1
u2 v2
...
uk vk


Where:

n is the number of dynos

k is the number of bonds

Each ui vi pair represents a possible bond


Example:

6 5 4 3
1 2
1 3
4 5
6 4
2 3


Output

The script prints:

Minimum cost to satisfy all dynos

Number of such cheapest configurations (if multiple)

One valid configuration (which dynos host buckets)


Output example:

Cheapest: 20
Number of cheapest configurations: 3

One cheapest solution (bucket placements):
Component [1, 2, 3]: Buckets on [1]
Component [4, 5, 6]: Buckets on [4]


