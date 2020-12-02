package main

import (
	"math"
)

func kthFactor(n int, k int) int {
	ans := make([]int, 0)
	for i := 1; i <= int(math.Sqrt(float64(n))); i++ {
		if n % i == 0 {
			ans = append(ans, i)
		}
	}
	if ans[len(ans) - 1] * ans[len(ans) - 1] == n && k > len(ans){
		k++
	}

	if k > 2 * len(ans) {
		return -1
	}

	if k <= len(ans) {
		return ans[k - 1]
	}
	return n / ans[2 * len(ans) - k]
}
