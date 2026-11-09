import numpy as np
import streamlit as st

from PIL import Image

st.title("Atv 4: RGB")

# 1. Leitura da foto

st.header("1. Leitura da foto")
col1, col2 = st.columns(2)

foto = Image.open("imagens/saubadia.jpeg")
img = np.array(foto)
col1.image(img)
col2.write(img.shape)
col2.write(img[100, 100])

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0

so_g = img.copy()
so_g[:, :, 0] = 0
so_g[:, :, 2] = 0

so_b = img.copy()
so_b[:, :, 0] = 0
so_b[:, :, 1] = 0

col1.image(r)
col1.image(g)
col1.image(g)

col2.image(so_r)
col2.image(so_g)
col2.image(so_b)

# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 0)
col1.image(quadrado, caption="amarelo")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (0, 255, 255)
col1.image(quadrado, caption="ciano")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 0, 255)
col1.image(quadrado, caption="magenta")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 255)
col1.image(quadrado, caption="branco")

col2.image(img, channels="BGR")

# quadrado = np.zeros((100, 100, 3), dtype=np.uint8)
# quadrado[:, :, 0] = 255
# st.image(quadrado)
# st.image(quadrado, channels="BGR")

# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)


r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)

soma = r + g + b
media = (soma / 3).astype(np.uint8)

soma_ponderada = 0.299 * r + 0.587 * g + 0.114 * b
media_ponderada = (soma_ponderada / (0.299 + 0.587 + 0.114)).astype(np.uint8)

col1.image(media, caption="média")
col2.image(media_ponderada, caption="média ponderada")