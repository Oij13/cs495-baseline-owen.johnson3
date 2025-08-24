from collections import Counter

# def main():
# 	result = first_unique_char("ssfffe")
# 	print(result)

def first_unique_char(s):
	char_count = Counter(s)

	for i, char in enumerate(s):
		if char_count[char] == 1:
			return i

	return -1

# if __name__ == "__main__":
# 	main()
