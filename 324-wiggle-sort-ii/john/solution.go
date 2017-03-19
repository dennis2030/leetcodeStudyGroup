func getMedianIdx(nums []int) int {
    if len(nums) % 2 == 1 {
        return len(nums) / 2
    } else { // len(nums) % 2 == 0
        return len(nums) / 2 - 1
    }
}

func swapNums(nums []int, idx1 int, idx2 int) {
    var tmpNum = nums[idx1]
    nums[idx1] = nums[idx2]
    nums[idx2] = tmpNum
}

func medianSort(nums []int) {
    var medianIdx = getMedianIdx(nums)

    var leftIdx = 0
    var rightIdx = len(nums) - 1

    for {
        var pickIdx = (leftIdx + rightIdx) / 2
        var storeIdx = leftIdx

        swapNums(nums, pickIdx, rightIdx)
        for iterIdx := leftIdx; iterIdx < rightIdx; iterIdx++ {
            if nums[iterIdx] < nums[rightIdx] {
                swapNums(nums, iterIdx, storeIdx)
                storeIdx++
            }
        }

        swapNums(nums, storeIdx, rightIdx)

        if (storeIdx < medianIdx) {
            leftIdx = storeIdx + 1
        } else if (storeIdx > medianIdx) {
            rightIdx = storeIdx - 1
        } else { // storeIdx == medianIdx
            return
        }
    }
}

func spreadMedians(nums []int) {
    var medianIdx = getMedianIdx(nums)
    var medianNum = nums[medianIdx]
    var storeIdx = 0

    storeIdx = 0
    for iterIdx := 0; iterIdx <= medianIdx; iterIdx++ {
        if nums[iterIdx] == medianNum {
            swapNums(nums, iterIdx, storeIdx)
            storeIdx++
        }
    }

    storeIdx = len(nums) - 1
    for iterIdx := len(nums) - 1; iterIdx > medianIdx; iterIdx-- {
        if nums[iterIdx] == medianNum {
            swapNums(nums, iterIdx, storeIdx)
            storeIdx--
        }
    }
}

func getPartNums(nums []int) ([]int, []int) {
    var medianIdx = getMedianIdx(nums)
    var smallerNums []int
    var largerNums []int

    for idx := 0; idx <= medianIdx; idx++ {
        smallerNums = append(smallerNums, nums[idx])
    }

    for idx := medianIdx + 1; idx < len(nums); idx++ {
        largerNums = append(largerNums, nums[idx])
    }

    return smallerNums, largerNums
}

func interlacePlace(nums []int, smallerNums []int, largerNums []int) {
    for idx := 0; idx < len(largerNums); idx++ {
        nums[idx * 2] = smallerNums[idx]
        nums[idx * 2 + 1] = largerNums[idx]
    }

    if len(smallerNums) > len(largerNums) {
        nums[len(nums) - 1] = smallerNums[len(smallerNums) - 1]
    }
}

func wiggleSort(nums []int) {
    medianSort(nums)
    spreadMedians(nums)

    var smallerNums, largerNums = getPartNums(nums)
    interlacePlace(nums, smallerNums, largerNums)
}
