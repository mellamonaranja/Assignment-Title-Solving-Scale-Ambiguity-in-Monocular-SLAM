# Assignment-Title-Solving-Scale-Ambiguity-in-Monocular-SLAM

This project provides instructions to recover **metric scale** from a **monocular ORB-SLAM3 trajectory**, generate a scaled trajectory, and evaluate it quantitatively against **KITTI ground truth**.  
The workflow follows the evaluation procedure required in the SLAM assignment.

---

## 1. Prerequisites

### System
- Ubuntu 24.04
- ORB-SLAM3 
- Python ≥ 3.8

### Python Tools
Use a virtual environment to avoid system package conflicts:

```bash
python3 -m venv evo_env
source evo_env/bin/activate
pip install evo
```

## 2. Required Files
```bash
trajectory_unscaled.txt     # ORB-SLAM3 monocular output (TUM format)
trajectory_scaled.txt       # Output after scale correction
kitti06_gt_tum.txt          # KITTI sequence 06 ground truth (TUM format)
```

## 3. Run ORB-SLAM3 (Monocular)
```bash
./Examples/Monocular/mono_kitti \
  Vocabulary/ORBvoc.txt \
  Examples/Monocular/KITTI04-12.yaml \
  KITTI_DATASET/dataset/sequences/06
```

ORB-SLAM3 will generate:
```bash
KeyFrameTrajectory.txt
```

Rename it for clarity:
```bash
mv KeyFrameTrajectory.txt trajectory_unscaled.txt
```

## 4. Scale Estimation and Trajectory Scaling
```bash
evo_ape tum kitti06_gt_tum.txt trajectory_unscaled.txt \
  --align --correct_scale --verbose
```

From the output, record:
```bash
Scale correction: <SCALE_VALUE>
```

## 5. Quantitative Evaluation (ATE RMSE)
Before Scaling
```bash
evo_ape tum kitti06_gt_tum.txt trajectory_unscaled.txt \
  --align --verbose
```

After Scaling
```bash
evo_ape tum kitti06_gt_tum.txt trajectory_scaled.txt \
  --align --verbose
```

## 6. Visual Trajectory Comparison
```bash
evo_traj tum \
  kitti06_gt_tum.txt \
  trajectory_unscaled.txt \
  trajectory_scaled.txt \
  --ref kitti06_gt_tum.txt \
  --align \
  --plot \
  --plot_mode xy
```
