from celery import Celery
import elasticsearch
from kombu.utils.url import _parse_url
from datetime import datetime
from celery.backends.elasticsearch import ElasticsearchBackend
from celery.app.backends import BACKEND_ALIASES
import json

class CustomElasticsearchBackend(ElasticsearchBackend):
    def __init__(self,url= None, *args, **kwargs):
        super(ElasticsearchBackend, self).__init__(url= url, *args, **kwargs)

        self.url = url
        _get = self.app.conf.get


        if url:
            _, host, port, username, password, path, _ = _parse_url(url)
            path = path.strip('/')
            index, _, doc_type = path.partition('/')
            self.username = username
            self.password = password
            self.index = index or self.index
            self.doc_type = doc_type or self.doc_type
            self.scheme = None
            self.host = host or self.host
            self.port = port or self.port

        self.es_retry_on_timeout = (
            _get('elasticsearch_retry_on_timeout') or self.es_retry_on_timeout
        )

        es_timeout = _get('elasticsearch_timeout')
        if es_timeout is not None:
            self.es_timeout = es_timeout

        es_max_retries = _get('elasticsearch_max_retries')
        if es_max_retries is not None:
            self.es_max_retries = es_max_retries

        self._server = None

    def set(self, key, value):
        try:
            body = value
            body = json.loads(value)
            #body['result'] = json.dumps(body['result'])
            body['@timestamp'] = '{0}Z'.format(datetime.utcnow().isoformat()[:-3])
            self._index(
                id=key,
                body=body,
            )
        except elasticsearch.exceptions.ConflictError:
            # document already exists, update it
            data = self.get(key)
            data[key] = value
            self._index(key, data, refresh=True)
        except Exception:
            raise


    def get(self, key):
        try:
            res = self.server.get(
                index=self.index,
                doc_type=self.doc_type,
                id=key,
            )
            try:
                if res['found'] == True:
                    del res['_source']['@timestamp']
                    #res['_source']['body'] = json.dumps(res['_source']['body'])
                    return json.dumps(res['_source'])

            except (TypeError, KeyError):
                pass
        except elasticsearch.exceptions.NotFoundError:
            pass # that is okay. it couldn't find


    def _get_server(self):
        """Connect to the Elasticsearch server."""
        return elasticsearch.Elasticsearch(
            ['%s:%s@%s:%s' % (self.username, self.password, self.host, self.port)],
            retry_on_timeout=self.es_retry_on_timeout,
            max_retries=self.es_max_retries,
            timeout=self.es_timeout
        )

