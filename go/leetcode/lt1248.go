package main

func numberOfSubarrays(nums []int, k int) int {
	oddList := make([]int, 0)
	for i := 0; i < len(nums); i++ {
		if nums[i] % 2 == 1 {
			oddList = append(oddList, i)
		}
	}
	tot := len(oddList)
	if tot == 0 {
		return 0
	}
	ans := 0
	for i := 0; i < tot; i++ {
		if i + k - 1 >= tot {
			return ans
		}
		leftAns := 0
		if i == 0 {
			leftAns = oddList[i]
		} else {
			leftAns = oddList[i] - oddList[i - 1] - 1
		}
		rightAns := 0
		j := i + k - 1
		if j == tot - 1 {
			rightAns = len(nums) - oddList[j] - 1
		} else {
			rightAns = oddList[j + 1] - oddList[j] - 1
		}
		ans += (leftAns + 1) * (rightAns + 1)
	}
	return ans
}

func main() {

}