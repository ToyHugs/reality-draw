# Lib for manipulate vector in tuple

def point_on_segment(point_1: tuple[int, int], point_2: tuple[int, int], z: float) -> tuple[int, int]:
    """
    Return the point on the segment point_1 point_2 at the distance z (z in [0, 1]) from point_1
    """
    assert 0 <= z <= 1
    
    pos_x = int(point_1[0] + z * (point_2[0] - point_1[0]))
    pos_y = int(point_1[1] + z * (point_2[1] - point_1[1]))
    return (pos_x, pos_y)

def vector(point_1: tuple[int, int], point_2: tuple[int, int]) -> tuple[int, int]:
    """
    Return the vector from point_1 to point_2
    """
    pos_x = point_2[0] - point_1[0]
    pos_y = point_2[1] - point_1[1]
    return (pos_x, pos_y)

def map_point(origine: tuple[int, int], vector_x: tuple[int, int], vector_y: tuple[int, int], point_base: tuple[float, float]) -> tuple[int, int]:
    """
    Return the point in the new coordinate system - point_base coordinate system is [0; 1] x [0; 1]
    """
    assert 0 <= point_base[0] <= 1
    assert 0 <= point_base[1] <= 1

    pos_x = int(origine[0] + vector_x[0] * point_base[0] + vector_y[0] * point_base[1])
    pos_y = int(origine[1] + vector_x[1] * point_base[0] + vector_y[1] * point_base[1])

    return (pos_x, pos_y)