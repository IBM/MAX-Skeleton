FROM codait/max-base:v1.1.3

# Fill in these with a link to the bucket containing the model and the model file name
# ARG model_bucket=
# ARG model_file=

WORKDIR /workspace

RUN wget -nv --show-progress --progress=bar:force:noscroll ${model_bucket}/${model_file} --output-document=assets/${model_file} && \
  tar -x -C assets/ -f assets/${model_file} -v && rm assets/${model_file}

COPY requirements.txt /workspace
RUN pip install -r requirements.txt

COPY . /workspace

# check file integrity
RUN md5sum -c md5sums.txt

EXPOSE 5000

CMD python app.py
