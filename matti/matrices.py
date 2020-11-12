from enum import Enum
import math

class Axis(Enum):
    """TODO
    """
    X = 1
    Y = 2
    Z = 3
    X_NEG = -1
    Y_NEG = -2
    Z_NEG = -3

class Rotation(Enum):
    """TODO
    """
    PSI = 1
    THETA = 2
    PHI = 3

class Matf:
    """ TODO
    """ 
    def __init__(self, data: list, rows: int, cols: int):
        """ Rows run horizontally, cols run vertically
            It is a row-major repesentation

            Example:
                       col col col   

                row  | 100 100 100 |    | m00 m01 m02 |
                row  | 200 200 200 | -> | m10 m11 m12 |
                row  | 300 300 300 |    | m20 m21 m22 |
                
                A[0][0] = m00
                A[0][1] = m01
                ...
                A[i][j] = mij
        """
        if len(data) != rows * cols:
            raise AttributeError("The provided data doesn't match the Matrix dimensions." )
        if rows < 0 or rows > 3:
            raise ValueError("The rows dimenstion is invalid. Valid numbers are 1 and 2.")
        if cols < 0 or rows > 3:
            raise ValueError("The clols dimension is invalid. Valid numbers are 1 and 2.")

        self._data = data.copy()
        self._rows = rows
        self._cols = cols

    def __str__(self) -> str:
        """ Pretty Prints the matrix.
        """
        return "TODO"

    def _add_data(self, other) -> list:
        if not isinstance(other, Matf):
            raise TypeError("Other Object has to be a Matrix.")
        if (self._rows != other._rows or self._cols != other._cols):
            raise AttributeError("Unable to add matrices with differing dimensions.")
        data_sum = [self._data[i] + other._data[i] for i in range(len(self._data))]
        return data_sum

    def _sub_data(self, other) -> list:
        """TODO
        """
        if not isinstance(other, Matf):
            raise TypeError("Other Object has to be a Matrix.")
        if (self._rows != other._rows or self._cols != other._cols):
            raise AttributeError("Unable to add matrices with differing dimensions.")
        data_dif = [self._data[i] - other._data[i] for i in range(len(self._data))]
        return data_dif        

    def get_rows(self) -> list:
        """TODO
        """
        rows = list()
        current_cell = 0
        while current_cell < len(self._data):
            rows.append(self._data[current_cell : current_cell + self._cols])
            current_cell += self._cols
        return rows
    
    def get_cols(self) -> list:
        """TODO
        """
        cols = list()
        for col_idx in range(self._cols):
            col = list()
            for row_idx in range(self._rows):
                cell_idx = col_idx + (row_idx * self._cols)
                col.append(self._data[cell_idx])
            cols.append(col)
        return cols

    def col_dimension(self) -> int:
        """TODO
        """
        return self._cols

    def row_dimension(self) -> int:
        """TODO
        """
        return self._rows

    def transpose_data(self) -> list:
        """TODO
        """
        transposed_data = list()
        for col in range(self._cols):
            for row in range(self._rows):
                idx = col + (row * self._rows)
                transposed_data.append(self._data[idx])
        return transposed_data

class Mat1x1f(Matf):
    """TODO: mas
    """
    def __init__(self, m00: float):
        """TODO
        """
        super(Mat1x1f, self).__init__([m00], 1, 1)

    def __add__(self, other: Matf) -> Matf:
        """TODO
        """
        data_sum = self._add_data(other)
        return Mat1x1f(data_sum[0])

    def __iadd__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._add_data(other)
        return self

    def __sub__(self, other: Matf) -> Matf:
        """TODO
        """
        data_dif = self._sub_data(other)
        return Mat1x1f(data_dif[0])

    def __isub__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._sub_data(other)
        return self

    def dot(self, other: Matf):
        """TODO
        """
        return None

    def transpose(self) -> Matf:
        """ Transposes the matrix

        It is important to notice that this method returns
        a newly created matrix. This is based on the Math
        structure this module has.
        """
        return Mat1x1f(self._data[0])

    def set_m00(self, m00: float) -> Matf:
        """TODO
        """
        self._data[0] = m00
        return self

    def m00(self) -> float: 
        """TODO
        """
        return self._data[0]

class Mat1x2f(Matf):
    """ TODO: mas
    """
    def __init__(self,
            m00: float, m01):
        """TODO
        """
        super(Mat1x2f, self).__init__([m00, m01], 1, 2)

    def __add__(self, other: Matf) -> Matf:
        """TODO
        """
        data_sum = self._add_data(other)
        return Mat1x2f(data_sum[0], data_sum[1])

    def __iadd__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._add_data(other)
        return self

    def __sub__(self, other: Matf) -> Matf:
        """TODO
        """
        data_dif = self._sub_data(other)
        return Mat1x2f(data_dif[0], data_dif[1])

    def __isub__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._sub_data(other)
        return self

    def transpose(self) -> Matf:
        """ Transposes the matrix

            It is important to notice that this method returns
            a newly created matrix. This is based on the Math
            structure this module has.
        """
        return Mat2x1f(self._data[0], self._data[1])

    def set_m00(self, m00: float) -> Matf:
        """TODO
        """
        self._data[0] = m00
        return self

    def set_m01(self, m01: float) -> Matf:
        """TODO
        """
        self._data[1] = m01 
        return self

    def m00(self) -> float: 
        """TODO
        """
        return self._data[0]

    def m01(self) -> float:
        """TODO
        """ 
        return self._data[1]

class Mat2x1f(Matf):
    """TODO
    """
    def __init__(self,
            m00: float,
            m10: float):
        """TODO
        """
        super().__init__([m00, m10], 2, 1)
    def __add__(self, other: Matf) -> Matf:
        """TODO
        """
        data_sum = self._add_data(other)
        return Mat2x1f(data_sum[0], data_sum[1])

    def __iadd__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._add_data(other)
        return self

    def __sub__(self, other: Matf) -> Matf:
        """TODO
        """
        data_dif = self._sub_data(other)
        return Mat2x1f(data_dif[0], data_dif[1])

    def __isub__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._sub_data(other)
        return self

    def transpose(self):
        """TODO
        """
        return Mat1x2f(
                self._data[0], self._data[1]
            )

    def m00(self) -> float:
        """TODO
        """
        return self._data[0]

    def m10(self) -> float:
        """TODO
        """
        return self._data[1]

class Mat2x2f(Matf):
    """TODO
    """

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
        super().__init__([m00, m01, m10, m11], 2, 2)

    def __add__(self, other: Matf) -> Matf:
        """TODO
        """
        data_sum = self._add_data(other)
        return Mat2x2f(data_sum[0], data_sum[1], data_sum[2], data_sum[3])

    def __iadd__(self, other: Matf) -> Matf:
        """TODO
        """        
        self._data = self._add_data(other)
        return self

    def __sub__(self, other: Matf) -> Matf:
        """TODO
        """        
        data_dif = self._sub_data(other)
        return Mat2x2f(data_dif[0], data_dif[1], data_dif[2], data_dif[3])

    def __isub__(self, other: Matf) -> Matf:
        """TODO
        """        
        self._data = self._sub_data(other)
        return self

    def transpose(self) -> Matf:
        """TODO
        """
        return Mat2x2f(
                self._data[0], self._data[2],
                self._data[1], self._data[3])

    def m00(self) -> float:
        """TODO
        """
        return self._data[0]

    def m01(self) -> float:
        """TODO
        """
        return self._data[1]

    def m10(self) -> float:
        """TODO
        """
        return self._data[2]

    def m11(self) -> float:
        """TODO
        """
        return self._data[3]

class Mat1x3f(Matf):
    """TODO
    """

    def __init__(self,
            m00: float, m01: float, m02: float):
        """TODO
        """
        super().__init__([m00, m01, m02], 1, 3)

    def __add__(self, other: Matf) -> Matf:
        data_sum = self._add_data(other)
        return Mat1x3f(data_sum[0], data_sum[1], data_sum[2])

    def __iadd__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._add_data(other)
        return self

    def __sub__(self, other: Matf) -> Matf:
        """TODO
        """        
        data_dif = self._sub_data(other)
        return Mat1x3f(data_dif[0], data_dif[1], data_dif[2])

    def __isub__(self, other: Matf) -> Matf:
        """TODO
        """        
        self._data = self._sub_data(other)
        return self

    def transpose(self):
        """TODO
        """
        return Mat3x1f(self._data[0], self._data[1],self._data[1])

    def m00(self) -> float:
        """TODO
        """
        return self._data[0]

    def m01(self) -> float:
        """TODO
        """
        return self._data[1]

    def m02(self) -> float:
        """TODO
        """
        return self._data[2]

class Mat3x1f(Matf):
    """ TODO: mas
    """
    def __init__(self,
            m00: float,
            m10: float,
            m20: float):
        """TODO
        """
        super(Mat3x1f, self).__init__([m00, m10, m20], 3, 1)

    def __add__(self, other: Matf) -> Matf:
        """TODO
        """
        data_sum = self._add_data(other)
        return Mat3x1f(data_sum[0], data_sum[1], data_sum[2])

    def __iadd__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._add_data(other)
        return self

    def __sub__(self, other: Matf) -> Matf:
        """TODO
        """
        data_dif = self._sub_data(other)
        return Mat3x1f(data_dif[0], data_dif[1], data_dif[2])

    def __isub__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._sub_data(other)
        return self

    def transpose(self) -> Matf:
        """ Transposes the matrix

            It is important to notice that this method returns
            a newly created matrix. This is based on the Math
            structure this module has.
        """
        return Mat1x3f(self._data[0], self._data[1], self._data[2])

    def set_m00(self, m00: float) -> Matf:
        """TODO
        """
        self._data[0] = m00 
        return self

    def set_m01(self, m10: float) -> Matf:
        """TODO
        """
        self._data[1] = m10 
        return self

    def set_m02(self, m20: float) -> Matf:
        """TODO
        """
        self._data[2] = m20 
        return self

    def m00(self) -> float: 
        """TODO
        """
        return self._data[0]
    
    def m10(self) -> float: 
        """TODO
        """
        return self._data[1]
    
    def m20(self) -> float: 
        """TODO
        """
        return self._data[2]

class Mat3x3f(Matf):
    """ TODO: mas
    """
    def __init__(self,
            m00: float, m01: float, m02: float,
            m10: float, m11: float, m12: float,
            m20: float, m21: float, m22: float,):
        """TODO
        """
        super(Mat3x3f, self).__init__([m00, m01, m02, m10, m11, m12, m20, m21, m22], 3, 3)

    def __add__(self, other: Matf) -> Matf:
        """TODO
        """
        data_sum = self._add_data(other)
        return Mat3x3f(
                data_sum[0], data_sum[1], data_sum[2],
                data_sum[3], data_sum[4], data_sum[5],
                data_sum[6], data_sum[7], data_sum[8])

    def __iadd__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._add_data(other)
        return self

    def __sub__(self, other: Matf) -> Matf:
        """TODO
        """
        data_dif = self._sub_data(other)
        return Mat3x3f(
                data_dif[0], data_dif[1], data_dif[2],
                data_dif[3], data_dif[4], data_dif[5],
                data_dif[6], data_dif[7], data_dif[8])

    def __isub__(self, other: Matf) -> Matf:
        """TODO
        """
        self._data = self._sub_data(other)
        return self

    def transpose(self) -> Matf:
        """ Transposes the matrix

            It is important to notice that this method returns
            a newly created matrix. This is based on the Math
            structure this module has.
        """
        return Mat3x3f(
                self._data[0], self._data[3], self._data[6],
                self._data[1], self._data[4], self._data[7],
                self._data[2], self._data[5], self._data[8])

    def set_m00(self, m00: float) -> Matf:
        """TODO
        """
        self._data[0] = m00 
        return self

    def set_m01(self, m01: float) -> Matf:
        """TODO
        """
        self._data[1] = m01 
        return self

    def set_m02(self, m02: float) -> Matf:
        """TODO
        """
        self._data[2] = m02 
        return self

    def set_m10(self, m10: float) -> Matf:
        """TODO
        """
        self._data[3] = m10 
        return self

    def set_m11(self, m11: float) -> Matf:
        """TODO
        """
        self._data[4] = m11
        return self

    def set_m12(self, m12: float) -> Matf:
        """TODO
        """
        self._data[5] = m12
        return self

    def set_m20(self, m20: float) -> Matf:
        """TODO
        """
        self._data[6] = m20
        return self

    def set_m21(self, m21: float) -> Matf:
        """TODO
        """
        self._data[7] = m21
        return self
        
    def set_m22(self, m22: float) -> Matf:
        """TODO
        """
        self._data[8] = m22
        return self

    def m00(self) -> float: 
        """TODO
        """
        return self._data[0]
    
    def m01(self) -> float: 
        """TODO
        """
        return self._data[1]
    
    def m02(self) -> float: 
        """TODO
        """
        return self._data[2]
    
    def m10(self) -> float: 
        """TODO
        """
        return self._data[3]
    
    def m11(self) -> float: 
        """TODO
        """
        return self._data[4]
    
    def m12(self) -> float: 
        """TODO
        """
        return self._data[5]
    
    def m20(self) -> float: 
        """TODO
        """
        return self._data[6]

    def m21(self) -> float: 
        """TODO
        """
        return self._data[7]

    def m22(self) -> float: 
        """TODO
        """
        return self._data[8]

def dot_rows_cols(rows: list, cols: list) -> list:
    """TODO
    """
    data = list()
    for row in rows:
        for col in cols:
            cell = 0
            for idx in range(len(col)):
                cell += (row[idx] * col[idx])
            data.append(cell)
    return data

def dot(first: Matf, second: Matf) -> Matf:
    """TODO
    """
    if first.col_dimension() != second.row_dimension():
        raise RuntimeError("Invalid matrix dimensions for multiplication. l != n")
    data = dot_rows_cols(first.get_rows(), second.get_cols())
    if first.row_dimension() == 1:
        if second.col_dimension() == 1:
            return Mat1x1f(data[0])
        if second.col_dimension() == 2:
            return Mat1x2f(data[0], data[1])
        elif second.col_dimension() == 3:
            return Mat1x3f(data[0], data[1], data[2])
        elif second.col_dimension() == 4:
            raise NotImplementedError("TODO")
        else:
            raise RuntimeError("TODO")
    elif first.row_dimension() == 2:
        if second.col_dimension() == 2:
            return Mat2x2f(data[0], data[1], data[2], data[3])
        elif second.col_dimension() == 3:
            raise NotImplementedError("TODO")
        elif second.col_dimension() == 4:
            raise NotImplementedError("TODO")
        else:
            raise RuntimeError("TODO")
    elif first.row_dimension() == 3:
        if second.col_dimension() == 1:
            return Mat1x3f(data[0], data[1], data[2])
        elif second.col_dimension() == 2:
            return NotImplementedError("TODO")
        elif second.col_dimension() == 3:
            return Mat3x3f(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        elif second.col_dimension() == 4:
            return NotImplementedError("TODO")
        else:
            raise RuntimeError("TODO")
    elif first.row_dimension() == 4:
        if second.col_dimension() == 2:
            return NotImplementedError("TODO")
        elif second.col_dimension() == 3:
            return NotImplementedError("TODO")
        elif second.col_dimension() == 4:
            return NotImplementedError("TODO")
        else:
            raise RuntimeError("TODO")
    else:
        raise RuntimeError("TODO")

def switch_xy_to_yx(point: Mat2x1f) -> Mat2x1f:
    """TODO
    """
    return Mat2x1f(point.m10(), point.m00())

def switch_yx_to_xy(point: Mat2x1f) -> Mat2x1f:
    """TODO
    """
    return Mat2x1f(point.m10(), point.m00())

def left_right_2d(point: Mat2x1f) -> Mat2x1f:
    """TODO
    """
    return Mat2x1f(point.m00(), point.m01())

def right_left_2d(point: Mat2x1f) -> Mat2x1f:
    """TODO
    """
    return Mat2x1f(point.m00(), point.m01())

def left_right_3d(point: Mat3x1f) -> Mat3x1f:
    """TODO
    """
    return Mat3x1f(point.m00(), point.m01(), -point.m02())

def right_left_3d(point: Mat3x1f) -> Mat3x1f:
    """TODO
    """
    return Mat3x1f(point.m00(), point.m01(), -point.m02())

def rot_x_2d_radians(alpha: float) -> Mat2x2f:
    """TODO
    """
    return Mat2x2f(
            math.cos(alpha), -math.sin(alpha),
            math.sin(alpha), math.cos(alpha)
        )

def rot_x_cw_rad(alpha: float) -> Mat3x3f:
    """TODO
    """
    return Mat3x3f(
            1, 0, 0,
            0, math.cos(alpha), math.sin(alpha),
            0, -math.sin(alpha), math.cos(alpha)
        )

def rot_x_ccw_rad(alpha: float) -> Mat3x3f:
    """TODO
    """
    return Mat3x3f(
            1, 0, 0,
            0, math.cos(alpha), -math.sin(alpha),
            0, math.sin(alpha), math.cos(alpha)
        )

def rot_y_cw_rad(alpha: float) -> Mat3x3f:
    """TODO
    """
    return Mat3x3f(
            math.cos(alpha), 0, math.sin(alpha),
            0, 1, math.sin(alpha),
            -math.sin(alpha), 0, math.cos(alpha)
        )

def rot_y_ccw_rad(alpha: float) -> Mat3x3f:
    """TODO
    """
    return Mat3x3f(
            math.cos(alpha), 0, math.sin(alpha),
            0, 1, math.sin(alpha),
            -math.sin(alpha), 0, math.cos(alpha)
        )

def rot_z_cw_rad(alpha: float) -> Mat3x3f:
    """TODO
    """
    return Mat3x3f(
            math.cos(alpha), math.sin(alpha), 0,
            -math.sin(alpha), math.cos(alpha), 0,
            0, 0, 1
        )

def rot_z_ccw_rad(alpha: float) -> Mat3x3f:
    """TODO
    """
    return Mat3x3f(
            math.cos(alpha), -math.sin(alpha), 0,
            math.sin(alpha), math.cos(alpha), 0,
            0, 0, 1
        )  
