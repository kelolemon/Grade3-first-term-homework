package main

func Abs(x int) int {
	if x > 0 {
		return x
	}
	return -x
}

func AbsDif(x int, y int) int {
	Opt := int64(x) * int64(y)
	if Opt < 0 {
		return Abs(x) + Abs(y)
	}
	return Abs(Abs(x) - Abs(y))
}

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	HashMap := make(map[int] int) // block
	for i := 0; i < len(nums); i++ {
		id := nums[i] / (t + 1)
		if nums[i] < 0 {
			id -= 1
		}
		// calc block number id
		if _, ok := HashMap[id]; ok {
			return true
		}
		if _, ok := HashMap[id + 1]; ok {
			if AbsDif(nums[i], HashMap[id + 1]) <= t {
				return true
			}
		}
		if _, ok := HashMap[id - 1]; ok {
			if AbsDif(nums[i], HashMap[id - 1]) <= t {
				return true
			}
		}
		HashMap[id] = nums[i]
		if i - k >= 0 {
			delete(HashMap, nums[i - k] / (t + 1))
		}
	}
	return false
}
