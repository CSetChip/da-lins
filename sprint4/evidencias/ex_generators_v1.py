from ex_generators_v0 import cores_arco_iris

if __name__ == '__main__':
    generator = cores_arco_iris()
    for cor in generator:
        print(cor)
    print('Fim')