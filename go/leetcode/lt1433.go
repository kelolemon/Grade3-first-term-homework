package main

import "sort"

func isBreak(x []int, y []int) bool {
	for i := 0; i < len(x); i++ {
		if x[i] >= y[i] {
			if i == len(x) - 1 {
				return true
			}
			continue
		}
		break
	}

	for i := 0; i < len(x); i++ {
		if x[i] <= y[i] {
			if i == len(x) - 1 {
				return true
			}
			continue
		}
		break
	}

	return false
}

func checkIfCanBreak(s1 string, s2 string) bool {
	a1 := make([]int, 0)
	a2 := make([]int, 0)
	if len(s1) != len(s2) {
		return false
	}
	if len(s1) == 0 {
		return true
	}
	n := len(s1)

	for i := 0; i < n; i++ {
		a1 = append(a1, int(s1[i]))
		a2 = append(a2, int(s2[i]))
	}
	sort.Ints(a1)
	sort.Ints(a2)
	return isBreak(a1, a2)
}
