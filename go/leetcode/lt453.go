package main

func minMoves(nums []int) int {
	min := nums[0]
	for i := 1; i < len(nums); i++ {
		if min < nums[i] {
			min = nums[i]
		}
	}
	ans := 0
	for i := 0; i < len(nums); i++ {
		ans += nums[i] - min
	}
	return ans
}