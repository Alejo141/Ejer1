{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ba77b81-c330-4f00-a974-834c740b1447",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# Función para procesar los archivos Excel\n",
    "def procesar_archivos(carpeta_origen, archivo_salida):\n",
    "    datos_consolidados = []\n",
    "\n",
    "    for archivo in os.listdir(carpeta_origen):\n",
    "        if archivo.endswith('.xlsx') and not archivo.startswith('~$'):\n",
    "            ruta_archivo = os.path.join(carpeta_origen, archivo)\n",
    "            try:\n",
    "                df = pd.read_excel(ruta_archivo, sheet_name=1)\n",
    "                \n",
    "                columna_1 = df.iloc[:, 0] # Identificacion\n",
    "                columna_2 = df.iloc[:, 2].astype(str).str.replace(\"-\", \"\") # Factura\n",
    "                columna_3 = df.iloc[:, 6] # Centro costos\n",
    "                columna_4 = df.iloc[:, 7] # Saldo cartera\n",
    "                columna_5 = df.iloc[:, 9] # mes\n",
    "                columna_6 = df.iloc[:, 10] # año\n",
    "\n",
    "                for valor1, valor2, valor3, valor4, valor5, valor6 in zip(columna_1, columna_2, columna_3, columna_4, columna_5, columna_6):\n",
    "                    datos_consolidados.append({\n",
    "                        'Archivo': archivo,\n",
    "                        'Identificacion': valor1,\n",
    "                        'Factura': valor2,\n",
    "                        'Centro de Costo': valor3,\n",
    "                        'Saldo Factura': valor4,\n",
    "                        'Mes': valor5,\n",
    "                        'Año': valor6\n",
    "                    })\n",
    "            except Exception as e:\n",
    "                st.warning(f\"Error procesando {archivo}: {e}\")\n",
    "\n",
    "    if datos_consolidados:\n",
    "        df_consolidado = pd.DataFrame(datos_consolidados)\n",
    "        df_consolidado.to_excel(archivo_salida, index=False)\n",
    "        return df_consolidado, archivo_salida\n",
    "    else:\n",
    "        return None, None\n",
    "\n",
    "# Interfaz de Streamlit\n",
    "st.title(\"Consolidación de Archivos Excel\")\n",
    "\n",
    "carpeta_origen = st.text_input(\"Ruta de la carpeta de origen:\", \"H:/Mi unidad/01. ZNI EXPERT/1. EMPRESAS/5. DISPOWER/5. Calculos 026/Cartera Dispower\")\n",
    "archivo_salida = st.text_input(\"Ruta del archivo de salida:\", \"H:/Mi unidad/01. ZNI EXPERT/1. EMPRESAS/5. DISPOWER/5. Calculos 026/Cartera Dispower/conso_cartera.xlsx\")\n",
    "\n",
    "if st.button(\"Procesar Archivos\"):\n",
    "    if os.path.exists(carpeta_origen):\n",
    "        with st.spinner(\"Procesando archivos...\"):\n",
    "            df_consolidado, archivo_salida_generado = procesar_archivos(carpeta_origen, archivo_salida)\n",
    "            if df_consolidado is not None:\n",
    "                st.success(f\"Datos consolidados guardados en: {archivo_salida_generado}\")\n",
    "                st.dataframe(df_consolidado)\n",
    "            else:\n",
    "                st.error(\"No se encontraron datos válidos para consolidar.\")\n",
    "    else:\n",
    "        st.error(\"La carpeta de origen no existe. Verifique la ruta ingresada.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
