from sys import float_info

class Matf:
    """ TODO
    """ 
    def __init__(self):
        """ Rows run horizontally, cols run vertically
            It is a row-major repesentation

            Example:   
                | 100 100 100 |    | m00 m01 m02 |
                | 200 200 200 | -> | m10 m11 m12 |
                | 300 300 300 |    | m20 m21 m22 |
                
                A[0][0] = m00
                A[0][1] = m01
                ...
                A[i][j] = mij
        """
        self.__rows = []
        self.__cols = []
        self.__max = float_info.min
        self.__min = float_info.max

    def __str__(self) -> str:
        """ Prints the Matrix
        """
        first = True
        out = "["
        for row in self.__rows:
            if first:
                out += "["
                first = False
            else:
                out += "\n ["
            out += (", ".join(str(cell) for cell in row)) + "]"
        return out + "]"

    def get_rows(self) -> list:
        return self.__rows.copy()
    
    def get_cols(self) -> list:
        return self.__cols.copy()

class Mat1x2f(Matf):
    """ TODO: mas
    """

    def __init__(self,
        m00: float, m01):
        super().__init__()

        self.row0 = [m00, m01]
        self.col0 = [m00]
        self.col1 = [m01]
        self.__rows = [self.row0]
        self.__cols = [self.col0, self.col1]

    def transpose(self):
        """ Transposes the matrix

        It is important to notice that this method returns
        a newly created matrix. This is based on the Math
        structure this module has.
        """
        return Mat2x1f(
                self.row0[0],
                self.row0[1]
            )

    def set_m00(self, m00):
        self.row0[0] = m00
        self.col0[0] = m00

    def set_m01(self, m01):
        self.row0[1] = m01
        self.col1[0] = m01

    def m00(self): return self.row0[0]
    def m01(self): return self.row0[1]

class Mat2x1f(Matf):

    def __init__(self,
            m00: float,
            m10: float):
        super().__init__()

        self.row0 = [m00]
        self.row1 = [m10]
        self.col0 = [m00, m10]
        self.rows = [self.row0, self.row1]
        self.cols = [self.col0]

    def transpose(self):
        return Mat1x2f(
                self.row0[0], self.row1[0]
            )

    def m00(self): return self.row0[0]
    def m10(self): return self.col0[0]

class Mat1x3f(Matf):

    def __init__(self,
        m00: float, m01: float, m02: float):
        
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02

        self.row0 = [m00, m01, m02]

        self.col0 = [m00]
        self.col1 = [m01]
        self.col2 = [m02]

        self.rows = [self.row0]

        self.cols = [self.col0, self.col1, self.col2]

    def transpose(self):
        return Mat1x3f(
                self.m00,
                self.m01,
                self.m02
            )

class Mat2x3f(Matf):

    def __init__(self,
        m00: float, m01: float, m02: float,
        m10: float, m11: float, m12: float):
        
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12

        self.row0 = [m00, m01, m02]
        self.row1 = [m10, m11, m12]

        self.col0 = [m00, m10]
        self.col1 = [m01, m11]
        self.col2 = [m02, m12]

        self.rows = [self.row0, self.row1]
        self.cols = [self.col0, self.col1, self. col2]

    def transpose(self):
        return Mat3x2f(
            self.m00, self.m10,
            self.m01, self.m11,
            self.m02, self.m12)

class Mat3x1f(Matf):

    def __init__(self,
            m00:float,
            m10: float,
            m20: float
        ):
        
        super().__init__()

        self.m00 = m00
        self.m10 = m10
        self.m20 = m20

        self.row0 = [m00]
        self.row1 = [m10]
        self.row2 = [m20]

        self.col0 = [m00, m10, m20]

        self.rows = [self.row0, self.row1, self.row2]
        self.cols = [self.col0]

    def transpose(self):
        return Mat1x3f(
                self.m00, self.m10, self.m20
            )

class Mat3x2f(Matf):

    def __init__(self,
            m00: float, m01: float,
            m10: float, m11: float,
            m20: float, m21: float
        ):
        
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11
        self.m20 = m20
        self.m21 = m21

        self.row0 = [m00, m01]
        self.row1 = [m10, m11]
        self.row2 = [m20, m21]

        self.col0 = [m00, m10]
        self.col1 = [m10, m11]

        self.rows = [self.row0, self.row1, self.row2]
        self.cols = [self.col0, self.col1]

    def transpose(self):
        return Mat2x3f(
                self.m00, self.m10, self.m20,
                self.m01, self.m11, self.m21
            )

class Mat1x4f(Matf):

    def __init__(
            self, m00: float, m01: float, m02: float, m03:float
        ):

        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m03 = m03

        self.row0 = [m00, m01, m02, m03]
        
        self.col0 = [m00]
        self.col1 = [m01]
        self.col2 = [m02]
        self.col3 = [m03]

        self.rows = [self.row0]
        self.cols = [self.col0, self.col1, self.col2, self.col3]

    def transpose(self):

        return Mat4x1f(
                self.m00,
                self.m01,
                self.m02,
                self.m03,
            )

class Mat2x4f(Matf):

    def __init__(self,
            m00: float, m01: float, m02: float, m03: float,
            m10: float, m11: float, m12: float, m13: float):

        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m03 = m03
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13

        self.row0 = [m00, m01, m02, m03]
        self.row1 = [m10, m11, m12, m13]

        self.col0 = [m00, m10]
        self.col1 = [m01, m11]
        self.col2 = [m02, m12]
        self.col3 = [m03, m13]

        self.rows = [self.row0, self.row1]
        self.cols = [self.col0, self.col1, self.col2, self.col3]

    def transpose(self):

        return Mat4x2f(
                self.m00, self.m10,
                self.m01, self.m11,
                self.m02, self.m12,
                self.m03, self.m13,
            )

class Mat3x4f(Matf):

    def __init__(self,
            m00: float, m01: float, m02: float, m03: float,
            m10: float, m11: float, m12: float, m13: float,
            m20: float, m21: float, m22: float, m23: float,
        ):

        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m03 = m03
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23

        self.row0 = [m00, m01, m02, m03]
        self.row1 = [m10, m11, m12, m13]
        self.row2 = [m20, m21, m22, m23]

        self.col0 = [m00, m10, m20]
        self.col1 = [m01, m11, m21]
        self.col2 = [m02, m12, m22]
        self.col3 = [m03, m13, m23]

        self.rows = [self.row0, self.row1, self.row2]
        self.cols = [self.col0, self.col1, self.col2, self.col3]

    def transpose(self):
        
        return Mat4x3f(
                self.m00, self.m10, self.m20,
                self.m01, self.m11, self.m21,
                self.m02, self.m03, self.m13,
                self.m03, self.m13, self.m23
            )
        
class Mat4x1f(Matf):

    def __init__(self,
            m00: float,
            m10: float,
            m20: float,
            m30:float
        ):

        super().__init__()

        self.m00 = m00
        self.m10 = m10
        self.m20 = m20
        self.m30 = m30

        self.row0 = [m00]
        self.row1 = [m10]
        self.row2 = [m20]
        self.row3 = [m30]

        self.col0 = [m00, m10, m20, m30]

        self.rows = [self.row0, self.row1, self.row2, self.row3]
        self.cols = [self.col0]

    def transpose(self):
        
        return Mat1x4f(
            self.m00, self.m10, self.m20, self.m30
        )

class Mat4x2f(Matf):

    def __init__(self,
            m00: float, m01: float,
            m10: float, m11: float,
            m20: float, m21: float,
            m30: float, m31: float
        ):

        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11
        self.m20 = m20
        self.m21 = m21
        self.m30 = m30
        self.m31 = m31

        self.row0 = [m00, m01]
        self.row1 = [m10, m11]
        self.row2 = [m20, m21]
        self.row3 = [m30, m31]

        self.col0 = [m00, m10, m20, m30]
        self.col1 = [m01, m11, m21, m31]

        self.rows = [self.row0, self.row1, self.row2, self.row3]
        self.cols = [self.col0, self.col1]

    def transpose(self):
        
        return Mat2x4f(
                self.m00, self.m10, self.m20, self.m30,
                self.m01, self.m11, self.m21, self.m31
            )

class Mat4x3f(Matf):

    def __init__(self,
            m00: float, m01: float, m02: float,
            m10: float, m11: float, m12: float,
            m20: float, m21: float, m22: float,
            m30: float, m31: float, m32: float
        ):

        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22
        self.m30 = m30
        self.m31 = m31
        self.m32 = m32

        self.row0 = [m00, m01, m02]
        self.row1 = [m10, m11, m12]
        self.row2 = [m20, m21, m22]
        self.row3 = [m30, m31, m32]

        self.col0 = [m00, m10, m20, m30]
        self.col1 = [m01, m11, m21, m31]
        self.col2 = [m02, m12, m22, m32]

        self.rows = [self.row0, self.row1, self.row2, self.row3]
        self.cols = [self.col0, self.col1, self.col2]

    def transpose(self):

        return Mat3x4f(
                self.m00, self.m10, self.m20, self.m30,
                self.m01, self.m11, self.m21, self.m31,
                self.m02, self.m12, self.m22, self.m32
            )

class Mat2x2f(Matf):

    def __init__(self, 
        m00 : float, m01 : float,
        m10 : float, m11 : float):
        """Initialization of the 2x2 Matrix in column Major representation.
        
        Arguments:
            m00 {float} -- [description]
            m01 {float} -- [description]
            m10 {float} -- [description]
            m11 {float} -- [description]
        """
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11

        self.row0 = [self.m00, self.m01]
        self.row1 = [self.m10, self.m11]
        self.col0 = [self.m00, self.m10]
        self.col1 = [self.m01, self.m11]

        self.rows = [self.row0, self.row1]
        self.cols = [self.col0, self.col1]

    def transpose(self):

        return Mat2x2f(
                self.m00, self.m10,
                self.m01, self.m11
            )
    

class Mat3x3f(Matf):
    def __init__(self,
        m00 : float, m01 : float, m02 : float,
        m10 : float, m11 : float, m12 : float,
        m20 : float, m21 : float, m22 : float):
        """Initialization of the 3x3 Matrix in column Major representation.
        
        Arguments:
            m00 {float} -- [description]
            m01 {float} -- [description]
            m02 {float} -- [description]
            m10 {float} -- [description]
            m11 {float} -- [description]
            m12 {float} -- [description]
            m20 {float} -- [description]
            m21 {float} -- [description]
            m22 {float} -- [description]
			TODO
        """
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22

        self.row0 = [self.m00, self.m01, self.m02]
        self.row1 = [self.m10, self.m11, self.m12]
        self.row2 = [self.m20, self.m21, self.m22]
        
        self.col0 = [self.m00, self.m10, self.m20]
        self.col1 = [self.m01, self.m11, self.m21]
        self.col2 = [self.m02, self.m12, self.m22]

        self.rows = [self.row0, self.row1, self.row2]
        self.cols = [self.col0, self.col1, self.col2]

    def transpose(self):
        return Mat3x3f(
                self.m00, self.m10, self.m20,
                self.m01, self.m11, self.m21,
                self.m02, self.m12, self.m22
            )

class Mat4x4f(Matf):
    """ TODO
    """ 
    def __init__(self,
        m00: float, m01: float, m02: float, m03: float,
        m10: float, m11: float, m12: float, m13: float,
        m20: float, m21: float, m22: float, m23: float,
        m30: float, m31: float, m32: float, m33: float
		):
        """Initialization of the 3x3 Matrix in column Major representation.
        
        Arguments:
            m00 {float} -- [description]
            m01 {float} -- [description]
            m02 {float} -- [description]
            m10 {float} -- [description]
            m11 {float} -- [description]
            m12 {float} -- [description]
            m20 {float} -- [description]
            m21 {float} -- [description]
            m22 {float} -- [description]
			TODO
        """
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m03 = m03
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m30 = m30
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33

        self.row0 = [self.m00, self.m01, self.m02, self.m03]
        self.row1 = [self.m10, self.m11, self.m12, self.m13]
        self.row2 = [self.m20, self.m21, self.m22, self.m23]
        self.row3 = [self.m30, self.m31, self.m32, self.m33]

        self.col0 = [self.m00, self.m10, self.m20, self.m30]
        self.col1 = [self.m01, self.m11, self.m21, self.m31]
        self.col2 = [self.m02, self.m12, self.m22, self.m32]
        self.col3 = [self.m03, self.m13, self.m23, self.m33]

        self.rows = [self.row0, self.row1, self.row2, self.row3]
        self.cols = [self.col0, self.col1, self.col2, self.col3]

    def transpose(self):

        return Mat4x4f(
                self.m00, self.m10, self.m20, self.m30,
                self.m01, self.m11, self.m21, self.m31,
                self.m02, self.m21, self.m22, self.m32,
                self.m03, self.m31, self.m32, self.m33
            )