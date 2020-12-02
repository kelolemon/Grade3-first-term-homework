package main

import "sort"

func abs(x int) int {
	if x > 0 {
		return x
	}
	return -x
}

func minMoves2(nums []int) int {
	sort.Ints(nums)
	target := nums[len(nums) >> 1]
	ans := 0
	for _, x := range nums {
		ans += abs(x - target)
	}

	return ans
}
