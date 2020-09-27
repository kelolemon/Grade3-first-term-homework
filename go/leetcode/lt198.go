package main

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func rob(nums []int) int {
	dp := make([]int, 0)
	dp = append(dp, 0)
	dp = append(dp, nums[0])
	dp = append(dp, max(nums[0], nums[1]))
	for i := 2; i < len(nums); i++ {
		dp = append(dp, max(dp[i - 1], nums[i] + dp[i - 2]))
	}
	return dp[len(nums) - 1]
}
