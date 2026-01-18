import numpy as np

gt = np.loadtxt("KITTI_DATASET/dataset/poses/06.txt")

with open("kitti06_gt_tum.txt", "w") as f:
    for i, p in enumerate(gt):
        tx, ty, tz = p[3], p[7], p[11]

        # identity quaternion (rotation not used for ATE translation error)
        f.write(f"{i} {tx} {ty} {tz} 0 0 0 1\n")
