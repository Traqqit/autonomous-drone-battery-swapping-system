"""Monte Carlo sampled workspace: illustrative, not collision checked."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'python'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from battery_swap.kinematics import Arm
rng=np.random.default_rng(42)
n=1500
# Arbitrary demonstration limits; must be verified against CAD and hardware.
lo=np.deg2rad([-180,-45,-145,-90])
hi=np.deg2rad([180,120,0,90])
q=rng.uniform(lo,hi,size=(n,4))
xyz=np.array([Arm().tool_position(angles) for angles in q])
fig=plt.figure(figsize=(7,5))
ax=fig.add_subplot(111,projection='3d')
ax.scatter(xyz[:,0],xyz[:,1],xyz[:,2],s=3,alpha=.35)
ax.set(xlabel='X (m)',ylabel='Y (m)',zlabel='Z (m)',
       title='Sampled 4R arm workspace (illustrative)')
fig.tight_layout()
out=Path(__file__).with_name('workspace_sample.png')
fig.savefig(out,dpi=140)
print('Saved:',out)
