import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("Desafio python bootcamp DIO - AI102 - Upload de arquivos fakes")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=['docx', 'jpg', 'pdf', 'txt', 'jpeg', 'png'])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso!")
            credit_card_info = analize_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName}")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption='Imagem enviada')
    st.write("Resultado da validação do cartão de crédito:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular do cartão: {credit_card_info['card_name']}")
        st.write(f"Validade do cartão: {credit_card_info['card_date']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Não foi possível validar o cartão de crédito")



if __name__ == '__main__':
    configure_interface()