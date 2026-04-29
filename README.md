🛡️ Monitoramento Inteligente de EPI com IA (YOLOv8)
Este projeto utiliza visão computacional de última geração para detectar em tempo real o uso de Equipamentos de Proteção Individual (EPIs) e a presença de pessoas em ambientes de trabalho.
Detecção Híbrida: Identifica simultaneamente classes padrão (Pessoas) e classes customizadas (EPIs como capacetes, luvas, etc.).

Alta Performance: Utiliza o framework Ultralytics YOLOv8.

Aceleração de Hardware: Suporte nativo para MPS (Metal Performance Shaders) para performance máxima em Macs e CUDA para Windows/Linux.

Feedback em Tempo Real: Visualização imediata via webcam com caixas delimitadoras (bounding boxes).

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.9+

Modelo de IA: YOLOv8 (Versões Nano e Small)

Bibliotecas: * ultralytics: Para processamento do modelo YOLO.

opencv-python: Para manipulação de frames de vídeo e interface.

torch: Para gestão dos tensores e aceleração de hardware.

📋 Pré-requisitos
Antes de rodar o projeto, certifique-se de ter as bibliotecas instaladas:

Bash
pip install ultralytics opencv-python torch
📂 Estrutura do Projeto
main.py: Código principal que gerencia a webcam e a lógica de detecção.

best.pt: Pesos do modelo treinado especificamente para detecção de EPIs.

requirements.txt: Lista de dependências para instalação rápida.

⚙️ Como Executar
Clone este repositório:

Bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
Certifique-se de que o arquivo best.pt está na pasta raiz do projeto.

Execute o script principal:

Bash
python main.py
Pressione a tecla 'q' para encerrar a aplicação.

🧠 Detalhes do Treinamento
O modelo customizado foi treinado utilizando o dataset PPE-Dataset via Roboflow, focado em segurança industrial. Foram utilizadas 25 épocas de treinamento com uma resolução de imagem de 640px, garantindo um equilíbrio entre velocidade e precisão (mAP).
