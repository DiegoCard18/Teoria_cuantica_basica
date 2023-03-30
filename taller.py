import libe as libreria
import numpy as np

def mat_diagonal(m):
    m1 = [[(0, 0) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j:
                m1[i][j] = (1, 0)
    return m1

def probabilidad(kep, pos):
    normsl = libreria.vec_nom(kep)
    pos_2 = libreria.module_complex(kep[pos]) ** 2
    res = round((pos_2/normsl ** 2)*100, 2)
    return res

def amplitud(K1, K2):
    v_1 = []
    for i in range(len(K2)):
        temp = [K2[i]]
        v_1 += [temp]
    K2 = libreria.conjugar_matrix(v_1)
    v_2 = []
    for i in range(len(K2)):
        v_2 += K2[i]
    nor1 = libreria.vec_nom(K1)
    norm_2 = libreria.vec_nom(v_2)
    norm = nor1 * norm_2
    probili = [libreria.val_ine(v_2, K1)]
    punto = libreria.valor_escalar((1 / norm, 0), probili)[0]
    punto = (round(punto[0], 2), round(punto[1], 2))
    return punto

def media(observable, K):
    K_aux = []
    for index in range(len(K)):
        aux = [K[index]]
        K_aux += [aux]
    if libreria.mat_hermitani(observable):
        vel = libreria.conjugar_matrix(K_aux)
        ac = libreria.accion_matrix(observable, K_aux)
        punto = libreria.val_ine(ac, vel)
        punto = (round(punto[0], 2), round(punto[1], 2))
        return punto
    else:
        return "No es un observable"

def varianza(observable, K):
    Ket_aux = []
    for index in range(len(K)):
        aux = [K[index]]
        Ket_aux += [aux]
    Bra = libreria.conjugar_matrix(Ket_aux)
    med = media(observable, K)
    id_med = [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
    for i in range(len(observable)):
        for j in range(len(observable[i])):
            if i == j:
                id_med[i][j] = libreria.umlti_complex((-1, 0), med)
    id_med = libreria.adicion_matrix(id_med, observable)
    cudrado = libreria.mult_matrices(id_med, id_med)
    action = libreria.accion_matrix(cudrado, Ket_aux)
    return libreria.val_ine(action, Bra)

def valores_vectores(observable):
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


def probabilidades_vectores(inicial, observable, posicion):
    vectores = valores_vectores(observable)
    return amplitud(inicial, vectores[posicion])

def dinamica(mat_u, v1, t):
    if libreria.verifi_mat_unitary(mat_u):
        for index in range(t):
            v1 = libreria.accion_matrix(mat_u, v1)
        return v1
    else:
        return "Matriz no valida"


if __name__ == '__main__':
    print("Ejercicio 4.3.1")
    #Ejercicio 4.3.1
    #v = [[(1, 0)], [(0, 0)]]
    #observable = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    #vr = libreria.accion_matrix(observable, v)
    #ob = observable
    #observable = np.array(observable)
    #vectores = np.linalg.eig(observable)
    #print(vr)
    #print(vectores)

    #Ejercicio 4.3.2
    print("Ejercicio 4.3.2")
    #p1 = probabilidades_vectores(vr, ob, 1)
    #print(p1)

    # Excercise 4.4.1
    print("Ejercicio 4.4.1")
    #vector_41 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    #vector_42 = [[((2**(1/2))/2, 0), ((2**(1/2))/2, 0)], [((2**(1/2))/2, 0), (-(2**(1/2))/2, 0)]]
    #if m_unitaria(vector_41) and m_unitaria(vector_42):
    #    print(m_unitaria(libreria.m_mul(v1_4,v2_4)))

    # Excercise 4.4.2
    print("Excercise 4.4.2")
    #print(dinamica([[(0, 0), (1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)],[(1/(2**(1/2)), 0), (0, 0), (0, 0), (-1/(2**(1/2)), 0)],[(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],[(0, 0), (-1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)]],[(1,0), (0,0), (0,0), (0,0)], 3))
    #print(dinamica([[(0, 0), (1 / (2 ** (1 / 2)), 0), (1 / (2 ** (1 / 2)), 0), (0, 0)],[(0, 1 / (2 ** (1 / 2))), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],[(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (0, 1 / (2 ** (1 / 2)))],[(0, 0), (1 / (2 ** (1 / 2)), 0), (-1 / (2 ** (1 / 2)), 0), (0, 0)]],[(1, 0), (0, 0), (0, 0), (0, 0)], 3))