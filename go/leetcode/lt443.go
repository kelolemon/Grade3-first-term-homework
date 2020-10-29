package main

import (
	"fmt"
	"strconv"
)

func compress(chars []byte) int {
	ans := 0
	index := 0
	for i := 0; i < len(chars); i++ {
		first := i
		nums := 1
		for i + 1 < len(chars) && chars[i] == chars[i + 1] {
			nums++
			i++
		}
		if nums == 1 {
			ans += 1
			chars[index] = chars[first]
			index++
		} else {
			exp := 1
			chars[index] = chars[first]
			index++
			x := strconv.Itoa(nums)
			exp += len(x)
			fmt.Println(x)
			for j := 0; j < len(x); j++ {
				chars[index] = x[j]
				index++
			}
			ans += exp
		}
	}
	return ans
}
