class Solution:
    def decodeCiphertext(self, encodedText, rows):
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows

        # build matrix
        matrix = [
            encodedText[i * cols:(i + 1) * cols]
            for i in range(rows)
        ]

        res = []

        # read diagonals
        for start_col in range(cols):
            i, j = 0, start_col
            while i < rows and j < cols:
                res.append(matrix[i][j])
                i += 1
                j += 1

        # remove trailing spaces
        return "".join(res).rstrip()
