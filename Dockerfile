FROM python:3.6-buster
COPY ./uminifier /python_app/uminifier
COPY ./requirements.txt /python_app/requirements.txt
COPY ./setup.py /python_app/setup.py
WORKDIR /python_app
VOLUME /output
RUN pip install -r requirements.txt && \
    pip --version && pip install twine setuptools wheel && \
    python ./setup.py sdist bdist_wheel && \
    cp /dist/ /output
