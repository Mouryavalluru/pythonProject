def minimumPasses(m, w, p, n):
    passes = 0
    candies = 0
    result = float('inf')

    while candies < n:

        passes_needed = ((p - candies) + (m * w) - 1) // (m * w)
        passes += passes_needed
        candies += passes_needed * m * w


        result = min(result, passes + ((n - candies) + (m * w) - 1) // (m * w))


        diff = abs(m - w)
        half_diff = diff // 2

        if m < w:
            half_diff = diff - half_diff

        if candies >= p:
            if half_diff <= candies // p:
                if m < w:
                    m += half_diff
                else:
                    w += half_diff
                candies -= half_diff * p
            else:
                if m < w:
                    m += candies // p
                else:
                    w += candies // p
                candies -= (candies // p) * p
        elif candies < p:
            needed = p - candies
            if half_diff <= needed // p:
                if m < w:
                    m += half_diff
                else:
                    w += half_diff
                candies += half_diff * p
            else:
                if m < w:
                    m += needed // p
                else:
                    w += needed // p
                candies += (needed // p) * p

    return min(passes, result)


m, w, p, n = 312, 12, 2, 12
result = minimumPasses(m, w, p, n)
print(result)
