import numpy as np
import math
"""
------ Libreria operaciones con numeros complejos
"""
# Version 1

import math
def sumcomplex(c1,c2):
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    return (real,imag)

def restcomplex(c1,c2):
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    return (real,imag)

def multcomplex(c1,c2):
    real = (c1[0] * c2[0]) - (c1[1] * c2[1])
    imag = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return (real,imag)

def divcomplex(c1,c2):
    real = round(((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0]**2) + (c2[1]**2)),2)
    imag = round(((c2[0] * c1[1]) - (c1[0] * c2[1])) / ((c2[0]**2) + (c2[1]**2)),2)
    return (real,imag)

def moducomplex(c):
    return round(math.sqrt((c[0] ** 2) + (c[1] ** 2)),2)

def conjucomplex(c):
    return (c[0], -1 * c[1])

def cartesian_to_polar_complex(c):
    x = c[0]
    y = c[1]
    r = round(math.sqrt(x**2 + y**2),2)
    theta = round(math.atan2(y, x))
    return (r, theta)

def fase_complex(c):
    return round(math.atan2(c[1],c[0]),2)

def sumacpmx(c1, c2):
    """1: Adición de vectores complejos"""
    suma = []
    for i in range(0, len(c1)):
        suma.append(c1[i] + c2[i])
    return suma

def inversocpmx(c):
    """2: Inverso (aditivo) de un vector complejos."""
    inve = []
    for i in range(len(c)):
        inve.append(-c[i])
    return inve

def mult_esca_vect_cpmx(e,v):
    """3: Multiplicación de un escalar por un vector complejo."""
    mult = []
    for i in range(len(v)):
        mult.append(e * v[i])
    return mult

def suma_mat_complex(mat1,mat2):
    """4: Adición de matrices complejas."""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "No son matrices compatibles"
    else:
        matrix = [[0 for i in range(len(mat1))] for j in range(len(mat1[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = mat1[i][j] + mat2[i][j]
        return matrix

def mat_inv_cpmx(mat):
    """5 :Inversa (aditiva) de una matriz compleja."""
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = -mat[i][j]
    return mat

def mat_mult_esc_cpmx(k, mat):
    """6: Multiplicación de un escalar por una matriz compleja."""
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = k * mat[i][j]
    return mat

def mat_traspone_cpmx(mat):
    """7: Transpuesta de una matriz/vector"""
    m = len(mat)
    n = len(mat[0])
    matrix = [[0 for i in range(m)] for j in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[j][i] = mat[i][j]
    return matrix

def neg_imag_matrix_cpmx(mat):
    """8: Conjugada de una matriz/vector"""
    dis = len(mat)
    dis2 = len (mat[0])
    for i in range(dis):
        for j in range(dis2):
            mat[i][j] = mat[i][j].conjugate()
    return mat

def adjunta_daga_cpmx(mat):
    """9: Adjunta (daga) de una matriz/vector"""
    return mat_traspone_cpmx(neg_imag_matrix_cpmx(mat))

def product_mat(mat1,mat2):
    """10: Producto de dos matrices (de tamaños compatibles)"""
    m1 = len(mat1)
    n1 = len(mat1[0])
    m2 = len(mat2)
    n2 = len(mat2[0])
    if n1 != m2:
        return "No son matrices compatibles"
    else:
        matri = [[0 for row in range(n2)] for col in range(m1)]
        for i in range(m1):
            for j in range(n2):
                for k in range(m2):
                    matri[i][j] += mat1[i][k] * mat2[k][j]
        return matri

def accion_mat(matrix, vect1):
    """11: Función para calcular la "acción" de una matriz sobre un vector."""
    m, n = len(matrix), len(matrix[0])
    resp = []
    if len(vect1) == n:
        matinit = (0, 0)
        for i in range(m):
            for j in range(len(matrix[i])):
                ope = multcomplex(matrix[i][j], vect1[j])
                matinit = sumcomplex(ope, matinit)
            resp += [matinit]
            matinit = (0, 0)
        return resp
    else:
        return "Size Error"

def produc_interno_vec(vector_1,vector_2):
    """12: Producto interno de dos vectores"""
    sum = 0
    if len(vector_1) != len(vector_2):
        return "No son vectores compatibles. "
    else:
        for i in range(len(vector_1)):
            sum+= vector_1[i]*vector_2[i]
    return sum

def norma_vector(vec):
    """13: Norma de un vector."""
    sum = 0
    for i in range(len(vec)):
        sum+=abs(vec[i])**2
        print(sum)
    return round((sum)**0.5, 2)

def distance_vect(vect_1, vect_2):
    """14: Distancia entre dos vectores."""
    resta = []
    for i in range(0, len(vect_1)):
        resta.append((vect_1[i] - vect_2[i]))
    ver = str(resta[0])
    val = []
    for i in range(len(ver)):
        if ver[i] == "+" or ver[i] == "-":
            val.append(ver[i-1])
            val.append(ver[i+1])
            break
    su = 0
    for i in range(2):
        su+=int(val[i])**2
    return round(su**0.5, 2)

def val_vec_prop_mat(mat):
    """15. Valores  y vectores propios de una matriz."""
    if len(mat) != len(mat[0]):
        return "No es una matriz cuadrada"
    matriz = np.array(mat)
    valores_propios, vectores_propios = np.linalg.eig(matriz)
    return "los valores propios para esta matriz o vector son {} y los vectores son {}".format(valores_propios, vectores_propios)

def mat_unita(mat):
    """16. Revisar si una matriz es unitaria."""
    long_f = len(mat)
    long_c = len(mat[0])
    if long_c != long_f:
        return "La matriz no es cuadrada"
    for i in range(long_f):
        for j in range(long_c):
            if i == j:
                if mat[i][j] == 1:
                    continue
            else:
                if mat[i][j] != 0:
                    return "No es unitaria"
    return "Si es matriz unitaria"

def mat_hermitiana(mat):
    """17. Revisar si una matriz es Hermitiana."""
    m = len(mat)
    n = len(mat[0])
    mat2 = mat_traspone_cpmx(mat)
    for row in range(m):
        for column in range(n):
            if mat[row][column] != (mat2[row][column]).conjugate():
                return "No es hermitiana"
    return "Es hermimtiana"


def prod_tense_mat(mat1, mat2):
    """18. Producto tensor de dos matrices/vectores."""
    m = len(mat1)
    n = len(mat2)
    m1 = len(mat1[0])
    n1 = len(mat2[0])
    fil = m * n
    col = n1 * m1
    matriz = [[0 for row in range(fil)]for column in range(col)]
    for j in range(fil):
        for k in range(col):
            matriz[j][k] = (mat1[j//n][k//n1] * mat2[j%n][k%n1])
    return matriz

def normal(vec):
    suma = 0
    for i in range(len(vec)):
        suma+=abs(vec[i])**2
    return suma**0.5

def module_vector(vec):
    return vec.real**2 + vec.imag**2

def normalizar_vector(vec):
    nor = normal(vec)
    for i in range(len(vec)):
        vec[i] = vec[i]/nor
    return vec

def probabilidad(vec,pos):
    x = vec[pos]
    val = abs(x)**2
    prope = normal(vec)
    return val/prope**2

def transicion(vec1,vec2):
    re = produc_interno_vec(vec2,vec1)
    b = re/(normal(vec1))*(normal(vec2))
    return module_vector(b)

def is_bolean(matriz):
    """Verifica si una matriz es Bolleana"""
    x1 = len(matriz)
    x2 = len(matriz[0])
    for i in range(x1):
        for j in range(x2):
            if (matriz[i][j] != 0):
                if (matriz[i][j] != 1):
                    return False
    return True

def add(c1, c2):
    re = c1[0] + c2[0]
    im = c1[1] + c2[1]
    resp = re, im
    return resp

def multi(c1, c2):
    re = c1[0]*c2[0] - c1[1]*c2[1]
    im = c1[0]*c2[1] + c1[1]*c2[0]
    resp = re, im
    return resp

def sub(c1, c2):
    re = c1[0] - c2[0]
    im = c1[1] - c2[1]
    resp = re, im
    return resp

def div(c1, c2):
    if c2[0] != 0 or c2[1] != 0:
        re = round(((c1[0]*c2[0])+(c1[1]*c2[1]))/(c2[0]**2+c2[1]**2), 3)
        im = round(((c2[0]*c1[1])-(c1[0]*c2[1]))/(c2[0]**2+c2[1]**2), 3)
        resp = re, im
        return resp

    else:
        raise ValueError('Can not divide by zero')
def mod(c1):
    m = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
    return m

def conj(c1):
    re = c1[0]
    im = c1[1]*-1
    resp = re, im
    return resp


def polar(c1):
    if c1[0] < 0 and c1[1] < 0:
        p = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
        o = round(2*math.pi-(-1*(math.atan2(c1[1], c1[0]))), 2)
        resp = p, o
        return resp
    elif c1[0] > 0 > c1[1]:
        p = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
        o = round((2*math.pi + math.atan2(c1[1], c1[0])), 2)
        resp = p, o
        return resp
    else:
        p = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
        o = round((math.atan2(c1[1], c1[0])), 2)
        resp = p, o
        return resp

def cart(c1):
    re = round(c1[0]*math.cos(c1[1]))
    im = round(c1[0]*math.sin(c1[1]))
    resp = re, im
    return resp


def phase(c1):
    if c1[0] < 0 and c1[1] < 0:
        ph = round(2 * math.pi - (-1 * (math.atan2(c1[1], c1[0]))), 2)
        return ph
    elif c1[0] > 0 > c1[1]:
        ph = round((2 * math.pi + math.atan2(c1[1], c1[0])), 2)
        return ph
    else:
        ph = round((math.atan2(c1[1], c1[0])), 2)
        return ph

def f_aux(product):
    aux = 0
    if product[0][0][0] != 1 and product[0][1][0] == 0:
            if product[0][0][0] > 0:
                aux = (1/(product[0][0][0]))
            elif product[0][0][0] < 0:
                aux = (-1/(product[0][0][0]))
    return aux

def length(v1, v2):
    if len(v1) == len(v2):
        return True
    else:
        return False


def diagonal(m):
    mI = [[(0, 0) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j:
                mI[i][j] = (1, 0)
    return mI


def conj_tup(c1):
    re = c1[0]
    im = c1[1] * -1
    res = re, im
    return res



def v_add(v1, v2):
    if length(v1, v2):
        m = []
        for index in range(len(v1)):
            m += [ComplexCalculator.add(v1[index], v2[index])]
        return m
    else:
        return 'Error: Different length vector'



def v_inv_add(v1):
    m = []
    for index in range(len(v1)):
        m += [ComplexCalculator.sub(v1[index], v1[index])]
    return m



def v_scalar(sc, v1):
    m = []
    for index in range(len(v1)):
        m += [ComplexCalculator.multi(sc, v1[index])]
    return m

def m_add(m1, m2):
    m = []
    if length(m1, m2):
        for row in range(len(m1)):
            m += [v_add(m1[row], m2[row])]
        return m

def m_inv_add(m1):
    m = []
    for row in range(len(m1)):
        m += [v_inv_add(m1[row])]
    return m




def m_scalar(sc, m1):
    m = []
    for row in range(len(m1)):
        m += [v_scalar(sc, m1[row])]
    return m


def m_action(m1, v1):
    return accion_mat(m1, v1)

def m_unit(m1):
    if length(m1, m1[0]):
        mI = diagonal((len(m1)))
        m2 = m_adj(m1)
        product = m_mul(m1, m2)
        flag = True
        aux = f_aux(product)
        for i in range(len(m1)):
            for j in range(len(m1)):
                if product[i][j] != mI[i][j]:
                    flag = False
        if flag:
            return "Is Unitary"
        else:
            return "Is not Unitary"
    else:
        return "The input have to be a square matrix"

