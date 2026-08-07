class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        latent = ""
        for word in strs:
            latent += str(len(word)) + "#" + word
        return latent  

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        results = []
        left = 0
        while left < len(s):
            right = left
            # we need to decode the length of string first
            while s[right] != "#":
                right += 1
            # get the length in string format, convert it to int
            length = int(s[left:right])
            # calculate the start and end index
            left = right + 1
            right = left + length
            # get the word
            word = s[left:right]
            # add the word in the result list
            results.append(word)
            # update the left pointer
            left = right
        return results
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))