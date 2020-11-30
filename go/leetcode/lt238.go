package main

func productExceptSelf(nums []int) []int {
	LeftMulti := make([]int, 0)
	for i := 0; i < len(nums); i++ {
		if i == 0 {
			LeftMulti = append(LeftMulti, nums[i])
			continue
		}
		LeftMulti = append(LeftMulti, nums[i] * LeftMulti[i - 1])
	}

	RightMulti := make([]int, 0)
	for i := len(nums) - 1; i >= 0; i-- {
		if i == len(nums) - 1 {
			RightMulti = append(RightMulti, nums[i])
			continue
		}
		RightMulti = append(RightMulti, nums[i] * RightMulti[len(RightMulti) - 1])
	}

	proNum := make([]int, 0)
	for i := 0; i < len(nums); i++ {
		if i == 0 {
			proNum = append(proNum, RightMulti[len(nums) - 1 - i - 1])
			continue
		}
		if i == len(nums) - 1 {
			proNum = append(proNum, LeftMulti[i - 1])
			continue
		}
		proNum = append(proNum, RightMulti[len(nums) - 2 - i] * LeftMulti[i - 1])
	}

	return proNum
}
