package main

import "fmt"

type Node struct {
	next *Node
	val int
}

type List struct {
	root *Node
	tail *Node
}

func (list *List) add(x int) {
	next := Node{
		next: nil,
		val: x,
	}

	if list.root == nil {
		list.root = &next
		list.tail = list.root
		return
	}

	list.tail.next = &next
	list.tail = &next
}

func main() {
	list := &List{
		root: nil,
		tail: nil,
	}

	list.add(1)
	list.add(2)
	list.add(114514)
	for x := list.root; x != nil; x = x.next {
		fmt.Println(x.val)
	}
}