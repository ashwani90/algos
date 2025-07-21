Certainly! Here's the continuation and completion of the **Split Array into Consecutive Subsequences** solution and explanation, plus a summary for all 10 problems:

---

### 10. **Split Array into Consecutive Subsequences (continued)**

```python
            freq[num + 2] -= 1
            append_freq[num + 2] += 1
        else:
            return False

    return True

# Example
print(isPossible([1,2,3,3,4,5]))  # Output: True
```

**Explanation:**
We try to append the current number to an existing subsequence ending at `num-1`. If not possible, we try to start a new subsequence with `num, num+1, num+2`. If neither is possible, return False.

---

# Summary of all 10 Advanced HashMap Problems:

| Problem                                       | Key Idea                   | Approach                                               |
| --------------------------------------------- | -------------------------- | ------------------------------------------------------ |
| 1. Subarrays with Equal XOR                   | Prefix XOR + Frequency Map | Count subarrays by tracking prefix XOR frequencies.    |
| 2. Shortest Completing Word                   | Letter frequency counting  | Compare license plate char frequencies with each word. |
| 3. Min Unique Ints after K removals           | Greedy on frequencies      | Remove from least frequent numbers first.              |
| 4. Longest substring ≤ K distinct chars       | Sliding window + hashmap   | Maintain freq and shrink window when exceeding k.      |
| 5. Check if Isomorphic                        | Bidirectional mapping      | Use two hashmaps to verify one-to-one mapping.         |
| 6. Number of Boomerangs                       | Distance frequency count   | For each point, count pairs with same distance.        |
| 7. Word Pattern II                            | Backtracking + hashmap     | Assign substring to pattern chars uniquely.            |
| 8. Number of Nice Subarrays                   | Prefix sums + hashmap      | Count subarrays with exactly k odd numbers.            |
| 9. Longest Harmonious Subsequence             | Frequency count            | Sum counts of consecutive numbers.                     |
| 10. Split Array into Consecutive Subsequences | Frequency + greedy append  | Use hashmap to extend or start subsequences.           |

---

If you want, I can provide detailed explanations or code walkthroughs for any particular problem above! Just let me know.
