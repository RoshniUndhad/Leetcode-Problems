# LeetCode Problem Solutions

A collection of Python solutions to LeetCode problems, organized by problem number. Solutions focus on clear implementations of common data structures and algorithmic patterns.

[![Language](https://img.shields.io/badge/Language-Python-3776AB?logo=python)](https://www.python.org/)
[![Problems](https://img.shields.io/badge/Problems-18-success)](#problem-index)

## Problem index

### Easy — 5

| # | Problem | Solution |
|---:|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](./1-two-sum/two-sum.py) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](./9-palindrome-number/palindrome-number.py) |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](./13-roman-to-integer/roman-to-integer.py) |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | [Python](./14-longest-common-prefix/longest-common-prefix.py) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python](./20-valid-parentheses/valid-parentheses.py) |

### Medium — 12

| # | Problem | Solution |
|---:|---|---|
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](./2-add-two-numbers/add-two-numbers.py) |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](./3-longest-substring-without-repeating-characters/longest-substring-without-repeating-characters.py) |
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](./5-longest-palindromic-substring/longest-palindromic-substring.py) |
| 6 | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [Python](./6-zigzag-conversion/zigzag-conversion.py) |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | [Python](./7-reverse-integer/reverse-integer.py) |
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [Python](./8-string-to-integer-atoi/string-to-integer-atoi.py) |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Python](./11-container-with-most-water/container-with-most-water.py) |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [Python](./15-3sum/3sum.py) |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | [Python](./16-3sum-closest/3sum-closest.py) |
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [Python](./17-letter-combinations-of-a-phone-number/letter-combinations-of-a-phone-number.py) |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | [Python](./18-4sum/4sum.py) |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Python](./19-remove-nth-node-from-end-of-list/remove-nth-node-from-end-of-list.py) |

### Hard — 1

| # | Problem | Solution |
|---:|---|---|
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](./4-median-of-two-sorted-arrays/median-of-two-sorted-arrays.py) |

**Total: 18 solutions** (5 Easy, 12 Medium, 1 Hard).

## Repository layout

Each problem directory contains its Python solution and a `README.md` with problem details.

```text
.
├── README.md
├── validate_solutions.py
├── 1-two-sum/
├── 2-add-two-numbers/
├── 3-longest-substring-without-repeating-characters/
├── 4-median-of-two-sorted-arrays/
├── 5-longest-palindromic-substring/
├── 6-zigzag-conversion/
├── 7-reverse-integer/
├── 8-string-to-integer-atoi/
├── 9-palindrome-number/
├── 11-container-with-most-water/
├── 13-roman-to-integer/
├── 14-longest-common-prefix/
├── 15-3sum/
├── 16-3sum-closest/
├── 17-letter-combinations-of-a-phone-number/
├── 18-4sum/
├── 19-remove-nth-node-from-end-of-list/
└── 20-valid-parentheses/
```

## Run the checks

Requires Python 3; no third-party packages are needed.

```bash
python3 validate_solutions.py
```

The validation script runs representative examples and edge cases for every solution module.

## Adding a solution

1. Create a directory named `<problem-number>-<problem-title>` with the solution and its problem `README.md`.
2. Add the module and sample/edge cases to `validate_solutions.py`.
3. Add the problem to the matching difficulty table above and update the solution totals.

## Author

Roshni Undhad
