import numpy as np

# -----------------------------
# Load ORB-SLAM3 keyframe trajectory (TUM format)
# timestamp tx ty tz qx qy qz qw
# -----------------------------
slam = np.loadtxt("KeyFrameTrajectory.txt")
slam_xyz = slam[:, 1:4]

# -----------------------------
# Load KITTI ground truth (poses/06.txt)
# R11 R12 R13 tx R21 R22 R23 ty R31 R32 R33 tz
# -----------------------------
gt = np.loadtxt("KITTI_DATASET/dataset/poses/06.txt")
gt_xyz = gt[:, [3, 7, 11]]

# -----------------------------
# Align lengths
# -----------------------------
N = min(len(slam_xyz), len(gt_xyz))
slam_xyz = slam_xyz[:N]
gt_xyz = gt_xyz[:N]
slam = slam[:N]

# -----------------------------
# Compute scale (least squares)
# -----------------------------
scale = np.sum(gt_xyz * slam_xyz) / np.sum(slam_xyz ** 2)
print(f"[INFO] Estimated scale = {scale:.6f}")

# -----------------------------
# Apply scale
# -----------------------------
slam_scaled = slam.copy()
slam_scaled[:, 1:4] *= scale

# -----------------------------
# Save scaled trajectory
# -----------------------------
np.savetxt(
    "trajectory_scaled.txt",
    slam_scaled,
    fmt="%.6f"
)

print("[INFO] trajectory_scaled.txt generated successfully")
