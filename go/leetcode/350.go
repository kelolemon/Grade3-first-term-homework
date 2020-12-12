package main

import "math"

func intersect(nums1 []int, nums2 []int) []int {
	Map1 := make(map[int]int)
	Map2 := make(map[int]int)
	ans := make([]int, 0)
	for _, x := range nums1 {
		if _, ok := Map1[x]; !ok {
			Map1[x] = 1
		} else {
			Map1[x]++
		}
	}
	for _, x := range nums2 {
		if _, ok := Map2[x]; !ok {
			Map2[x] = 1
		} else {
			Map2[x]++
		}
	}
	for key, value := range Map1 {
		if _, ok := Map2[key]; ok {
			time := int(math.Min(float64(Map2[key]), float64(value)))
			for i := 0; i < time; i++ {
				ans = append(ans, key)
			}
		}
	}
	return ans
}
