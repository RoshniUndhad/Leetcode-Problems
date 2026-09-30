import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def make_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def load_solution(problem_dir, file_name, class_name):
    module_path = ROOT / problem_dir / file_name
    spec = importlib.util.spec_from_file_location(problem_dir.replace("-", "_"), module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load solution module: {module_path}")

    module = importlib.util.module_from_spec(spec)
    if problem_dir in {"2-add-two-numbers", "19-remove-nth-node-from-end-of-list"}:
        module.ListNode = ListNode
    spec.loader.exec_module(module)
    return getattr(module, class_name)()


TESTS = [
    (
        "1-two-sum",
        "two-sum.py",
        "Solution",
        "twoSum",
        [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])],
    ),
    (
        "11-container-with-most-water",
        "container-with-most-water.py",
        "Solution",
        "maxArea",
        [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([4, 3, 2, 1, 4], 16)],
    ),
    (
        "13-roman-to-integer",
        "roman-to-integer.py",
        "Solution",
        "romanToInt",
        [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)],
    ),
    (
        "14-longest-common-prefix",
        "longest-common-prefix.py",
        "Solution",
        "longestCommonPrefix",
        [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""), (["leetcode"], "leetcode")],
    ),
    (
        "15-3sum",
        "3sum.py",
        "Solution",
        "threeSum",
        [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
        ],
    ),
    (
        "16-3sum-closest",
        "3sum-closest.py",
        "Solution",
        "threeSumClosest",
        [([-1, 2, 1, -4], 1, 2), ([0, 0, 0], 1, 0), ([1, 1, 1, 0], 100, 3)],
    ),
    (
        "17-letter-combinations-of-a-phone-number",
        "letter-combinations-of-a-phone-number.py",
        "Solution",
        "letterCombinations",
        [
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ("", []),
            ("2", ["a", "b", "c"]),
        ],
    ),
    (
        "18-4sum",
        "4sum.py",
        "Solution",
        "fourSum",
        [
            ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
            ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
            ([1, 2, 3], 6, []),
        ],
    ),
    (
        "19-remove-nth-node-from-end-of-list",
        "remove-nth-node-from-end-of-list.py",
        "Solution",
        "removeNthFromEnd",
        [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]), ([1], 1, []), ([1, 2], 1, [1])],
    ),
    (
        "20-valid-parentheses",
        "valid-parentheses.py",
        "Solution",
        "isValid",
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([)]", False),
            ("{[]}", True),
        ],
    ),
    (
        "2-add-two-numbers",
        "add-two-numbers.py",
        "Solution",
        "addTwoNumbers",
        [
            (make_linked_list([2, 4, 3]), make_linked_list([5, 6, 4]), [7, 0, 8]),
            (make_linked_list([0]), make_linked_list([0]), [0]),
            (make_linked_list([9, 9, 9, 9, 9, 9, 9]), make_linked_list([9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
        ],
    ),
    (
        "3-longest-substring-without-repeating-characters",
        "longest-substring-without-repeating-characters.py",
        "Solution",
        "lengthOfLongestSubstring",
        [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)],
    ),
    (
        "4-median-of-two-sorted-arrays",
        "median-of-two-sorted-arrays.py",
        "Solution",
        "findMedianSortedArrays",
        [([1, 3], [2], 2.0), ([1, 2], [3, 4], 2.5), ([0, 0], [0, 0], 0.0)],
    ),
    (
        "5-longest-palindromic-substring",
        "longest-palindromic-substring.py",
        "Solution",
        "longestPalindrome",
        [("babad", "bab"), ("cbbd", "bb"), ("a", "a")],
    ),
    (
        "6-zigzag-conversion",
        "zigzag-conversion.py",
        "Solution",
        "convert",
        [
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("A", 1, "A"),
            ("AB", 3, "AB"),
            ("ABCDEF", 2, "ACEBDF"),
        ],
    ),
    (
        "7-reverse-integer",
        "reverse-integer.py",
        "Solution",
        "reverse",
        [(123, 321), (-123, -321), (120, 21), (1534236469, 0)],
    ),
    (
        "8-string-to-integer-atoi",
        "string-to-integer-atoi.py",
        "Solution",
        "myAtoi",
        [("42", 42), ("   -42", -42), ("4193 with words", 4193), ("words and 987", 0)],
    ),
    (
        "9-palindrome-number",
        "palindrome-number.py",
        "Solution",
        "isPalindrome",
        [(121, True), (-121, False), (10, False), (12321, True)],
    ),
]


def run_case(name, file_name, class_name, method_name, case):
    module_path = ROOT / name / file_name
    if not module_path.exists():
        raise FileNotFoundError(f"Missing test target: {module_path}")

    instance = load_solution(name, file_name, class_name)
    method = getattr(instance, method_name)
    if name == "2-add-two-numbers":
        left, right, expected = case
        actual = method(left, right)
        assert linked_list_to_list(actual) == expected, (
            f"{name}: expected {expected}, got {linked_list_to_list(actual)}"
        )
        return

    if name == "19-remove-nth-node-from-end-of-list":
        values, n, expected = case
        actual = linked_list_to_list(method(make_linked_list(values), n))
        assert actual == expected, f"{name}: expected {expected}, got {actual}"
        return

    if method_name == "twoSum":
        nums, target, expected = case
        actual = method(nums, target)
        assert actual == expected, f"{name}: expected {expected}, got {actual}"
        return

    if method_name == "findMedianSortedArrays":
        left, right, expected = case
        actual = method(left, right)
        assert abs(actual - expected) < 1e-9, f"{name}: expected {expected}, got {actual}"
        return

    if method_name in {"threeSum", "fourSum"}:
        if method_name == "threeSum":
            nums, expected = case
            actual = method(nums)
        else:
            nums, target, expected = case
            actual = method(nums, target)
        actual = sorted(tuple(combination) for combination in actual)
        expected = sorted(tuple(combination) for combination in expected)
        assert actual == expected, f"{name}: expected {expected}, got {actual}"
        return

    if method_name == "letterCombinations":
        digits, expected = case
        actual = method(digits)
        assert set(actual) == set(expected), f"{name}: expected {expected}, got {actual}"
        return

    if method_name == "longestPalindrome":
        s, expected = case
        actual = method(s)
        assert len(actual) == len(expected) and actual in s and actual == actual[::-1], (
            f"{name}: expected a palindrome of length {len(expected)} from {s}, got {actual}"
        )
        return

    if len(case) == 2:
        arg1, expected = case
        actual = method(arg1)
        assert actual == expected, f"{name}: expected {expected}, got {actual}"
        return

    if len(case) == 3:
        arg1, arg2, expected = case
        actual = method(arg1, arg2)
        assert actual == expected, f"{name}: expected {expected}, got {actual}"
        return

    raise AssertionError(f"Unsupported test format for {name}: {case}")


def main():
    case_count = 0
    for name, file_name, class_name, method_name, cases in TESTS:
        for case in cases:
            run_case(name, file_name, class_name, method_name, case)
            case_count += 1
    print(f"Validated {len(TESTS)} problem modules ({case_count} cases) successfully.")


if __name__ == "__main__":
    main()
