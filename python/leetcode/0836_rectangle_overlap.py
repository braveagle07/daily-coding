"""LeetCode 836 - Rectangle Overlap.

A rectangle is [x1, y1, x2, y2] (bottom-left, top-right). Two rectangles
overlap only if their intersection has positive area, so rectangles that
merely touch at an edge or a corner do NOT overlap.

Easier to reason about the opposite case: they do not overlap if one is
completely to the left of, to the right of, below, or above the other.
That is why every comparison uses <= / >= (touching counts as separated).
Time: O(1), Space: O(1)
"""


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (
            rec1[2] <= rec2[0]  # rec1 is left of rec2
            or rec1[0] >= rec2[2]  # rec1 is right of rec2
            or rec1[3] <= rec2[1]  # rec1 is below rec2
            or rec1[1] >= rec2[3]  # rec1 is above rec2
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]) is True
    assert solution.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]) is False  # share an edge
    assert solution.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]) is False  # far apart
    assert solution.isRectangleOverlap([0, 0, 1, 1], [1, 1, 2, 2]) is False  # share a corner
    assert solution.isRectangleOverlap([0, 0, 4, 4], [1, 1, 2, 2]) is True  # one inside the other
    print("All Rectangle Overlap checks passed")
