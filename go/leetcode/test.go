package main

import (
	"fmt"
)

type ListNode struct {
	val int
	next *ListNode
}

func judge(head ListNode) bool {
	array := make([]int, 0)
	for x := head; x.next != nil; x = *x.next{
		array = append(array, x.val)
		if x.next != nil && x.next.next == nil {
			array = append(array, x.next.val)
		}
	}

	for i := 0; i < len(array) / 2; i++ {
		if array[i] != array[len(array) - 1 - i] {
			return false
		}
	}
	return true
}

func main() {
	node1 := ListNode{
		val: 1,
		next: nil,
	}

	node2 := ListNode{
		val: 2,
		next: nil,
	}

	node3 := ListNode{
		val: 2,
		next: nil,
	}

	node4 := ListNode{
		val: 1,
		next: nil,
	}
	node1.next = &node2
	node2.next = &node3
	node3.next = &node4
	fmt.Println(judge(node1))
}