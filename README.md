# Ansible regression ansible.builtin.uri
Example role to demonstrate regression in ansible.builtin.uri module where the json dictionary is not returned when the status code is not 200 and the python interpreter is python2.

full details of issue here: https://github.com/ansible/ansible/issues/79592

[Documentation](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html#parameter-return_content) states the following about `return_content` key.

        Independently of this option, if the reported Content-type is
        “application/json”, then the JSON is always loaded into a key called json in the
        dictionary results.

The problem is no matter whether the return_content is `true` or `false`, if the `Content-type: application/json` is returned when the target system is running `python2`, and the status code is not something like `200` the json key is not returned.

## To reproduce issue
### working in 2.11
```
rm -rf .venv
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements_2.11.1.txt
# see that the json dictionary is returned
molecule converge
```

### not working in 2.13+
```
rm -rf .venv
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements_2.13.7.txt
# see that the json dictionary is not returned
molecule converge
# see that the json dictionary is not returned
pip install -r requirements_2.14.1.txt
molecule converge
```
