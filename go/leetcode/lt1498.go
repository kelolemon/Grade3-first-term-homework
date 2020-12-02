package main

import (
	"sort"
)

func pow(x int) int {
	if x == 0 {
		return 1
	}
	if x == 1 {
		return 2
	}
	half := pow(x >> 1)
	if x & 1 == 1 {
		return half * 2 * half % 1000000007
	}
	return half * half % 1000000007
}

func numSubseq(nums []int, target int) int {
	ans := 0
	sort.Ints(nums)
	l, r := 0, len(nums) - 1
	for ;l <= r; {
		for ;l <= r && nums[l] + nums[r] > target; {
			r--
		}
		if l <= r {
			ans += pow(r - l)
			ans = ans % 1000000007
		} else {
			break
		}
		l++
	}
	return ans % 1000000007
}
