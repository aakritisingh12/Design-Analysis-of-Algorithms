def combinationSum(candidates: [int], target: int) -> [[int]]:
    sort_set = sorted(candidates)

    def backtrack(space, path):
        if sum(path) > target:
            return
        if sum(path) == target:
            answer.append(path)

        for i in range(len(space)):
            backtrack(space[i:], path + [space[i]])

    answer = []
    backtrack(sort_set, [])
    return answer


W = [5, 10, 12, 13, 15, 18]
target = 30
print(combinationSum(W, target))
