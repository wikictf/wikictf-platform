deploy:
    ( \
       source ~wikictf/wikienv/bin/activate; \
       pip install -r requirements.txt; \
       python wikictf/manage.py makemigrations --noinput; \
       python wikictf/manage.py makemigrations gameplatform --noinput; \
       python wikictf/manage.py migrate --noinput; \
       python wikictf/manage.py collectstatic --noinput; \

    )
