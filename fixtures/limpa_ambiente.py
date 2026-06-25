"""Fixtures e funções para manter o sistema limpo"""

import pytest
import os
import re

from conftest import VIDEO_PATH


# @pytest.fixture(scope="session", autouse=True)
# def fixt_apaga_videos_antigos():
#     """Fixture para apagar os vídeos no começo de uma nova sessão de testes"""
    
#     # Itera por todos os arquivos
#     for file in os.scandir(VIDEO_PATH):
        
#         # Garante que o arquivo seja um vídeo, para evitar apagamentos indesejados
#         if re.search(r"\.webm$", file.path):

#             # Remove o arquivo
#             os.remove(file.path)