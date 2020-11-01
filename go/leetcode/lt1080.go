package main

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func dfs(x *TreeNode, sum int, limit int) int {
	if x == nil {
		return sum
	}

	if x.Left == nil && x.Right == nil {
		tmp := x.Val
		if sum + x.Val < limit {
			x = nil
		}
		return sum + tmp
	}

	if x.Left == nil {
		rightAns := dfs(x.Right, sum + x.Val, limit)
		if rightAns < limit {
			x.Right = nil
		}
		return rightAns + x.Val
	}

	if x.Right == nil {
		leftAns := dfs(x.Left, sum + x.Val, limit)
		if leftAns < limit {
			x.Left = nil
		}
		return leftAns + x.Val
	}

	leftAns := dfs(x.Left, sum + x.Val, limit)
	rightAns := dfs(x.Right, sum + x.Val, limit)
	if leftAns < limit {
		x.Left = nil
	}
	if rightAns < limit {
		x.Right = nil
	}

	return max(leftAns, rightAns) + x.Val
}

func sufficientSubset(root *TreeNode, limit int) *TreeNode {
	fin := dfs(root, 0, limit)
	if fin < limit {
		root = nil
	}
	return root
}
