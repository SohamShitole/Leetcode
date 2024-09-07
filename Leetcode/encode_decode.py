class Solution:

    def encode(self, strs: list[str]) -> str:
        str1 = []
        for i in strs:
            str1.append(f"{len(i)}${i}")
        return "".join(str1)

    def decode(self, s: str) -> list[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = s.index("$",i)
            length = int(s[i:j])
            i = j + 1
            decoded.append(s[i:i+length])
            i += length
        return decoded



encoder = Solution()
original_strings = ["hello", "world", "this", "is", "a", "test"]
encoded_string = encoder.encode(original_strings)
decoded_strings = encoder.decode(encoded_string)

print("Encoded:", encoded_string)
print("Decoded:", decoded_strings)