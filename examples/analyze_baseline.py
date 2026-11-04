"""Reproduce descriptive statistics from 2025 report trial tables."""
from pathlib import Path
import csv
from statistics import mean
path=Path(__file__).resolve().parents[1]/'experiments/baseline_2025/trials.csv'
with path.open(newline='') as f:
    rows=list(csv.DictReader(f))
success=[r for r in rows if r['success']=='1']
times=[float(r['duration_s']) for r in success]
print(f"Attempts: {len(rows)}")
print(f"Successful: {len(success)}")
print(f"Success rate: {100*len(success)/len(rows):.1f}%")
print(f"Mean successful-trial duration: {mean(times):.2f} s")
print(f"Failure reasons: {sorted(set(r['failure_reason'] for r in rows if r['failure_reason']))}")
