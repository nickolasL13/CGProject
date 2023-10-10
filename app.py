import streamlit as st
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
sys.path.append('./utils')
from figura import FiguraR2

st.title('Trabalho de Computação Gráfica')

option = st.selectbox(
    'Selecione a opção entre as implementações:',
    ('Rasterização de Retas', 'Rasterização de Polígonos Convexos', 'Rasterização de Curvas Hermite'),
    index=None,
)

if option == 'Rasterização de Retas':

    st.write('**Crie seu espaço:**')

    col1, col2 = st.columns(2)

    with col1:
        x = st.slider('Selecione o valor de X da resolução', 0, 1920, step=1, value=300)
        y = st.slider('Selecione o valor de Y da resolução', 0, 1920, step=1, value=300)

    with col2:
        w = st.slider('Selecione a largura da imagem (width)', 1.0, 4.0, step=0.01, value=1.0)
        h = st.slider('Selecione a altura da imagem (height)', 1.0, 4.0, step=0.01, value=1.0)

    if st.button('Gerar espaço:'):

        matplotlib.rcParams.update({'font.size': int(np.max([w,h])*2)})

        img = np.ones((y, x))

        fig, ax = plt.subplots(figsize=(w, h))
        ax.imshow(img, cmap='gray', origin='lower', vmin=0, vmax=1, aspect='auto')

        st.pyplot(fig, use_container_width=False)


