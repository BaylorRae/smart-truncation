class Abbreviator:
    """
    Abbreviates strings to target_length
    """
    def __init__(self, target_length: int):
        if target_length < 1:
            raise ValueError("target_length must be greater than 0.")
        self.target_len = target_length

    def abbreviate(self, input_sent) -> str:
        """
        Abbreviates an input string, prioritizing minimizing length of longest word.
        Given instance `target_length` smaller than possible with min token word length of 1,
        returns smallest possible output given max per-token length of 1.
        :param input_sent
        :return: str string of abbreviated words
        """

        current_length = len(input_sent)

        if current_length <= self.target_len:
            return input_sent

        words = {word: i for i, word in enumerate(input_sent.split())}

        # store result list for downstream in-place token replacement
        result = [word for word in words]

        while current_length > self.target_len:
            sorted_words = [word for word in sorted(words.keys(), key=len, reverse=True)]
            longest_word = sorted_words[0]

            if len(longest_word) == 1:
                return self._re_assemble(words, result)

            words[longest_word[:-1]] = words.pop(longest_word)
            current_length -= 1

            if current_length <= self.target_len:
                return self._re_assemble(words, result)

            for k, v in words.items():
                result[v] = k

        return ' '.join(result)

    @staticmethod
    def _re_assemble(words, result):
        """
        Re-assembles list of words into a string in original order
        :param words:
        :param result:
        :return:
        """
        for k, v in words.items():
            result[v] = k
        return ' '.join(result)
