package main

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
	
}