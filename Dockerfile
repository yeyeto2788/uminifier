FROM python:3.7-buster
LABEL maintainer="Juan Biondi <juanernestobiondi@gmail.com>"
COPY ./uminifier /python_app/uminifier
COPY ./requirements.txt /python_app/requirements.txt
COPY ./setup.py /python_app/setup.py
COPY ./README.md /python_app/README.md
WORKDIR /python_app
RUN pip --version &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt && \
    pip install twine setuptools wheel && \
    python ./setup.py install
ENTRYPOINT ["uminifier"]