package main

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func count(x *TreeNode) (int, int) {
	if x == nil {
		return -1, 0
	}

	ll, lr := count(x.Left)
	rl, rr := count(x.Right)
	return ll + lr + 1, rl + rr + 1
}

func search(node *TreeNode,x int) (int, int){
	if node == nil {
		return -1, -1
	}

	if node.Val == x {
		return count(node)
	}

	l0, l1 := search(node.Left, x)
	r0, r1 := search(node.Right, x)
	if l0 == -1 && l1 == -1 {
		return r0, r1
	}
	return l0, l1
}

func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
	leftSum, rightSum := search(root, x)
	if n - (leftSum + rightSum + 1) > leftSum + rightSum + 1 {
		return true
	}

	if leftSum > n - leftSum {
		return true
	}

	if rightSum > n - rightSum {
		return true
	}

	return false
}