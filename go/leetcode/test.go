package main

import (
	"fmt"
	"reflect"
)

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

func judge(a interface{}) {
	defer func() {
		err := recover()
		fmt.Println(err)
	}()
	x := reflect.ValueOf(a)
	x.IsNil()
}

func main() {
	a := [4]int{1, 2, 3, 4}
	judge(a)
	fmt.Println("end")
}