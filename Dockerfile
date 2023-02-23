FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime
RUN git clone https://github.com/AlexanderAuras/template.git &&\
    git checkout -b dev &&\
    python -m pip install --upgrade build &&\
    python -m build &&\
    python -m pip install --editable .[dev]