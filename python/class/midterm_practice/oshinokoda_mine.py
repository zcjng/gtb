import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0

    Q = data[p]; p += 1        # number of queries
    N = data[p]; p += 1        # matrix size

    # Prepare arrays
    A = [[0]*N for _ in range(N)]
    rowSum = [0]*N
    colSum = [0]*N
    diagMain = [0]*(2*N - 1)   # index = i - j + (N-1)
    diagAnti = [0]*(2*N - 1)   # index = i + j

    # Read matrix and fill sums
    for i in range(N):
        for j in range(N):
            v = data[p]; p += 1
            A[i][j] = v
            rowSum[i] += v
            colSum[j] += v
            diagMain[i - j + (N - 1)] += v
            diagAnti[i + j] += v

    out_lines = []
    for _ in range(Q):
        x = data[p]; y = data[p+1]; p += 2
        # input appears 1-based in sample — convert to 0-based
        x -= 1
        y -= 1
        brightness = (
            rowSum[x]
            + colSum[y]
            + diagMain[x - y + (N - 1)]
            + diagAnti[x + y]
            - 3 * A[x][y]
        )
        out_lines.append(str(brightness))

    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    main()
