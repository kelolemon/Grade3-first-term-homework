package main

import (
	"math"
	"sort"
)

func check(houses []int, heaters []int, radius int) bool {
	housePoint := 0
	heaterPoint := 0
	for ;; {
		if housePoint == len(houses) {
			break
		}
		if heaterPoint == len(heaters) {
			break
		}

		if heaters[heaterPoint] - radius <= houses[housePoint] && heaters[heaterPoint] + radius >= houses[housePoint] {
			housePoint++
			continue
		}

		if houses[housePoint] < heaters[heaterPoint] - radius {
			return false
		}
		heaterPoint++
	}
	if housePoint == len(houses) {
		return true
	}
	return false
}

func findRadius(houses []int, heaters []int) int {
	sort.Ints(houses)
	sort.Ints(heaters)
	left, right := 0, math.MaxInt32
	for ;left < right; {
		mid := (left + right) >> 1
		if check(houses, heaters, mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return right
}
