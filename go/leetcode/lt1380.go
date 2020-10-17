package main

import "math"

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x int, y int) int {
	if x < y {
		return x
	}
	return y
}
func luckyNumbers (matrix [][]int) []int {
	MaxRow := make([]int, 0)
	MaxCol := make([]int, 0)
	for i := 0; i < len(matrix); i++ {
		mini := math.MaxInt32
		for j := 0; j < len(matrix[i]); j++ {
			mini = min(mini, matrix[i][j])
		}
		MaxRow = append(MaxRow, mini)
	}
	for i := 0; i < len(matrix[0]); i++ {
		maxi := -1
		for j := 0; j < len(matrix); j++ {
			maxi = max(matrix[j][i], maxi)
		}
		MaxCol = append(MaxCol, maxi)
	}
	ans := make([]int, 0)
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == MaxRow[i] && matrix[i][j] == MaxCol[j] {
				ans = append(ans, matrix[i][j])
			}
		}
	}
	return ans
}
