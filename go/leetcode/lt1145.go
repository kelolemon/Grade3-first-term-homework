package main

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func count(x *TreeNode) (int, int) {
	
}

func search(node *TreeNode,x int) (int, int){
	if node == nil {
		return -1, -1
	}

	if node.Val == x {
		count(node)
	}

	l0, l1 := search(node.Left, x)
	r0, r1 := search(node.Right, x)
	if l0 == -1 && l1 == -1 {
		return r0, r1
	}
	return l0, l1
}

func btreeGameWinningMove(root *TreeNode, n int, x int) bool {

}