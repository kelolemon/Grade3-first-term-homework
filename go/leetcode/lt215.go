package main

func quickFind(nums []int, l int, r int, k int) int {
	x := nums[l]
	i, j := l, r
	for ; i < j; {
		for ; i < j && x < nums[j]; {
			j--
		}

		if i < j {
			nums[i] = nums[j]
			i++
		}

		for ; i < j && x > nums[i]; {
			i++
		}

		if i < j {
			nums[j] = nums[i]
			j--
		}
	}
	nums[i] = x
	if i == k - 1 {
		return x
	}

	if i > k - 1 {
		return quickFind(nums, l, i - 1, k)
	}
	return quickFind(nums, i + 1, r, k)
}

func findKthLargest(nums []int, k int) int {
	return quickFind(nums, 0, len(nums) - 1, k)
}