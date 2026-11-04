import csv
import unittest
from pathlib import Path
from statistics import mean

class BaselineTests(unittest.TestCase):
    def test_transcribed_results(self):
        file=Path(__file__).resolve().parents[1]/'experiments/baseline_2025/trials.csv'
        with file.open(newline='') as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),20)
        success=[r for r in rows if r['success']=='1']
        self.assertEqual(len(success),12)
        self.assertAlmostEqual(mean(float(r['duration_s']) for r in success),89.925,places=3)
        self.assertEqual(sum(r['failure_reason']=='gripper_failed_to_secure_battery' for r in rows),1)
