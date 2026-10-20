# Daily Coding Repository Cleanup Status

This repository has undergone a safe, non-destructive cleanup pass.

## What was changed safely
- Added `LICENSE`
- Added `.gitignore`
- Improved root `README.md`
- Added a structured, beginner-friendly copy layout under:
  - `python/daily/`
  - `python/dynamic_programming/`
  - `python/leetcode/`
  - `java/basics/`
  - `java/dsa/`

## Important note
The original files were kept in place to preserve the original learning history and avoid breaking any references.

## Structured copies are now the improved versions
The files under `python/` are no longer byte-for-byte copies of the root-level originals. These have been improved and should be treated as canonical:
- `python/dynamic_programming/stone_game.py` - added a general interval DP (`stoneGameDP`) next to the O(1) answer
- `python/dynamic_programming/climbing_stairs.py` - split the two shadowed `climb_stairs` definitions into `climb_stairs_optimized` and `climb_stairs_dp`
- `python/leetcode/0001_two_sum.py` - documented complexity and added edge-case asserts
- `python/leetcode/0003_fizz_buzz.py` - documented complexity and added self-checks

The root-level `dp1.py`, `dp2.py` and `6.py` are left untouched as learning history.

## Files that still require manual review before renaming or deletion
- `day3` (missing `.py` extension)
- `java-programs/3.java`
- `leetcode-problems/dayn.py`
- `leetcode-problems/rec overlap.py`
- `leetcode-problems/Majority Element.py`
- `leetcode-problems/Detail - Maximum Number of Words Found in Sentences.py`
- `6.py` vs `leetcode-problems/twosum.py` (possible duplicate problem solutions)

## Safe next steps
- Keep original files as-is
- Use structured copies as the clearer canonical references
- Review ambiguous files manually
- Only then decide whether to delete, rename, or archive them

## Goal
This approach preserves the learning history while making the repository easier to navigate without breaking existing workflows.
