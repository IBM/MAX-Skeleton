FROM codait/max-base:v1.1.3

# Fill in these with a link to the bucket containing the model and the model file name
# ARG model_bucket=
# ARG model_file=

WORKDIR /workspace

ARG use_pre_trained_model=true

RUN if [ "$use_pre_trained_model" = "true" ] ; then\
    # download pre-trained model artifacts from Cloud Object Storage
    wget -nv --show-progress --progress=bar:force:noscroll ${model_bucket}/${model_file} --output-document=assets/${model_file} &&\
            tar -x -C assets/ -f assets/${model_file} -v && rm assets/${model_file} ; fi

COPY requirements.txt /workspace
RUN pip install -r requirements.txt

COPY . /workspace

RUN if [ "$use_pre_trained_model" = "true" ] ; then \
      # validate downloaded pre-trained model assets
      md5sum -c md5sums.txt ; \
    else \
      # rename the directory that contains the custom-trained model artifacts
      if [ -d "/workspace/custom_assets/" ] ; then \
        mv /workspace/custom_assets/* /workspace/assets ; \
      fi \
    fi

EXPOSE 5000

CMD python app.py
