package main

var ans map[int]*TreeNode
var Hash []int

func dfs(x *TreeNode) {
	if x == nil {
		return
	}

	if x.Left != nil && Hash[x.Left.Val] == 1 {
		defer func() {
			x.Left = nil
		}()
	}

	if x.Right != nil && Hash[x.Right.Val] == 1 {
		defer func() {
			x.Right = nil
		}()
	}

	if Hash[x.Val] == 1 {
		if _, ok := ans[x.Val]; ok {
			delete(ans, x.Val)
		}

		if x.Left != nil {
			ans[x.Left.Val] = x.Left
		}

		if x.Right != nil {
			ans[x.Right.Val] = x.Right
		}
	}
	dfs(x.Left)
	dfs(x.Right)
}

func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	Hash = make([]int, 1001)
	ans = make(map[int]*TreeNode)
	ans[root.Val] = root
	for _, x := range to_delete {
		Hash[x] = 1
	}
	dfs(root)
	ansSet := make([]*TreeNode, 0)
	for _, subAns := range ans {
		ansSet = append(ansSet, subAns)
	}
	return ansSet
}