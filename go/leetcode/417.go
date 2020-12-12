package main

type NodeInfo struct {
	LeftMax int
	RightMax int
	UpMax int
	DownMax int
}

func check(node NodeInfo, n int, m int) bool {
	if node.LeftMax == 0 && node.RightMax == m - 1 {
		return true
	}
	if node.LeftMax == 0 && node.DownMax == n - 1 {
		return true
	}
	if node.RightMax == m - 1 && node.UpMax == 0 {
		return true
	}
	if node.UpMax == 0 && node.DownMax == n - 1{
		return true
	}
	return false
}

func pacificAtlantic(matrix [][]int) [][]int {
	n := len(matrix)
	if n == 0 {
		return make([][]int, 0)
	}
	m := len(matrix[n])
	if m == 0 {
		return make([][]int, 0)
	}
	Map := make([][]NodeInfo, n)
	for i := 0; i < n; i++ {
		Map[i] = make([]NodeInfo, m)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if j == 0 {
				Map[i][j].LeftMax = 0
			} else {
				if matrix[i][j] > matrix[i][j - 1] {
					Map[i][j].LeftMax = Map[i][j - 1].LeftMax
				} else {
					Map[i][j].LeftMax = j
				}
			}
		}

		for j := m - 1; j >= 0; j-- {
			if j == m - 1 {
				Map[i][j].RightMax = m - 1
			} else {
				if matrix[i][j] > matrix[i][j + 1] {
					Map[i][j].RightMax = Map[i][j + 1].RightMax
				} else {
					Map[i][j].RightMax = j
				}
			}
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if j == 0 {
				Map[j][i].LeftMax = 0
			} else {
				if matrix[j][i] > matrix[j - 1][i] {
					Map[j][i].UpMax = Map[j - 1][i].UpMax
				} else {
					Map[j][i].UpMax = j
				}
			}
		}

		for j := n - 1; j >= 0; j-- {
			if j == n - 1 {
				Map[j][i].DownMax = n - 1
			} else {
				if matrix[j][i] > matrix[j + 1][i] {
					Map[j][i].DownMax = Map[j + 1][i].DownMax
				} else {
					Map[j][i].DownMax = j
				}
			}
		}
	}

	ans := make([][]int, 0)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if check(Map[i][j], n, m) {
				subAns := make([]int, 2)
				subAns[0] = i
				subAns[1] = j
				ans = append(ans, subAns)
			}
		}
	}
	return ans
}
