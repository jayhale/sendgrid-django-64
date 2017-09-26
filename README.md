# fix/64

https://github.com/elbuo8/sendgrid-django/issues/65
https://github.com/elbuo8/sendgrid-django/issues/64

## Replication attempt
```
$ git clone git@github.com:jayhale/sendgrid-django-64.git

$ cd sendgrid-django-64

$ pytest test.py
```

## Result
```
========================================= test session starts =========================================
platform darwin -- Python 3.6.2, pytest-3.2.2, py-1.4.34, pluggy-0.4.0
rootdir: /Users/james/Projects/sendgrid-django-64, inifile:
collected 2 items                                                                                      

test.py ..

====================================== 2 passed in 1.35 seconds ======================================
```

## Conclusion
Issue resolved by #58