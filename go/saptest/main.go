package main

import "fmt"

type TreeNode struct {
	Val int
	LeftNode *TreeNode
	RightNode *TreeNode
}

func dfs(x *TreeNode) {
	if x == nil {
		return
	}
	dfs(x.LeftNode)
	fmt.Println(x.Val)
	dfs(x.RightNode)
}

func main() {

}
