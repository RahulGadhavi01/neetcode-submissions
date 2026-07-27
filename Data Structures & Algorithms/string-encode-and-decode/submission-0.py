class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            # Store: length#word
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            # Find where the length ends
            j = i
            while s[j] != "#":
                j += 1

            # Get the length of the word
            length = int(s[i:j])

            # Extract the word using its length
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Move to the next encoded word
            i = j + 1 + length

        return result
