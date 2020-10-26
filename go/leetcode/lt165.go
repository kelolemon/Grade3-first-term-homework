package main

func ord(x uint8) int{
	return int(x) - int('0')
}

func check(x string, pos int) int {
	for i := pos; i < len(x); i++ {
		if x[i] == '0' || x[i] == '.' {
			continue
		}
		return 1
	}
	return 0
}

func compareVersion(version1 string, version2 string) int {
	subversion1 := 0
	subversion2 := 0
	for i, j := 0, 0; i < len(version1) && j < len(version2); {
		if version1[i] == '.' && version2[j] == '.' {
			if subversion1 > subversion2 {
				return 1
			}
			if subversion1 < subversion2 {
				return -1
			}
			subversion2 = 0
			subversion1 = 0
			i ++
			j ++
			continue
		}
		if  version1[i] == '.' {
			if j == len(version2) - 1 {
				subversion2 *= 10
				subversion2 += ord(version2[j])
				if subversion1 > subversion2 {
					return 1
				}
				if subversion1 < subversion2 {
					return -1
				}
				return check(version1, i)
			}
			subversion2 *= 10
			subversion2 += ord(version2[j])
			j ++
			continue
		}

		if version2[j] == '.' {
			if i == len(version1) - 1 {
				subversion1 *= 10
				subversion1 += ord(version1[i])
				if subversion1 > subversion2 {
					return 1
				}
				if subversion1 < subversion2 {
					return -1
				}
				return -1 * check(version2, j)
			}
			subversion1 *= 10
			subversion1 += ord(version1[i])
			i ++
			continue
		}

		subversion1 *= 10
		subversion1 += ord(version1[i])
		subversion2 *= 10
		subversion2 += ord(version2[j])
		i ++
		j ++
		if i == len(version1) && j == len(version2) {
			if subversion1 > subversion2 {
				return 1
			}
			if subversion1 < subversion2 {
				return -1
			}
			return 0
		}
		if i == len(version1) {
			for k := j; k < len(version2); k++ {
				if version2[k] == '.' {
					if subversion1 > subversion2 {
						return 1
					}
					if subversion1 < subversion2 {
						return -1
					}
					return -1 * check(version2, k)
				}
				subversion2 *= 10
				subversion2 += ord(version2[k])
			}
			if subversion1 > subversion2 {
				return 1
			}
			if subversion1 < subversion2 {
				return -1
			}
			return 0
		}

		if j == len(version2) {
			for k := i; k < len(version1); k++ {
				if version1[k] == '.' {
					if subversion1 > subversion2 {
						return 1
					}
					if subversion1 < subversion2 {
						return -1
					}
					return check(version1, k)
				}
				subversion1 *= 10
				subversion1 += ord(version1[k])
			}
			if subversion1 > subversion2 {
				return 1
			}
			if subversion1 < subversion2 {
				return -1
			}
			return 0
		}
	}
	return 0
}