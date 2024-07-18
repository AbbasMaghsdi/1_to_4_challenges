def group_anagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    
    return list(anagrams.values())

# Example usage
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(input_strs)
print(result)  # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
