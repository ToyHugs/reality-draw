import numpy as np


def add_numbers(a, b):
    return a + b


def compute_homography(src_pts, dst_pts):
    """
    src_pts, dst_pts: np.array shape (4, 2) — 4 points (x, y)
    Returns H: np.array shape (3, 3)
    """

    A = []
    for (x, y), (xp, yp) in zip(src_pts, dst_pts):
        A.append([-x, -y, -1,  0,  0,  0, x*xp, y*xp, xp])
        A.append([0,  0,  0, -x, -y, -1, x*yp, y*yp, yp])

    A = np.array(A)

    # Solve Ah = 0 with SVD
    _, _, Vt = np.linalg.svd(A)
    h = Vt[-1, :]  # last row of V (corresponds to smallest singular value)
    H = h.reshape((3, 3))

    return H / H[2, 2]  # normalize so that H[2,2] = 1
