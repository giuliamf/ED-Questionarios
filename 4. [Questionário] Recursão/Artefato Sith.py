def buscarArtefato():
    verificar = bb8.verificarChao()
    if verificar:
        return verificar

    if bb8.verificarSeFoiVisitado():
        return

    bb8.registrarComoVisitado()

    if bb8.verificarNorte():
        bb8.moverNorte()
        verificar = buscarArtefato()
        if verificar:
            return verificar
        bb8.moverSul()

    if bb8.verificarSul():
        bb8.moverSul()
        verificar = buscarArtefato()
        if verificar:
            return verificar
        bb8.moverNorte()

    if bb8.verificarLeste():
        bb8.moverLeste()
        verificar = buscarArtefato()
        if verificar:
            return verificar
        bb8.moverOeste()

    if bb8.verificarOeste():
        bb8.moverOeste()
        verificar = buscarArtefato()
        if verificar:
            return verificar
        bb.moverLeste()
