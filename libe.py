import math
import cal_matrix_cpmx as cal
import numpy as np
def suma_complex(c1, c2):
    re = c1[0] + c2[0]
    im = c1[1] + c2[1]
    resp = re, im
    return resp

def umlti_complex(c1, c2):
    re = c1[0]*c2[0] - c1[1]*c2[1]
    im = c1[0]*c2[1] + c1[1]*c2[0]
    resp = re, im
    return resp

def resta_complex(c1, c2):
    re = c1[0] - c2[0]
    im = c1[1] - c2[1]
    resp = re, im
    return resp

def div_complex(c1, c2):
    if c2[0] != 0 or c2[1] != 0:
        re = round(((c1[0]*c2[0])+(c1[1]*c2[1]))/(c2[0]**2+c2[1]**2), 3)
        im = round(((c2[0]*c1[1])-(c1[0]*c2[1]))/(c2[0]**2+c2[1]**2), 3)
        resp = re, im
        return resp
    else:
        raise ValueError('Can not divide by zero')

def module_complex(c1):
    m = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
    return m

def conjugate_complex(c1):
    re = c1[0]
    im = c1[1]*-1
    resp = re, im
    return resp

def fase_aux(product):
    aux = 0
    if product[0][0][0] != 1 and product[0][1][0] == 0:
            if product[0][0][0] > 0:
                aux = (1/(product[0][0][0]))
            elif product[0][0][0] < 0:
                aux = (-1/(product[0][0][0]))
    return aux

def verificar_longitud(v1, v2):
    if len(v1) == len(v2):
        return True
    else:
        return False

def mat_diagonal(m):
    mI = [[(0, 0) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j:
                mI[i][j] = (1, 0)
    return mI

def conjugar_vector(c1):
    re = c1[0]
    im = c1[1] * -1
    res = re, im
    return res

def vector_anadir(v1, v2):
    if verificar_longitud(v1, v2):
        m = []
        for index in range(len(v1)):
            m += [suma_complex(v1[index], v2[index])]
        return m
    else:
        return 'Error: Different length vector'

def v_inv_add(v1):
    m = []
    for index in range(len(v1)):
        m += [resta_complex(v1[index], v1[index])]
    return m

def valor_escalar(sc, v1):
    m = []
    for index in range(len(v1)):
        m += [umlti_complex(sc, v1[index])]
    return m

def adicion_matrix(m1, m2):
    m = []
    if verificar_longitud(m1, m2):
        for row in range(len(m1)):
            m += [vector_anadir(m1[row], m2[row])]
        return m

def m_inv_add(m1):
    m = []
    for row in range(len(m1)):
        m += [v_inv_add(m1[row])]
    return m

def m_scalar(sc, m1):
    m = []
    for row in range(len(m1)):
        m += [valor_escalar(sc, m1[row])]
    return m

def at_transicion(m1):
    m = [[(0, 0) for i in range(len(m1))] for j in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m[j][i] = m1[i][j]
    return m

def conjugar_matrix(m1):
    m2 = [[(0, 0) for j in range(len(m1[0]))] for i in range(len(m1))]
    for row in range(len(m1)):
        for column in range(len(m1[0])):
            m2[row][column] = conjugar_vector(m1[row][column])
    return m2

def vec_nom(v1):
    aux = 0
    for index in range(len(v1)):
        aux += (module_complex(v1[index]) ** 2)
    return round(math.sqrt(aux), 2)

def vector_distancia(v1, v2):
    if verificar_longitud(v1, v2):
        v = []
        for index in range(len(v1)):
            v += [resta_complex(v1[index], v2[index])]
        dist = abs(vec_nom(v))
        return dist
    else:
        return 'Error: Different length vector'
def matrix_daga(m1):
    m2 = [[m1[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    m2 = conjugar_matrix(m2)
    m2 = at_transicion(m2)
    return m2

def mult_matrices(m1, m2):
    if len(m1[0]) == len(m2):
        m = [[(0, 0) for i in range(len(m2[0]))] for j in range(len(m1))]
        for row in range(len(m1)):
            for column in range(len(m2[0])):
                for aux in range(len(m1[0])):
                    m[row][column] = suma_complex(m[row][column], umlti_complex(m1[row][aux], m2[aux][column]))
        return m
    else:
        return "Length error"

def accion_matrix(m1, v1):
    return mult_matrices(m1, v1)

def val_ine(v1, v2):
    point = (0, 0)
    if verificar_longitud(v1, v2):
        for index in range(len(v1)):
            aux = umlti_complex(v1[index], v2[index])
            point = suma_complex(point, aux)
        return point
    else:
        return "Length error"
def product_tensor(m1, m2):
    mt = [[[] for j in range(len(m1[0]))] for i in range(len(m1))]
    for row in range(len(m1)):
        for column in range((len(m1[0]))):
            sc = m1[row][column]
            mt[row][column] = m_scalar(sc, m2)
    return

def verifi_mat_unitary(m1):
    if verificar_longitud(m1, m1[0]):
        maty = mat_diagonal((len(m1)))
        m2 = matrix_daga(m1)
        product = mult_matrices(m1, m2)
        rest = True
        for i in range(len(m1)):
            for j in range(len(m1)):
                if product[i][j] != maty[i][j]:
                    rest = False
        if rest:
            return True
        else:
            return False
    else:
        return False

def mat_hermitani(m1):
    flag = True
    m2 = matrix_daga(m1)
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j] != m2[i][j]:
                flag = False
    if flag:
        return "Es hermitian"
    else:
        return "No es hermitian"

def val_vect(observable):
    valores, vectores = np.linalg.eig(observable)
    lista_valores = []
    lista_vectores = []
    for index in range(len(valores)):
        lista_valores += [(valores[index].real, valores[index].imag)]
    for index in range(len(vectores)):
        vector = []
        for index_2 in range(len(vectores[0])):
            vector += [(vectores[index][index_2].real, vectores[index][index_2].imag)]
        lista_vectores += [vector]
    return lista_valores, lista_vectores

def val_prop_mat_numpy(mat):
    valores_propios, vectores_propios = np.linalg.eig(mat)
    return valores_propios#"los valores propios para esta matriz o vector son {} y los vectores son {}".format(valores_propios, vectores_propios)

def vec_prop_mat_numpy(mat):
    valores_propios, vectores_propios = np.linalg.eig(mat)
    return vectores_propios#"los valores propios para esta matriz o vector son {} y los vectores son {}".format(valores_propios, vectores_propios)

def varianza(mat1,mat2):
    mat1 = np.matrix(mat1)
    mat2 = np.matrix(mat2)
    landa1 = mat1-mat2
    rest = val_prop_mat_numpy(landa1)
    product = np.dot(rest, rest)
    return product

def transicion(v1,v2):
    b = cal.produc_interno_vec(v2,v1)
    b = b/(cal.normal(v1)*cal.normal(v2))
    prob = cal.module_vector(b)
    return prob

def media(matrix,ket):
    if cal.normal(ket) != 1:
        ket = cal.normalizar_vector(ket)
    resp = cal.mat_hermitiana(matrix)
    if resp == "La madrix no es hermitiana" or resp == "Error, el tamaño de matrix es incorrrecto":
        return resp
    else:
        med = cal.produc_interno_vec(cal.accion_mat(matrix,ket),ket)
        return med.real

def transitar_a_vectores(mat,ket):
    if cal.normalizar_vector(ket) != 1:
        ket = cal.normalizar_vector(ket)
    vectores = vec_prop_mat_numpy(mat)
    valores = val_prop_mat_numpy(mat)
    prob = []
    for i in range(len(vectores)):
        proba = transicion(ket,vectores[i])
        prob.append(proba)
    return prob