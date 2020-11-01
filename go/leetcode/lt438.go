package main

func findAnagrams(s string, p string) []int {
	if len(s) < len(p) {
		return make([]int, 0)
	}
	HashMap := make([]int, 26)
	WindowSize := len(p)
	for i := 0; i < WindowSize; i++ {
		HashMap[p[i] - 'a']++
	}
	WindowMap := make([]int, 26)
	for i := 0; i < WindowSize; i++ {
		WindowMap[s[i] - 'a']++
	}
	ans := make([]int, 0)
	for i := 0; i <= len(s) - WindowSize; i++ {
		if i == 0 {
			flag := 0
			for x := 0; x < 26; x++ {
				if HashMap[x] != WindowMap[x] {
					flag = 1
					break
				}
			}
			if flag == 0 {
				ans = append(ans, i)
			}
			continue
		}
		WindowMap[s[i - 1] - 'a']--
		WindowMap[s[i + WindowSize - 1] - 'a']++
		flag := 0
		for x := 0; x < 26; x++ {
			if HashMap[x] != WindowMap[x] {
				flag = 1
				break
			}
		}
		if flag == 0 {
			ans = append(ans, i)
		}
	}
	return ans
}
