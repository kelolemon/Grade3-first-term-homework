package main

import "sort"

type NodeInfo struct {
	key int
	value int
	depth int
}

var NodeList []NodeInfo

type NodeSlice []NodeInfo

func (nodes NodeSlice) Len() int {
	return len(nodes)
}

func (nodes NodeSlice) Swap(i, j int) {
	nodes[i], nodes[j] = nodes[j], nodes[i]
}

func (nodes NodeSlice) Less(i, j int) bool {
	if nodes[i].key == nodes[j].key {
		if nodes[i].depth == nodes[j].depth {
			return nodes[i].value < nodes[j].value
		}
		return nodes[i].depth < nodes[j].depth
	}
	return nodes[i].key < nodes[j].key
}

func dfs(x *TreeNode, pos int, depth int) {
	if x == nil {
		return
	}
	NodeList = append(NodeList, NodeInfo{
		depth: depth,
		key: pos,
		value: x.Val,
	})
	dfs(x.Left, pos - 1, depth + 1)
	dfs(x.Right, pos + 1, depth + 1)
}

func verticalTraversal(root *TreeNode) [][]int {
	NodeList = make([]NodeInfo, 0)
	dfs(root, 0, 0)
	sort.Sort(NodeSlice(NodeList))
	ans := make([][]int, 0)
	for i := 0; i < len(NodeList); i++ {
		subAns := make([]int, 0)
		for i < len(NodeList) - 1 && NodeList[i].key == NodeList[i + 1].key {
			subAns = append(subAns, NodeList[i].value)
			i++
		}
		subAns = append(subAns, NodeList[i].value)
		ans = append(ans, subAns)
	}
	return ans
}
