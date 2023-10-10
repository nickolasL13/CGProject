class FiguraR2:

  def __init__(self):
    self.listaPontos = []
    self.listaPontosNomes = []
    self.listaArestas = []
    self.listaArestasNomes = []
    self.listaFaces = []
    self.listaFacesNomes = []

  def addPonto(self, x, y, rotulo):
    if ([x,y] not in self.listaPontos) and (rotulo not in self.listaPontosNomes):
      self.listaPontos.append([x, y])
      self.listaPontosNomes.append(rotulo)
    else:
      print(f"O ponto [{x},{y}] ou o nome ({rotulo}) já existem na figura.")

  def addAresta(self, p1, p2, rotulo):

    try:
      index1 = self.listaPontosNomes.index(p1)
      index2 = self.listaPontosNomes.index(p2)

      ponto1 = self.listaPontos[index1]
      ponto2 = self.listaPontos[index2]

      if ([ponto1, ponto2] not in self.listaArestas) and ([ponto2, ponto1] not in self.listaArestas) and (rotulo not in self.listaArestasNomes) and (ponto1 != ponto2):
        self.listaArestas.append([ponto1, ponto2])
        self.listaArestasNomes.append(rotulo)
      else:
        if ponto1 == ponto2:
          print(f"Os pontos {p1} e {p2} são iguais.")
        else:
          print(f"A aresta [{ponto1},{ponto2}] ou o nome ({rotulo}) já existem na figura.")

    except Exception as error:
      print(f"Não foi possível achar os pontos. Erro: {error}")

  def addFace(self, arestas, rotulo):

    face = []

    try:
      for i in arestas:
        indexAresta = self.listaArestasNomes.index(i)
        face.append(self.listaArestas[indexAresta])

      if (face not in self.listaFaces) and (rotulo not in self.listaFacesNomes) and (len(face) >= 3):
        self.listaFaces.append(face)
        self.listaFacesNomes.append(rotulo)
      else:
        if len(face) < 3:
          print(f"É necessário no mínimo 3 arestas, {len(face)} foram passadas.")
        else:
          print(f"A face {face} ou o nome ({rotulo}) já existem na figura.")

    except Exception as error:
      print(f"Não foi possível achar as arestas. Erro: {error}")

  def pontosAresta(self, aresta):
    if aresta in self.listaArestasNomes:
      indexAresta = self.listaArestasNomes.index(aresta)
      return self.listaArestas[indexAresta]
    else:
      print(f"Não existe a aresta {aresta}")

  def arestasFace(self, face):
    if face in self.listaFacesNomes:
      indexFace = self.listaFacesNomes.index(face)
      return self.listaFaces[indexFace]
    else:
      print(f"Não existe a face {face}")
