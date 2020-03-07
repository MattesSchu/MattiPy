
class Mat2x2f:

    def __init__(self, m00 : float, m01 : float, m10 : float, m11 : float):
        """Initialization of the 2x2 Matrix in column Major representation.
        
        Arguments:
            m00 {float} -- [description]
            m01 {float} -- [description]
            m10 {float} -- [description]
            m11 {float} -- [description]
        """
        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11

    def __str__(self) -> str:
        return(
            "|{: .2f}, {: .2f}|\n" \
            "|{: .2f}, {: .2f}|"
            .format(self.m00, self.m01, self.m10, self.m11)
        )

test = Mat2x2f(1,2,3,4)

print(test)