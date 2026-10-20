import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz")

bandeira = np.zeros((6, 9, 3), dtype=np.uint8)
bandeira[:2, :] = (0, 0, 0)
bandeira[2:4, :] = (255, 255, 255)
bandeira[4:, :] = (20, 153, 84)

bandeira[:1, 0] = (255,0,0)
bandeira[1:2, 0:2] = (255,0,0)
bandeira[2:3, 0:3] = (255,0,0)

bandeira[3:4, 0:3] = (255,0,0)
bandeira[4:5, 0:2] = (255,0,0)
bandeira[5:6, 0:1] = (255,0,0)

st.image(ampliar(bandeira),caption="Bandeira da Palestina")
