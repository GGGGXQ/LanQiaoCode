if __name__ == '__main__':
    for _ in range(int(input())):
        B1, B2, B3 = map(int, input().split())
        cntA, cntB = map(int, input().split())
        vA, vB = map(int, input().split())
        if vA > vB:
            cntA, cntB = cntB, cntA
            vA, vB = vB, vA

        ans = 0
        for i in range(cntA + 1):
            if i * vA > B1:
                break
            for j in range(cntA - i + 1):
                if j * vA > B2:
                    break
                res = i + j
                remainCntA = cntA - i - j
                remainCntB = cntB
                remain_B1 = B1 - vA * i
                remain_B2 = B2 - vA * j
                remain_B3 = B3

                res += min(remain_B1 // vB, cntB)
                remainCntB -= min(remain_B1 // vB, remainCntB)
                res += min(remain_B2 // vB, remainCntB)
                remainCntB -= min(remain_B2 // vB, remainCntB)

                res += min(remain_B3 // vA, remainCntA)
                remain_B3 -= min(remain_B3 // vA, remainCntA) * vA
                res += min(remain_B3 // vB, remainCntB)

                ans = max(ans, res)
        print(ans)