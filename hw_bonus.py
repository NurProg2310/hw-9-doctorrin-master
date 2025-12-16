from typing import List, Tuple, Dict


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:

    seen: Dict[int, int] = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    # Per prompt, this shouldn't happen.
    raise ValueError("No two sum solution found.")


def is_isomorphic(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s_to_t: Dict[str, str] = {}
    t_to_s: Dict[str, str] = {}

    for cs, ct in zip(s, t):
        if cs in s_to_t and s_to_t[cs] != ct:
            return False
        if ct in t_to_s and t_to_s[ct] != cs:
            return False
        s_to_t[cs] = ct
        t_to_s[ct] = cs

    return True


def is_alien_sorted(words: List[str], order: str) -> bool:

    rank = {ch: i for i, ch in enumerate(order)}

    def in_correct_order(a: str, b: str) -> bool:
        # return True if a <= b in alien lexicographic order
        for ca, cb in zip(a, b):
            if ca != cb:
                return rank[ca] < rank[cb]

        return len(a) <= len(b)

    for i in range(len(words) - 1):
        if not in_correct_order(words[i], words[i + 1]):
            return False
    return True


def length_of_longest_substring(s: str) -> int:

    last: Dict[str, int] = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)

    return best


def group_shifted(strings: List[str]) -> List[List[str]]:

    def key(s: str) -> Tuple[int, ...]:
        if len(s) <= 1:
            return ()
        diffs = []
        for i in range(1, len(s)):
            diffs.append((ord(s[i]) - ord(s[i - 1])) % 26)
        return tuple(diffs)

    groups: Dict[Tuple[int, ...], List[str]] = {}
    for st in strings:
        k = key(st)
        groups.setdefault(k, []).append(st)

    return list(groups.values())
