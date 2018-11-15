2018-11-15 01:44:19 default[20181115t083510]  Traceback (most recent call last):
File "/env/local/lib/python2.7/site-packages/flask/app.py", line 1982, in wsgi_app
response = self.full_dispatch_request()
File "/env/local/lib/python2.7/site-packages/flask/app.py", line 1614, in full_dispatch_request
rv = self.handle_user_exception(e)

File "/env/local/l
ib/python2.7/site-packages/flask/app.py", line 1517, in handle_user_exception      reraise(exc_type, exc_value, tb)    File "/env/local/lib/python2.7/site-packages/flask/app.py", line 16
12, in full_dispatch_request      rv = self.dispatch_request()

File "/env/local/lib/python2.7/site-packages/flask/app.py", line 1598, in dispatch_request      return self.view_functio
ns[rule.endpoint](**req.view_args)    File "/env/local/lib/python2.7/site-packages/dash/dash.py", line 551, in dispatch      return self.callback_map[target_id]['callback'](*args)    Fil
e "/env/local/lib/python2.7/site-packages/dash/dash.py", line 508, in add_context

output_value = func(*args, **kwargs)    File "/home/vmagent/app/main.py", line 77, in update_graph
     df = web.DataReader(tic,'iex',start,end)

File "/env/local/lib/python2.7/site-packages/pandas_datareader/data.py", line 322, in DataReader      session=session).read()

File "/e
nv/local/lib/python2.7/site-packages/pandas_datareader/iex/daily.py", line 91, in read      " \
                                                                   "" \
                                                                   "self._get_params(self.symbols))    " \
                                                                   "" \
                                                                   "File "/env/local/lib/python2.7/site-packages/pandas_datarea
der/base.py", line 89, in _read_one_data      return self._read_lines(out)    " \
           "" \
           "File "/env/local/lib/python2.7/site-packages/pandas_datareader/iex/daily.py", line 104, in _read_lines

d = json_data.pop(symbol)["chart"]  KeyError: u'A'