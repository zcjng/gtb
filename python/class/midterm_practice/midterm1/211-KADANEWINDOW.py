from collections import Counter

s = input().strip()
K = int(input())
target = input().strip()

target_count = Counter(target)
window_count = Counter(s[:K])

# Check if the first window works
if all(window_count[c] >= target_count[c] for c in target_count):
    print("YES")
else:
    found = False
    for i in range(1, len(s) - K + 1):
        # Slide the window: remove left, add right
        left_char = s[i-1]
        right_char = s[i+K-1]

        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

        window_count[right_char] += 1

        if all(window_count[c] >= target_count[c] for c in target_count):
            found = True
            break

    print("YES" if found else "NO")
