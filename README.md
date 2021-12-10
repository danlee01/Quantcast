# Most Active Cookie

CLI applications that returns the most active cookie on a given day.

## Running
Run `python most_active_cookie.py {log_file} {-d UTC_DATE}`.

```console
$ python most_active_cookie.py tests/test.csv -d 2018-12-09
AtY0laUfhglK3lC7
```
## Testing
To test, run `python3 -m pytest test_module.py`