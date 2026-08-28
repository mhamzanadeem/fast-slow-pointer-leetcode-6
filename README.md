# Fast & Slow Pointers — LeetCode Practice

## Floyd's Cycle Detection (Tortoise and Hare) — in my own words

Imagine two runners on a circular track. The **slow** pointer takes 1 step at a
time; the **fast** pointer takes 2. If the track is a loop (a cycle), the faster
runner will eventually lap the slower one and they will meet. If there is no loop
(the track has an end), the fast runner falls off the edge (`fast` or
`fast.next` becomes `None`) and we conclude there is no cycle.

That is the whole idea: by moving at different speeds you guarantee that, *if a
cycle exists*, the two pointers must eventually occupy the same node.

### Why must fast and slow meet inside a cycle?

Once both pointers are inside the cycle, think of their distance apart. On each
iteration the fast pointer gains exactly **1 step** on the slow pointer (it moves
2, slow moves 1, so the gap shrinks by 1). Because the gap shrinks by a fixed
amount of 1 every step, it cannot skip over the meeting point — it must hit
exactly 0 at some step. The only way they would *never* meet is if the gap
jumped in a way that skipped 0, but a constant gain of 1 makes that impossible.
So, provided a cycle exists and both eventually enter it, they are guaranteed to
meet.

(Formally: the position of slow modulo the cycle length `L` is `s + t (mod L)`
and fast is `s + 2t (mod L)`; they meet when `t ≡ 0 (mod L)`, which always has a
solution.)

### The reset-to-head trick in Linked List Cycle II

Detecting a cycle tells us *a* meeting point, but not where the cycle *starts*.
Let:
- `m` = distance from head to the cycle's entry node,
- `k` = distance from the entry node to the meeting point (inside the cycle),
- `L` = length of the cycle.

When they meet, slow has travelled `m + k` steps and fast has travelled
`m + k + qL` steps for some integer `q` (fast went around the loop `q` times).
Since fast travelled exactly twice as far as slow:

```
2(m + k) = m + k + qL
=> m + k = qL
=> m = qL - k
```

`qL - k` is the distance from the meeting point forward to the entry node
(walk the remaining loop `q-1` times plus the `L - k` leftover). So if we put one
pointer back at the **head** and advance *both* pointers one step at a time, the
head pointer travels `m` steps to the entry while the other travels `m` steps
from the meeting point — and `m` steps from the meeting point lands exactly on
the entry node too. That's why resetting one pointer to `head` and stepping both
together makes them collide at the cycle's start.

---

## Solutions (single file per problem)

| Problem | File | LeetCode |
| --- | --- | --- |
| Middle of the Linked List | [Middle of the Linked List.py](./Middle%20of%20the%20Linked%20List.py) | 876 |
| Linked List Cycle | [Linked List Cycle.py](./Linked%20List%20Cycle.py) | 141 |
| Linked List Cycle II | [Linked List Cycle II.py](./Linked%20List%20Cycle%20II.py) | 142 |
| Happy Number | [Happy Number.py](./Happy%20Number.py) | 202 |
| Palindrome Linked List | [Palindrome Linked List.py](./Palindrome%20Linked%20List.py) | 234 |
| Remove Nth Node From End of List | [Remove Nth Node From End of List.py](./Remove%20Nth%20Node%20From%20End%20of%20List.py) | 19 |

### Notes on requirements
- **All 6 solved** — each file contains a working `Solution` class.
- **Remove Nth Node From End in a single pass** — `Remove Nth Node From End of List.py`
  uses a `dummy` node and keeps a gap of `n` between `fast` and `slow`; when `fast`
  reaches the tail, `slow` is right before the target. One traversal only.
- **Happy Number** reuses Floyd's idea by treating each number's "next sum of
  squares" as the `next` pointer of a virtual linked list.
