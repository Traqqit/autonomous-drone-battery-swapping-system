# 2025 baseline data — transcription from the university report

`trials.csv` transcribes Tables 4.1 and 4.2 of the submitted report.
`duration_s` is blank for failed swaps because the report lists N/A.
Do not interpret missing duration as zero.

The report reports 12/20 successful swaps = 60%, with approximately 90 s
average among successful trials. The battery objects were replicas, not
energized flight batteries; no charging tests were performed.

Run `python examples/analyze_baseline.py` to reproduce the counts and mean.
